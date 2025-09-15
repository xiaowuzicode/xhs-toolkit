"""
小红书 API 适配器模块

基于 xhs-mcp 项目的 API 实现，适配现有的 cookie 管理机制
提供搜索笔记、获取笔记内容和评论等功能
"""

import asyncio
import json
import time
import os
from collections.abc import Mapping
from urllib.parse import urlencode, urlparse, parse_qs
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
from numbers import Integral
from typing import Iterable
import random
import base64

try:
    import requests
    from curl_cffi.requests import AsyncSession, Response
    import execjs
except ImportError as e:
    raise ImportError(f"缺少必要的依赖: {e}. 请运行: pip install curl_cffi execjs") from e

from ..core.config import XHSConfig
from ..utils.logger import get_logger

logger = get_logger(__name__)


class XhsApiAdapter:
    """小红书 API 适配器类"""
    
    def __init__(self, config: XHSConfig):
        """
        初始化 XHS API 适配器
        
        Args:
            config: 配置管理器实例
        """
        self.config = config
        self._base_url = "https://edith.xiaohongshu.com" 
        # 使用与原始xhs-mcp完全相同的headers
        self._headers = {
            'content-type': 'application/json;charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }
        
        # 获取 xhsvm.js 文件路径
        self._js_file_path = Path(__file__).parent / "xhsvm.js"
        
        logger.debug(f"XhsApiAdapter 初始化完成，JS文件路径: {self._js_file_path}")
    
    def _cookies_list_to_string(self, cookies_list: List[Dict[str, Any]]) -> str:
        """
        将 cookies 列表转换为字符串格式
        
        Args:
            cookies_list: Cookie 字典列表（来自 selenium）
            
        Returns:
            Cookie 字符串，格式为 "key1=value1; key2=value2"
        """
        if not cookies_list:
            return ""
        
        cookie_pairs = []
        for cookie in cookies_list:
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            if name and value:
                cookie_pairs.append(f"{name}={value}")
        
        result = "; ".join(cookie_pairs)
        logger.debug(f"转换了 {len(cookies_list)} 个cookies -> {len(result)} 字符")
        return result
    
    def _parse_cookie(self, cookie: str) -> Dict:
        """
        解析 cookie 字符串为字典格式
        
        Args:
            cookie: Cookie 字符串
            
        Returns:
            Cookie 字典
        """
        cookie_dict = {}
        if cookie:
            pairs = cookie.split(';')
            for pair in pairs:
                if '=' in pair:
                    key, value = pair.strip().split('=', 1)
                    cookie_dict[key] = value
        return cookie_dict
    
    def init_session(self):
        """初始化 HTTP 会话"""
        return AsyncSession(
            verify=True,
            impersonate="chrome124"
        )
    
    async def request(self, uri: str, session=None, method="GET", headers=None, params=None, data=None) -> Dict:
        """
        发送 HTTP 请求
        
        Args:
            uri: API 路径
            session: HTTP 会话
            method: 请求方法
            headers: 请求头
            params: URL 参数
            data: 请求数据
            
        Returns:
            响应数据字典
        """
        if session is None:
            session = self.init_session()
        if headers is None:
            headers = {}
        
        # 合并默认headers
        merged_headers = self._headers.copy()
        merged_headers.update(headers)
        
        # 根据API类型选择合适的cookie
        if uri in ["/api/sns/web/v1/search/notes", "/api/sns/web/v1/feed", "/api/sns/web/v2/comment/page"]:
            # 搜索和内容相关API使用主站cookies
            cookie_string = self._get_main_site_cookie_string()
            logger.info("🔍 搜索相关API，使用主站cookies")
        else:
            # 其他API使用创作者cookies（保持原有功能）
            cookie_string = self._get_creator_cookie_string()
            logger.info("✍️ 创作者功能API，使用创作者cookies")
        
        logger.info(f"请求URL: {self._base_url}{uri}")
        logger.info(f"请求方法: {method}")
        logger.info(f"请求头: {merged_headers}")
        logger.info(f"Cookie前50字符: {cookie_string[:50]}...")
        
        response: Response = await session.request(
            method=method,
            url=f"{self._base_url}{uri}",
            params=params,
            json=data,
            cookies=self._parse_cookie(cookie_string),
            quote=False,
            stream=True,
            headers=merged_headers
        )
        
        content = await response.acontent()
        logger.info(f"响应状态码: {response.status_code}")
        return json.loads(content)
    
    def _get_creator_cookie_string(self) -> str:
        """
        获取创作者后台的 cookie 字符串（用于发布等功能）
        
        Returns:
            Cookie 字符串
        """
        try:
            # 使用现有的 cookie 管理器加载 cookies (creator后台)
            from ..auth.cookie_manager import CookieManager
            cookie_manager = CookieManager(self.config)
            cookies_list = cookie_manager.load_cookies()
            
            if not cookies_list:
                logger.warning("未找到创作者后台的 cookies")
                return ""
            
            cookie_string = self._cookies_list_to_string(cookies_list)
            logger.debug(f"获取到创作者cookie字符串长度: {len(cookie_string)}")
            return cookie_string
            
        except Exception as e:
            logger.error(f"获取创作者cookie失败: {e}")
            return ""
    
    def _get_main_site_cookie_string(self) -> str:
        """
        获取主站的 cookie 字符串（用于搜索等功能）
        
        Returns:
            Cookie 字符串
        """
        try:
            # 首先尝试从环境变量获取主站cookies
            import os
            env_cookie = os.getenv('XHS_MAIN_COOKIE')
            if env_cookie:
                logger.debug("使用环境变量中的 XHS_MAIN_COOKIE")
                return env_cookie
            
            # 如果没有专门的主站cookie，尝试使用通用的XHS_COOKIE
            env_cookie = os.getenv('XHS_COOKIE')
            if env_cookie:
                logger.debug("使用环境变量中的 XHS_COOKIE 作为主站cookie")
                return env_cookie
            
            # 最后尝试使用创作者cookie（向后兼容）
            logger.warning("未找到主站cookies，尝试使用创作者cookies")
            return self._get_creator_cookie_string()
            
        except Exception as e:
            logger.error(f"获取主站cookie失败: {e}")
            return ""
    
    def _get_current_cookie_string(self) -> str:
        """
        获取当前操作需要的 cookie 字符串（保持向后兼容）
        
        Returns:
            Cookie 字符串
        """
        # 为了保持向后兼容，默认返回主站cookies
        return self._get_main_site_cookie_string()
    
    def base36encode(self, number: Integral, alphabet: Iterable[str] = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> str:
        """Base36 编码"""
        base36 = ''
        alphabet = ''.join(alphabet)
        sign = '-' if number < 0 else ''
        number = abs(number)
        
        while number:
            number, i = divmod(number, len(alphabet))
            base36 = alphabet[i] + base36
        
        return sign + (base36 or alphabet[0])
    
    def search_id(self):
        """生成搜索 ID"""
        e = int(time.time() * 1000) << 64
        t = int(random.uniform(0, 2147483646))
        return self.base36encode((e + t))
    
    def get_xs_xt(self, uri, data, cookie):
        """
        生成 X-s 和 X-t 签名
        
        Args:
            uri: API 路径
            data: 请求数据
            cookie: Cookie 字符串
            
        Returns:
            包含 X-s 和 X-t 的字典
        """
        try:
            if not self._js_file_path.exists():
                logger.error(f"JavaScript 签名文件不存在: {self._js_file_path}")
                return json.dumps({"X-s": "", "X-t": ""})
            
            with open(self._js_file_path, 'r', encoding='utf-8') as f:
                js_code = f.read()
            
            result = execjs.compile(js_code).call('GetXsXt', uri, data, cookie)
            logger.debug("成功生成 X-s/X-t 签名")
            return result
            
        except Exception as e:
            logger.error(f"生成签名失败: {e}")
            return json.dumps({"X-s": "", "X-t": ""})
    
    def get_nodeid_token(self, url=None, note_ids=None):
        """
        从 URL 中提取 note_id 和 xsec_token
        
        Args:
            url: 笔记 URL
            note_ids: 可选的 note_ids 参数
            
        Returns:
            包含 note_id 和 xsec_token 的字典
        """
        if note_ids is not None:
            note_id = note_ids[0:24]
            xsec_token = note_ids[24:]
            return {"note_id": note_id, "xsec_token": xsec_token}
        
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        note_id = parsed_url.path.split('/')[-1]
        xsec_token = None
        xsec_token_list = query_params.get('xsec_token', [None])
        if len(xsec_token_list) > 0:
            xsec_token = xsec_token_list[0]
        
        return {"note_id": note_id, "xsec_token": xsec_token}
    
    async def check_cookie(self) -> str:
        """
        检测 cookie 是否有效
        
        Returns:
            检测结果字符串
        """
        try:
            data = await self.get_me()
            
            if 'success' in data and data['success'] == True:
                return "cookie有效"
            else:
                return "cookie已失效"
        except Exception as e:
            logger.error(f"检查 cookie 失败: {e}")
            return "cookie已失效"
    
    async def get_me(self) -> Dict:
        """获取用户信息"""
        uri = '/api/sns/web/v2/user/me'
        return await self.request(uri, method="GET")
    
    async def search_notes(self, keywords: str, limit: int = 20) -> Dict:
        """
        根据关键词搜索笔记
        
        Args:
            keywords: 搜索关键词
            limit: 返回结果数量限制
            
        Returns:
            搜索结果字典
        """
        logger.info(f"开始搜索笔记，关键词: {keywords}")
        
        try:
            data = {
                "keyword": keywords,
                "page": 1,
                "page_size": limit,
                "search_id": self.search_id(),
                "sort": "general",
                "note_type": 0,
                "ext_flags": [],
                "geo": "",
                "image_formats": json.dumps(["jpg", "webp", "avif"], separators=(",", ":"))
            }
            
            result = await self.request("/api/sns/web/v1/search/notes", method="POST", data=data)
            logger.info(f"搜索完成，关键词: {keywords}")
            logger.info(f"API返回完整数据: {result}")
            
            # 检查API是否返回错误
            if isinstance(result, dict):
                if 'success' in result and not result['success']:
                    logger.error(f"API返回错误: code={result.get('code')}, msg={result.get('msg')}")
                elif 'code' in result and result['code'] != 0:
                    logger.error(f"API返回错误代码: {result['code']}, msg={result.get('msg')}")
            
            return result
            
        except Exception as e:
            logger.error(f"搜索笔记失败: {e}")
            return {"error": str(e)}
    
    async def get_note_content(self, note_id: str, xsec_token: str) -> Dict:
        """
        获取笔记内容
        
        Args:
            note_id: 笔记 ID
            xsec_token: xsec_token 参数
            
        Returns:
            笔记内容字典
        """
        logger.info(f"开始获取笔记内容，note_id: {note_id}")
        
        try:
            data = {
                "source_note_id": note_id,
                "image_formats": ["jpg", "webp", "avif"],
                "extra": {"need_body_topic": "1"},
                "xsec_source": "pc_feed",
                "xsec_token": xsec_token
            }
            
            uri = "/api/sns/web/v1/feed"
            p = {"uri": uri, "method": "POST", "data": data}
            
            headers = {
                'content-type': 'application/json;charset=UTF-8',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }
            
            # 生成签名
            cookie_string = self._get_current_cookie_string()
            xsxt = json.loads(self.get_xs_xt(uri, data, cookie_string))
            headers['x-s'] = xsxt['X-s']
            headers['x-t'] = str(xsxt['X-t'])
            headers['x-s-common'] = '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'
            
            result = await self.request(**p, headers=headers)
            logger.info(f"获取笔记内容完成，note_id: {note_id}")
            return result
            
        except Exception as e:
            logger.error(f"获取笔记内容失败: {e}")
            return {"error": str(e)}
    
    async def get_note_comments(self, note_id: str, xsec_token: str) -> Dict:
        """
        获取笔记评论
        
        Args:
            note_id: 笔记 ID
            xsec_token: xsec_token 参数
            
        Returns:
            笔记评论字典
        """
        logger.info(f"开始获取笔记评论，note_id: {note_id}")
        
        try:
            uri = '/api/sns/web/v2/comment/page'
            params = {
                'note_id': note_id,
                'cursor': '',
                'top_comment_id': '',
                'image_formats': 'jpg,webp,avif',
                'xsec_token': xsec_token
            }
            
            result = await self.request(uri, method="GET", params=params)
            logger.info(f"获取笔记评论完成，note_id: {note_id}")
            return result
            
        except Exception as e:
            logger.error(f"获取笔记评论失败: {e}")
            return {"error": str(e)}


def create_xhs_api_adapter(config: XHSConfig) -> XhsApiAdapter:
    """
    创建 XHS API 适配器的便捷函数
    
    Args:
        config: 配置管理器实例
        
    Returns:
        XHS API 适配器实例
    """
    return XhsApiAdapter(config)
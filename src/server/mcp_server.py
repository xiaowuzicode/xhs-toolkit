"""
小红书MCP服务器模块

提供MCP协议的服务器实现，支持AI客户端通过MCP协议与小红书交互
"""

import os
import json
import asyncio
import signal
import sys
import socket
import uuid
import time
from pathlib import Path
from typing import Dict, Any, List, Union, Optional

from dataclasses import dataclass, asdict

from fastmcp import FastMCP

from ..core.config import XHSConfig
from ..core.exceptions import format_error_message, XHSToolkitError
from ..xiaohongshu.client import XHSClient
from ..xiaohongshu.models import XHSNote
from ..utils.logger import get_logger, setup_logger
from ..data import storage_manager, data_scheduler
from ..auth.smart_auth_server import SmartAuthServer, create_smart_auth_server
from .xhs_api_adapter import XhsApiAdapter

logger = get_logger(__name__)


@dataclass
class PublishTask:
    """发布任务数据类"""
    task_id: str
    status: str  # "pending", "uploading", "filling", "publishing", "completed", "failed"
    note: XHSNote
    progress: int  # 0-100
    message: str
    result: Dict[str, Any] = None
    start_time: float = None
    end_time: float = None

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        data = asdict(self)
        # 移除note对象，避免序列化问题
        if 'note' in data:
            data['note_title'] = self.note.title
            data['note_has_images'] = bool(self.note.images)
            data['note_has_videos'] = bool(self.note.videos)
            del data['note']
        return data


class TaskManager:
    """任务管理器"""

    def __init__(self):
        self.tasks: Dict[str, PublishTask] = {}
        self.running_tasks: Dict[str, asyncio.Task] = {}

    def create_task(self, note: XHSNote) -> str:
        """创建新任务"""
        task_id = str(uuid.uuid4())[:8]  # 使用短ID
        task = PublishTask(
            task_id=task_id,
            status="pending",
            note=note,
            progress=0,
            message="任务已创建，准备开始",
            start_time=time.time()
        )
        self.tasks[task_id] = task
        logger.info(f"📋 创建新任务: {task_id} - {note.title}")
        return task_id

    def get_task(self, task_id: str) -> PublishTask:
        """获取任务"""
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, status: str = None, progress: int = None, message: str = None, result: Dict = None):
        """更新任务状态"""
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if status:
                task.status = status
            if progress is not None:
                task.progress = progress
            if message:
                task.message = message
            if result:
                task.result = result
            if status in ["completed", "failed"]:
                task.end_time = time.time()
            logger.info(f"📋 更新任务 {task_id}: {status} ({progress}%) - {message}")

    def remove_old_tasks(self, max_age_seconds: int = 3600):
        """移除超过指定时间的旧任务"""
        current_time = time.time()
        expired_tasks = []
        for task_id, task in self.tasks.items():
            if task.end_time and (current_time - task.end_time) > max_age_seconds:
                expired_tasks.append(task_id)

        for task_id in expired_tasks:
            del self.tasks[task_id]
            if task_id in self.running_tasks:
                self.running_tasks[task_id].cancel()
                del self.running_tasks[task_id]
            logger.info(f"🗑️ 清理过期任务: {task_id}")


class MCPServer:
    """MCP服务器管理器"""

    def __init__(self, config: XHSConfig):
        """
        初始化MCP服务器
        
        Args:
            config: 配置管理器实例
        """
        self.config = config
        self.xhs_client = XHSClient(config)
        self.mcp = FastMCP("小红书MCP服务器")
        self.task_manager = TaskManager()  # 添加任务管理器
        self.scheduler_initialized = False  # 调度器初始化标志
        self.auth_server = create_smart_auth_server(config)  # 智能认证服务器
        self.xhs_api_adapter = XhsApiAdapter(config)  # XHS API 适配器
        self._setup_tools()
        self._setup_resources()
        self._setup_prompts()

    async def _initialize_data_collection(self) -> None:
        """初始化数据采集功能"""
        if self.scheduler_initialized:
            return  # 已经初始化过了

        try:
            import os
            logger.info("📊 初始化数据采集功能...")

            # 检查cookies是否存在，数据采集需要登录状态
            cookies = self.xhs_client.cookie_manager.load_cookies()
            if not cookies:
                logger.warning("⚠️ 未找到cookies文件，跳过数据采集功能初始化")
                logger.info("💡 数据采集需要登录状态，请先运行: python xhs_toolkit.py cookie save")
                self.scheduler_initialized = False
                return

            logger.info(f"✅ 检测到 {len(cookies)} 个cookies，可以进行数据采集")

            # 初始化存储管理器
            storage_manager.initialize()
            storage_info = storage_manager.get_storage_info()
            logger.info(f"💾 存储配置: {storage_info['storage_types']}")

            # 检查是否启用自动采集
            enable_auto_collection = os.getenv('ENABLE_AUTO_COLLECTION', 'false').lower() == 'true'

            if enable_auto_collection:
                # 初始化调度器
                data_scheduler.initialize(self.xhs_client)

                # 启动调度器
                await data_scheduler.start()

                if data_scheduler.is_running():
                    job_info = data_scheduler.get_job_info()
                    logger.info("⏰ 数据采集调度器已启动")

                    # 显示下次执行时间
                    if job_info.get('jobs'):
                        for job in job_info['jobs']:
                            next_run = job.get('next_run_time')
                            if next_run:
                                logger.info(f"📅 下次采集时间: {next_run}")
                else:
                    logger.warning("⚠️ 调度器启动失败")
            else:
                logger.info("📊 自动数据采集已禁用")

            self.scheduler_initialized = True

        except Exception as e:
            import traceback
            logger.error(f"❌ 数据采集功能初始化失败: {e}")
            logger.error(f"❌ 错误详情: {traceback.format_exc()}")
            self.scheduler_initialized = False

    def _setup_tools(self) -> None:
        """设置MCP工具"""

        @self.mcp.tool()
        async def test_connection() -> str:
            """
            测试MCP连接是否正常
            
            Returns:
                连接状态信息
            """
            logger.info("🧪 收到连接测试请求")
            try:
                import time
                import os
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                # 检查配置
                config_status = self.config.to_dict()
                config_status["current_time"] = current_time

                # 添加数据采集状态
                config_status["data_collection"] = {
                    "scheduler_initialized": self.scheduler_initialized,
                    "auto_collection_enabled": os.getenv('ENABLE_AUTO_COLLECTION', 'false').lower() == 'true',
                    "storage_info": storage_manager.get_storage_info() if self.scheduler_initialized else None
                }

                logger.info(f"✅ 连接测试完成: {config_status}")

                result = {
                    "status": "success",
                    "message": "MCP连接正常！",
                    "config": config_status,
                    "timestamp": current_time
                }

                return json.dumps(result, ensure_ascii=False, indent=2)

            except Exception as e:
                error_msg = f"连接测试失败: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return error_msg

        @self.mcp.tool()
        async def smart_publish_note(title: str,
                                     content: str,
                                     images: Optional[Union[str, List[str]]] = None,
                                     videos: Optional[Union[str, List[str]]] = None,
                                     topics: Optional[Union[str, List[str]]] = None,
                                     location: str = "", is_commercial: bool = False) -> str:
            """
            发布小红书笔记（支持多种输入格式）
            
            这是主要的笔记发布工具，支持更灵活的参数输入，可以处理来自不同平台的各种数据格式。
            
            Args:
                title (str): 笔记标题
                content (str): 笔记内容  
                images: 图片，支持格式：
                       - 本地路径："image.jpg" 或 ["/path/to/image.jpg"]
                       - 网络地址："https://example.com/image.jpg"
                       - 混合数组：["local.jpg", "https://example.com/img.jpg"]
                       - 逗号分隔字符串："a.jpg,b.jpg,c.jpg"
                videos: 视频路径（目前仅支持本地文件）
                topics: 话题，支持字符串或数组格式
                        例如 "话题1,话题2" 或 ["话题1", "话题2"]
                location (str, optional): 位置信息
                is_commercial (boolean): 是否为商业笔记
            
            Returns:
                str: 任务ID和状态信息
                
            示例:
                # 使用网络图片
                smart_publish_note(
                    title="美食分享",
                    content="今天的美食",
                    images="a.jpg,b.jpg,c.jpg"
                    topics="话题1,话题2"
                )
                
            """
            logger.info(f"🚀 启动发布任务: 标题='{title}'")
            logger.debug(f"📋 参数详情: images={images}, videos={videos}, topics={topics}")

            try:
                # 使用异步智能创建方法
                note = await XHSNote.async_smart_create(
                    title=title,
                    content=content,
                    topics=topics,
                    location=location,
                    images=images,
                    videos=videos,
                    is_commercial=is_commercial
                )

                # 记录解析结果
                logger.info(
                    f"✅ 智能解析结果: 图片{len(note.images) if note.images else 0}张, 视频{len(note.videos) if note.videos else 0}个, 话题{len(note.topics) if note.topics else 0}个")

                # 创建异步任务
                task_id = self.task_manager.create_task(note)

                # 启动后台任务
                async_task = asyncio.create_task(self._execute_publish_task(task_id))
                self.task_manager.running_tasks[task_id] = async_task

                result = {
                    "success": True,
                    "task_id": task_id,
                    "message": f"发布任务已启动，任务ID: {task_id}",
                    "next_step": f"请使用 check_task_status('{task_id}') 查看进度",
                    "parsing_result": {
                        "images_parsed": note.images if note.images else [],
                        "videos_parsed": note.videos if note.videos else [],
                        "topics_parsed": note.topics if note.topics else [],
                        "images_count": len(note.images) if note.images else 0,
                        "videos_count": len(note.videos) if note.videos else 0,
                        "topics_count": len(note.topics) if note.topics else 0,
                        "content_type": "图文" if note.images else "视频" if note.videos else "纯文本"
                    }
                }

                return json.dumps(result, ensure_ascii=False, indent=2)

            except Exception as e:
                error_msg = f"发布任务启动失败: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": error_msg,
                    "suggestion": "请检查输入格式，确保图片/视频路径正确或网络连接正常"
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def check_task_status(task_id: str) -> str:
            """
            检查发布任务状态
            
            Args:
                task_id (str): 任务ID
            
            Returns:
                str: 任务状态信息
            """
            logger.info(f"📊 检查任务状态: {task_id}")

            task = self.task_manager.get_task(task_id)
            if not task:
                return json.dumps({
                    "success": False,
                    "message": f"任务 {task_id} 不存在"
                }, ensure_ascii=False, indent=2)

            # 计算运行时间
            elapsed_time = 0
            if task.start_time:
                elapsed_time = int(time.time() - task.start_time)

            result = {
                "success": True,
                "task_id": task_id,
                "status": task.status,
                "progress": task.progress,
                "message": task.message,
                "elapsed_seconds": elapsed_time,
                "is_completed": task.status in ["completed", "failed"]
            }

            # 如果任务完成，包含结果
            if task.result:
                result["result"] = task.result

            return json.dumps(result, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def get_task_result(task_id: str) -> str:
            """
            获取已完成任务的结果
            
            Args:
                task_id (str): 任务ID
            
            Returns:
                str: 任务结果信息
            """
            logger.info(f"📋 获取任务结果: {task_id}")

            task = self.task_manager.get_task(task_id)
            if not task:
                return json.dumps({
                    "success": False,
                    "message": f"任务 {task_id} 不存在"
                }, ensure_ascii=False, indent=2)

            if task.status not in ["completed", "failed"]:
                return json.dumps({
                    "success": False,
                    "message": f"任务 {task_id} 尚未完成，当前状态: {task.status}",
                    "current_status": task.status,
                    "progress": task.progress
                }, ensure_ascii=False, indent=2)

            # 返回完整结果
            result = {
                "success": task.status == "completed",
                "task_id": task_id,
                "status": task.status,
                "message": task.message,
                "execution_time": int(task.end_time - task.start_time) if task.end_time and task.start_time else 0
            }

            if task.result:
                result["publish_result"] = task.result

            return json.dumps(result, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def login_xiaohongshu(force_relogin: bool = False, quick_mode: bool = False) -> str:
            """
            智能登录小红书
            
            当用户说"登录小红书"时调用此工具。提供MCP专用的智能流程，无需用户交互确认。
            
            Args:
                force_relogin: 是否强制重新登录，即使当前状态有效
                quick_mode: 快速模式，降低验证要求以避免超时
                
            Returns:
                登录结果的JSON字符串
            """
            logger.info(f"🚀 MCP工具调用：智能小红书 (force_relogin={force_relogin}, quick_mode={quick_mode})")

            try:
                # 如果是快速模式，先检查是否已有cookies
                if quick_mode:
                    cookies_file = Path(self.config.cookies_file)
                    if cookies_file.exists():
                        logger.info("⚡ 快速模式：发现已有cookies，跳过登录")
                        return json.dumps({
                            "success": True,
                            "message": "✅ 快速模式：检测到已有cookies，跳过登录流程",
                            "action": "quick_skip",
                            "status": "valid",
                            "mode": "mcp_quick"
                        }, ensure_ascii=False, indent=2)

                # 使用MCP专用的智能模式
                result = await self.auth_server.smart_login(interactive=False, mcp_mode=True)

                # 格式化返回消息
                if result.get("success", False):
                    action = result.get("action", "unknown")
                    if action == "mcp_auto_login":
                        message = f"✅ {result['message']}\n🤖 MCP智能登录已完成，cookies已保存"
                    elif action == "skipped":
                        message = f"✅ {result['message']}\n💡 当前登录状态有效"
                    else:
                        message = f"✅ {result['message']}"
                else:
                    message = f"❌ {result['message']}\n🔧 请检查浏览器或网络连接"

                logger.info(f"✅ MCP自动登录结果: {result.get('action', 'unknown')}")
                return json.dumps({
                    "success": result.get("success", False),
                    "message": message,
                    "action": result.get("action", "unknown"),
                    "status": result.get("status", "unknown"),
                    "mode": "mcp_auto"
                }, ensure_ascii=False, indent=2)

            except Exception as e:
                error_msg = f"MCP自动登录执行失败: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": f"❌ {error_msg}",
                    "error": str(e),
                    "mode": "mcp_auto",
                    "suggestion": "可以尝试快速模式：login_xiaohongshu(quick_mode=True)"
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def get_creator_data_analysis() -> str:
            """
            获取创作者数据用于分析
            
            Returns:
                str: 包含所有创作者数据的详细信息用于数据分析
            """
            logger.info("📊 获取创作者数据用于分析")

            try:
                # 检查cookies是否存在，数据分析需要登录状态
                cookies = self.xhs_client.cookie_manager.load_cookies()
                if not cookies:
                    return json.dumps({
                        "success": False,
                        "message": "数据分析需要登录状态，未找到cookies文件",
                        "suggestion": "请先运行: python xhs_toolkit.py cookie save"
                    }, ensure_ascii=False, indent=2)

                if not self.scheduler_initialized:
                    return json.dumps({
                        "success": False,
                        "message": "数据采集功能未初始化，可能因为cookies问题",
                        "suggestion": "请检查cookies状态并重启服务器"
                    }, ensure_ascii=False, indent=2)

                # 获取存储管理器
                csv_storage = storage_manager.get_csv_storage()

                # 读取所有数据
                dashboard_data = await csv_storage.get_latest_data('dashboard', limit=100)
                content_data = await csv_storage.get_latest_data('content_analysis', limit=100)
                fans_data = await csv_storage.get_latest_data('fans', limit=100)

                # 获取存储信息
                storage_info = storage_manager.get_storage_info()

                result = {
                    "success": True,
                    "message": "创作者数据获取成功，可用于分析",
                    "data_summary": {
                        "dashboard_records": len(dashboard_data),
                        "content_records": len(content_data),
                        "fans_records": len(fans_data),
                        "storage_info": storage_info
                    },
                    "dashboard_data": dashboard_data,
                    "content_analysis_data": content_data,
                    "fans_data": fans_data,
                    "analysis_tips": {
                        "dashboard": "仪表板数据包含账号整体表现指标",
                        "content": "内容分析数据包含每篇笔记的详细表现",
                        "fans": "粉丝数据包含粉丝增长趋势"
                    },
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }

                return json.dumps(result, ensure_ascii=False, indent=2)

            except Exception as e:
                error_msg = f"获取创作者数据失败: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": error_msg
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def parse_xiaohongshu_url(url: str, include_raw_html: bool = False) -> str:
            """
            解析小红书URL，提取页面内容信息
            
            支持解析小红书的各种页面类型：笔记页面、用户主页等，提取其中的文本内容、图片、作者信息等结构化数据。
            
            Args:
                url (str): 小红书页面URL，支持格式：
                          - 笔记链接：https://www.xiaohongshu.com/explore/...
                          - 用户主页：https://www.xiaohongshu.com/user/profile/...
                          - 其他小红书页面URL
                include_raw_html (bool): 是否在结果中包含原始HTML内容（用于调试，默认False）
            
            Returns:
                str: 解析结果的JSON字符串，包含以下信息：
                    - success: 解析是否成功
                    - url: 原始URL
                    - page_type: 页面类型（note/user/topic/unknown）
                    - title: 页面标题
                    - content: 页面文本内容
                    - author: 作者信息
                    - images: 图片URL列表
                    - tags: 标签/话题列表
                    - likes/comments/shares: 互动数据
                    - publish_time: 发布时间
                    - error_message: 错误信息（如果失败）
                    
            示例:
                parse_xiaohongshu_url("https://www.xiaohongshu.com/explore/...")
                parse_xiaohongshu_url("https://www.xiaohongshu.com/user/profile/...", include_raw_html=True)
            """
            logger.info(f"🔍 收到URL解析请求: {url}")
            
            try:
                # 基本URL验证
                if not url or not isinstance(url, str):
                    return json.dumps({
                        "success": False,
                        "url": url,
                        "error_message": "URL不能为空且必须是字符串"
                    }, ensure_ascii=False, indent=2)
                
                # 检查是否为小红书URL
                if "xiaohongshu.com" not in url and "xhslink.com" not in url:
                    return json.dumps({
                        "success": False,
                        "url": url,
                        "error_message": "只支持解析小红书官方链接（包含xiaohongshu.com或xhslink.com）"
                    }, ensure_ascii=False, indent=2)
                
                # 创建新的客户端实例进行解析
                client = XHSClient(self.config)
                
                # 执行URL解析
                result = await client.parse_xiaohongshu_url(url, include_raw_html)
                
                # 格式化返回结果
                response_data = result.to_dict()
                
                # 添加解析统计信息
                response_data["parsing_stats"] = {
                    "images_found": len(result.images) if result.images else 0,
                    "tags_found": len(result.tags) if result.tags else 0,
                    "has_author": bool(result.author),
                    "has_content": bool(result.content),
                    "page_type": result.page_type
                }
                
                # 成功日志
                if result.success:
                    logger.info(f"✅ URL解析成功 - 类型: {result.page_type}, 标题: {result.title}")
                else:
                    logger.warning(f"⚠️ URL解析失败: {result.error_message}")
                
                return json.dumps(response_data, ensure_ascii=False, indent=2)
                
            except Exception as e:
                error_msg = f"URL解析过程出错: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "url": url,
                    "error_message": error_msg,
                    "suggestion": "请检查URL格式是否正确，或稍后重试"
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def search_notes(keywords: str) -> str:
            """
            根据关键词搜索笔记
            
            这个工具基于小红书官方API实现，可以根据用户输入的关键词搜索相关的笔记内容。
            搜索结果包括笔记标题、点赞数、链接等信息，帮助用户快速找到感兴趣的内容。
            
            Args:
                keywords (str): 搜索关键词，例如："美食推荐"、"护肤心得"、"旅行攻略"等
            
            Returns:
                str: 搜索结果的JSON字符串，包含以下信息：
                    - success: 搜索是否成功
                    - message: 结果描述信息
                    - results: 搜索结果列表，每个结果包含：
                        * title: 笔记标题
                        * liked_count: 点赞数
                        * url: 笔记链接（包含xsec_token）
                        * index: 结果序号
                    - total_count: 搜索结果总数
                    - error_message: 错误信息（如果失败）
                        
            示例:
                search_notes("美食推荐")
                search_notes("护肤心得")
            """
            logger.info(f"🔍 收到搜索笔记请求: {keywords}")
            
            try:
                # 基本参数验证
                if not keywords or not isinstance(keywords, str):
                    return json.dumps({
                        "success": False,
                        "message": "搜索关键词不能为空且必须是字符串",
                        "error_message": "无效的搜索参数"
                    }, ensure_ascii=False, indent=2)
                
                keywords = keywords.strip()
                if len(keywords) == 0:
                    return json.dumps({
                        "success": False,
                        "message": "搜索关键词不能为空",
                        "error_message": "搜索关键词为空"
                    }, ensure_ascii=False, indent=2)
                
                # 调用API搜索
                data = await self.xhs_api_adapter.search_notes(keywords)
                
                # 处理搜索结果
                results = []
                if 'data' in data and 'items' in data['data'] and len(data['data']['items']) > 0:
                    for i, item in enumerate(data['data']['items']):
                        if 'note_card' in item and 'display_title' in item['note_card']:
                            title = item['note_card']['display_title']
                            liked_count = item['note_card']['interact_info']['liked_count']
                            url = f'https://www.xiaohongshu.com/explore/{item["id"]}?xsec_token={item["xsec_token"]}'
                            
                            results.append({
                                "index": i,
                                "title": title,
                                "liked_count": liked_count,
                                "url": url
                            })
                    
                    # 成功找到结果
                    result_data = {
                        "success": True,
                        "message": f"成功找到 {len(results)} 条与「{keywords}」相关的笔记",
                        "keywords": keywords,
                        "results": results,
                        "total_count": len(results)
                    }
                    
                    logger.info(f"✅ 搜索完成: {keywords} - 找到{len(results)}条结果")
                    return json.dumps(result_data, ensure_ascii=False, indent=2)
                else:
                    # 检查是否是cookie问题
                    cookie_status = await self.xhs_api_adapter.check_cookie()
                    if "有效" in cookie_status:
                        # Cookie有效但没找到结果
                        result_data = {
                            "success": True,
                            "message": f"未找到与「{keywords}」相关的笔记",
                            "keywords": keywords,
                            "results": [],
                            "total_count": 0
                        }
                    else:
                        # Cookie无效
                        result_data = {
                            "success": False,
                            "message": "搜索失败：登录状态无效",
                            "keywords": keywords,
                            "error_message": "需要重新登录小红书",
                            "suggestion": "请先运行登录工具：login_xiaohongshu()"
                        }
                    
                    logger.warning(f"⚠️ 搜索无结果或Cookie失效: {keywords}")
                    return json.dumps(result_data, ensure_ascii=False, indent=2)
                    
            except Exception as e:
                error_msg = f"搜索笔记过程出错: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": "搜索笔记失败",
                    "keywords": keywords,
                    "error_message": error_msg,
                    "suggestion": "请检查网络连接或稍后重试"
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def get_note_content(url: str) -> str:
            """
            获取笔记内容，参数url要带上xsec_token
            
            这个工具可以获取指定小红书笔记的详细内容，包括标题、作者信息、发布时间、
            互动数据（点赞、评论、收藏）以及笔记正文内容。需要提供包含xsec_token的完整URL。
            
            Args:
                url (str): 笔记URL，必须包含xsec_token参数
                          格式：https://www.xiaohongshu.com/explore/{note_id}?xsec_token={token}
                          可以从search_notes的结果中获取此格式的URL
            
            Returns:
                str: 笔记内容的JSON字符串，包含以下信息：
                    - success: 获取是否成功
                    - message: 结果描述信息
                    - note_info: 笔记信息（如果成功），包含：
                        * title: 笔记标题
                        * author: 作者昵称
                        * publish_time: 发布时间
                        * liked_count: 点赞数
                        * comment_count: 评论数
                        * collected_count: 收藏数
                        * content: 笔记正文内容
                        * cover_image: 封面图片URL
                        * url: 笔记链接
                    - error_message: 错误信息（如果失败）
                        
            示例:
                get_note_content("https://www.xiaohongshu.com/explore/123456?xsec_token=abc123")
            """
            logger.info(f"📄 收到获取笔记内容请求: {url}")
            
            try:
                # 基本URL验证
                if not url or not isinstance(url, str):
                    return json.dumps({
                        "success": False,
                        "message": "URL不能为空且必须是字符串",
                        "error_message": "无效的URL参数"
                    }, ensure_ascii=False, indent=2)
                
                # 检查是否为小红书URL
                if "xiaohongshu.com" not in url and "xhslink.com" not in url:
                    return json.dumps({
                        "success": False,
                        "message": "只支持小红书官方链接",
                        "url": url,
                        "error_message": "URL必须包含xiaohongshu.com或xhslink.com"
                    }, ensure_ascii=False, indent=2)
                
                # 提取note_id和xsec_token
                params = self.xhs_api_adapter.get_nodeid_token(url=url)
                note_id = params.get("note_id")
                xsec_token = params.get("xsec_token")
                
                if not note_id:
                    return json.dumps({
                        "success": False,
                        "message": "无法从URL中提取笔记ID",
                        "url": url,
                        "error_message": "URL格式不正确"
                    }, ensure_ascii=False, indent=2)
                
                if not xsec_token:
                    return json.dumps({
                        "success": False,
                        "message": "URL中缺少xsec_token参数",
                        "url": url,
                        "error_message": "需要包含xsec_token的完整URL",
                        "suggestion": "请使用search_notes获取包含xsec_token的URL"
                    }, ensure_ascii=False, indent=2)
                
                # 调用API获取笔记内容
                data = await self.xhs_api_adapter.get_note_content(note_id, xsec_token)
                
                # 处理返回结果
                if 'data' in data and 'items' in data['data'] and len(data['data']['items']) > 0:
                    item = data['data']['items'][0]
                    
                    if 'note_card' in item and 'user' in item['note_card']:
                        note_card = item['note_card']
                        
                        # 提取封面图片
                        cover = ''
                        if 'image_list' in note_card and len(note_card['image_list']) > 0:
                            if note_card['image_list'][0].get('url_pre'):
                                cover = note_card['image_list'][0]['url_pre']
                        
                        # 格式化发布时间
                        publish_time = "未知时间"
                        if note_card.get('time'):
                            try:
                                timestamp = note_card.get('time', 0) / 1000
                                publish_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                            except:
                                publish_time = "时间格式错误"
                        
                        # 提取互动数据
                        interact_info = note_card.get('interact_info', {})
                        liked_count = interact_info.get('liked_count', 0)
                        comment_count = interact_info.get('comment_count', 0)
                        collected_count = interact_info.get('collected_count', 0)
                        
                        # 构建笔记信息
                        note_info = {
                            "title": note_card.get('title', ''),
                            "author": note_card['user'].get('nickname', ''),
                            "publish_time": publish_time,
                            "liked_count": liked_count,
                            "comment_count": comment_count,
                            "collected_count": collected_count,
                            "content": note_card.get('desc', ''),
                            "cover_image": cover,
                            "url": url
                        }
                        
                        result_data = {
                            "success": True,
                            "message": f"成功获取笔记内容：{note_info['title']}",
                            "note_info": note_info
                        }
                        
                        logger.info(f"✅ 获取笔记内容成功: {note_info['title']}")
                        return json.dumps(result_data, ensure_ascii=False, indent=2)
                    else:
                        logger.warning("⚠️ 返回数据结构异常")
                        return json.dumps({
                            "success": False,
                            "message": "笔记数据结构异常",
                            "url": url,
                            "error_message": "API返回数据格式不正确"
                        }, ensure_ascii=False, indent=2)
                else:
                    # 检查是否是cookie问题
                    cookie_status = await self.xhs_api_adapter.check_cookie()
                    if "有效" in cookie_status:
                        error_msg = "获取笔记内容失败，可能是笔记不存在或已被删除"
                    else:
                        error_msg = "获取笔记内容失败：登录状态无效"
                    
                    logger.warning(f"⚠️ 获取笔记内容失败: {url}")
                    return json.dumps({
                        "success": False,
                        "message": error_msg,
                        "url": url,
                        "error_message": "无法获取笔记内容",
                        "suggestion": "请检查URL是否正确或重新登录"
                    }, ensure_ascii=False, indent=2)
                    
            except Exception as e:
                error_msg = f"获取笔记内容过程出错: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": "获取笔记内容失败",
                    "url": url,
                    "error_message": error_msg,
                    "suggestion": "请检查URL格式和网络连接"
                }, ensure_ascii=False, indent=2)

        @self.mcp.tool()
        async def get_note_comments(url: str) -> str:
            """
            获取笔记评论，参数url要带上xsec_token
            
            这个工具可以获取指定小红书笔记的评论列表，包括评论内容、评论者信息和发布时间。
            需要提供包含xsec_token的完整URL。
            
            Args:
                url (str): 笔记URL，必须包含xsec_token参数
                          格式：https://www.xiaohongshu.com/explore/{note_id}?xsec_token={token}
                          可以从search_notes的结果中获取此格式的URL
            
            Returns:
                str: 评论数据的JSON字符串，包含以下信息：
                    - success: 获取是否成功
                    - message: 结果描述信息
                    - comments: 评论列表（如果成功），每个评论包含：
                        * index: 评论序号
                        * author: 评论者昵称
                        * content: 评论内容
                        * create_time: 发布时间
                    - total_count: 评论总数
                    - error_message: 错误信息（如果失败）
                        
            示例:
                get_note_comments("https://www.xiaohongshu.com/explore/123456?xsec_token=abc123")
            """
            logger.info(f"💬 收到获取笔记评论请求: {url}")
            
            try:
                # 基本URL验证
                if not url or not isinstance(url, str):
                    return json.dumps({
                        "success": False,
                        "message": "URL不能为空且必须是字符串",
                        "error_message": "无效的URL参数"
                    }, ensure_ascii=False, indent=2)
                
                # 检查是否为小红书URL
                if "xiaohongshu.com" not in url and "xhslink.com" not in url:
                    return json.dumps({
                        "success": False,
                        "message": "只支持小红书官方链接",
                        "url": url,
                        "error_message": "URL必须包含xiaohongshu.com或xhslink.com"
                    }, ensure_ascii=False, indent=2)
                
                # 提取note_id和xsec_token
                params = self.xhs_api_adapter.get_nodeid_token(url=url)
                note_id = params.get("note_id")
                xsec_token = params.get("xsec_token")
                
                if not note_id:
                    return json.dumps({
                        "success": False,
                        "message": "无法从URL中提取笔记ID",
                        "url": url,
                        "error_message": "URL格式不正确"
                    }, ensure_ascii=False, indent=2)
                
                if not xsec_token:
                    return json.dumps({
                        "success": False,
                        "message": "URL中缺少xsec_token参数",
                        "url": url,
                        "error_message": "需要包含xsec_token的完整URL",
                        "suggestion": "请使用search_notes获取包含xsec_token的URL"
                    }, ensure_ascii=False, indent=2)
                
                # 调用API获取笔记评论
                data = await self.xhs_api_adapter.get_note_comments(note_id, xsec_token)
                
                # 处理返回结果
                comments = []
                if 'data' in data and 'comments' in data['data'] and len(data['data']['comments']) > 0:
                    for i, comment in enumerate(data['data']['comments']):
                        # 格式化评论时间
                        create_time = "未知时间"
                        if comment.get('create_time'):
                            try:
                                timestamp = comment['create_time'] / 1000
                                create_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                            except:
                                create_time = "时间格式错误"
                        
                        comment_info = {
                            "index": i,
                            "author": comment['user_info'].get('nickname', '匿名用户'),
                            "content": comment.get('content', ''),
                            "create_time": create_time
                        }
                        
                        comments.append(comment_info)
                    
                    result_data = {
                        "success": True,
                        "message": f"成功获取到 {len(comments)} 条评论",
                        "comments": comments,
                        "total_count": len(comments),
                        "url": url
                    }
                    
                    logger.info(f"✅ 获取笔记评论成功: 共{len(comments)}条评论")
                    return json.dumps(result_data, ensure_ascii=False, indent=2)
                else:
                    # 检查是否是cookie问题
                    cookie_status = await self.xhs_api_adapter.check_cookie()
                    if "有效" in cookie_status:
                        result_data = {
                            "success": True,
                            "message": "该笔记暂无评论",
                            "comments": [],
                            "total_count": 0,
                            "url": url
                        }
                    else:
                        result_data = {
                            "success": False,
                            "message": "获取评论失败：登录状态无效",
                            "url": url,
                            "error_message": "需要重新登录小红书",
                            "suggestion": "请先运行登录工具：login_xiaohongshu()"
                        }
                    
                    logger.info(f"ℹ️ 获取笔记评论: 无评论或需要登录")
                    return json.dumps(result_data, ensure_ascii=False, indent=2)
                    
            except Exception as e:
                error_msg = f"获取笔记评论过程出错: {str(e)}"
                logger.error(f"❌ {error_msg}")
                return json.dumps({
                    "success": False,
                    "message": "获取笔记评论失败",
                    "url": url,
                    "error_message": error_msg,
                    "suggestion": "请检查URL格式和网络连接"
                }, ensure_ascii=False, indent=2)


    async def _execute_publish_task(self, task_id: str) -> None:
        """
        执行发布任务的后台逻辑
        
        Args:
            task_id: 任务ID
        """
        task = self.task_manager.get_task(task_id)
        if not task:
            logger.error(f"❌ 任务 {task_id} 不存在")
            return

        try:
            # 阶段0：快速验证登录状态（仅检查cookies存在性）
            self.task_manager.update_task(task_id, status="validating", progress=5, message="正在快速验证登录状态...")

            try:
                # 只检查cookies文件是否存在，避免重复的详细验证
                cookies_file = Path(self.config.cookies_file)
                if not cookies_file.exists():
                    self.task_manager.update_task(
                        task_id,
                        status="failed",
                        progress=0,
                        message="❌ 未找到登录cookies，请先登录小红书",
                        result={
                            "success": False,
                            "error_type": "auth_required",
                            "user_action_required": "需要登录小红书",
                            "suggested_command": "请对AI说：'登录小红书'"
                        }
                    )
                    logger.warning(f"⚠️ 任务 {task_id} 因缺少cookies而停止")
                    return

                # 快速验证通过，继续发布流程
                self.task_manager.update_task(task_id, status="initializing", progress=10, message="✅ 登录状态验证通过，正在初始化浏览器...")

            except Exception as e:
                logger.error(f"❌ 登录状态验证出错: {e}")
                self.task_manager.update_task(
                    task_id,
                    status="failed",
                    progress=0,
                    message=f"❌ 登录状态验证出错: {str(e)}",
                    result={
                        "success": False,
                        "error_type": "validation_error",
                        "error": str(e),
                        "suggested_action": "请重新登录小红书后重试"
                    }
                )
                return

            # 阶段1：初始化浏览器
            # 创建新的客户端实例，避免并发冲突
            client = XHSClient(self.config)

            # 阶段2：上传文件
            if task.note.images or task.note.videos:
                self.task_manager.update_task(task_id, status="uploading", progress=20, message="正在上传文件...")

                # 执行发布过程
                result = await client.publish_note(task.note)

                if result.success:
                    self.task_manager.update_task(
                        task_id,
                        status="completed",
                        progress=100,
                        message="发布成功！",
                        result=result.to_dict()
                    )
                else:
                    self.task_manager.update_task(
                        task_id,
                        status="failed",
                        progress=0,
                        message=f"发布失败: {result.message}",
                        result=result.to_dict()
                    )
            else:
                # 没有文件的快速发布
                self.task_manager.update_task(task_id, status="publishing", progress=60, message="正在发布笔记...")

                result = await client.publish_note(task.note)

                if result.success:
                    self.task_manager.update_task(
                        task_id,
                        status="completed",
                        progress=100,
                        message="发布成功！",
                        result=result.to_dict()
                    )
                else:
                    self.task_manager.update_task(
                        task_id,
                        status="failed",
                        progress=0,
                        message=f"发布失败: {result.message}",
                        result=result.to_dict()
                    )

        except Exception as e:
            error_msg = f"任务执行失败: {str(e)}"
            logger.error(f"❌ 任务 {task_id} 执行失败: {e}")
            self.task_manager.update_task(
                task_id,
                status="failed",
                progress=0,
                message=error_msg,
                result={"success": False, "message": error_msg}
            )
        finally:
            # 清理运行任务记录
            if task_id in self.task_manager.running_tasks:
                del self.task_manager.running_tasks[task_id]

    def _setup_resources(self) -> None:
        """设置MCP资源"""

        @self.mcp.resource("xhs://config")
        def get_xhs_config() -> str:
            """获取小红书MCP服务器配置信息"""
            config_info = self.config.to_dict()
            config_info["server_status"] = "running"
            return json.dumps(config_info, ensure_ascii=False, indent=2)

        @self.mcp.resource("xhs://help")
        def get_xhs_help() -> str:
            """获取小红书MCP服务器使用帮助"""
            help_text = """
# 小红书MCP服务器使用帮助

## 可用工具

### 1. test_connection
- 功能: 测试MCP连接
- 参数: 无

### 2. start_publish_task
- 功能: 启动异步发布任务（解决MCP超时问题）
- 参数:
  - title: 笔记标题
  - content: 笔记内容
  - tags: 标签（逗号分隔）
  - location: 位置信息
  - images: 图片路径（逗号分隔多个路径）
  - videos: 视频路径（逗号分隔多个路径）

### 3. check_task_status
- 功能: 检查发布任务状态
- 参数:
  - task_id: 任务ID

### 4. get_task_result
- 功能: 获取已完成任务的结果
- 参数:
  - task_id: 任务ID

### 5. close_browser
- 功能: 关闭浏览器

### 6. test_publish_params
- 功能: 测试发布参数解析（调试用）
- 参数:
  - title: 测试标题
  - content: 测试内容
  - image_path: 测试图片路径

## 可用资源

- xhs://config - 查看服务器配置
- xhs://help - 查看此帮助信息

## 环境变量

- CHROME_PATH: Chrome浏览器路径
- WEBDRIVER_CHROME_DRIVER: ChromeDriver路径
- json_path: Cookies文件路径
"""
            return help_text

    def _setup_prompts(self) -> None:
        """设置MCP提示词"""

        @self.mcp.prompt()
        def xiaohongshu_content_creation(topic: str, style: str = "生活分享") -> str:
            """
            小红书内容创作助手
            
            Args:
                topic: 内容主题
                style: 写作风格（生活分享、美妆护肤、美食探店、旅行攻略等）
            
            Returns:
                内容创作提示词
            """
            prompt = f"""
请帮我创作一篇关于"{topic}"的小红书笔记，风格为"{style}"。

要求：
1. 标题要吸引人，包含emoji和关键词
2. 内容要有价值，包含具体的建议或信息
3. 适当使用emoji让内容更生动
4. 添加相关标签（3-5个）
5. 字数控制在200-500字
6. 语言风格要贴近小红书用户习惯

请按以下格式输出：

【标题】
[在这里写标题]

【正文】
[在这里写正文内容]

【标签】
[在这里列出相关标签]

【发布建议】
[发布时间、配图建议等]
"""
            return prompt

    def _setup_signal_handlers(self) -> None:
        """设置信号处理器"""
        def signal_handler(signum, frame):
            logger.info("👋 收到停止信号，正在优雅关闭服务器...")
            # 清理资源
            try:
                # 停止数据采集调度器
                if self.scheduler_initialized and data_scheduler.is_running():
                    logger.info("🧹 停止数据采集调度器...")
                    asyncio.run(data_scheduler.stop())

                # 清理浏览器实例
                if hasattr(self.xhs_client, 'browser_manager') and self.xhs_client.browser_manager.is_initialized:
                    logger.info("🧹 清理残留的浏览器实例...")
                    self.xhs_client.browser_manager.close_driver()
            except Exception as cleanup_error:
                logger.warning(f"⚠️ 清理资源时出错: {cleanup_error}")

            logger.info("✅ 服务器已停止")
            os._exit(0)  # 强制退出避免ASGI错误

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

    def start_stdio(self) -> None:
        """启动stdio模式的MCP服务器（用于Claude Desktop）"""
        # 设置日志只输出到stderr，避免干扰stdio通信
        import sys
        from ..utils.logger import setup_logger, get_logger

        # 重新配置日志，只输出到stderr
        import logging
        root_logger = logging.getLogger()
        root_logger.handlers = []

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s'))
        root_logger.addHandler(stderr_handler)
        root_logger.setLevel(getattr(logging, self.config.log_level.upper()))

        logger.info("🚀 启动MCP服务器（stdio模式）...")

        # 验证配置
        validation = self.config.validate_config()
        if not validation["valid"]:
            logger.error("❌ 配置验证失败:")
            for issue in validation["issues"]:
                logger.error(f"   • {issue}")
            return

        logger.info("✅ 配置验证通过")

        # 工具已在__init__中注册
        logger.info(f"🎯 MCP工具列表:")
        for tool in ["test_connection", "smart_publish_note", "check_task_status",
                     "get_task_result", "login_xiaohongshu", "get_creator_data_analysis",
                     "parse_xiaohongshu_url", "search_notes", "get_note_content", "get_note_comments"]:
            logger.info(f"   • {tool}")

        # 初始化数据采集（如果启用）
        try:
            cookies = self.xhs_client.cookie_manager.load_cookies()
            if cookies and os.getenv('ENABLE_AUTO_COLLECTION', 'false').lower() == 'true':
                logger.info("📊 初始化数据采集功能...")
                # stdio模式下使用无头浏览器
                self.xhs_client.browser_manager.headless = True
                self.scheduler_initialized = self._initialize_data_collection()
            else:
                logger.info("ℹ️ 数据采集功能未启用")
        except Exception as e:
            logger.warning(f"⚠️ 数据采集功能初始化失败: {e}")

        # 使用stdio transport
        logger.info("🎯 MCP工具已注册，等待客户端连接...")
        self.mcp.run(transport="stdio")

    def start(self) -> None:
        """启动MCP服务器"""
        logger.info("🚀 启动小红书 MCP 服务器...")

        # 设置日志级别
        setup_logger(self.config.log_level)

        # 验证配置
        logger.info("🔍 验证配置...")
        validation = self.config.validate_config()

        if not validation["valid"]:
            logger.error("❌ 配置验证失败:")
            for issue in validation["issues"]:
                logger.error(f"   • {issue}")
            logger.error("💡 请检查 .env 文件配置")
            return

        logger.info("✅ 配置验证通过")

        # 设置信号处理
        self._setup_signal_handlers()

        # 获取本机IP地址
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("10.254.254.254", 80))
            local_ip = s.getsockname()[0]
            s.close()
            logger.info(f"📡 本机IP地址: {local_ip}")
        except Exception:
            local_ip = "未知"

        logger.info(f"🚀 启动SSE服务器 (端口{self.config.server_port})")
        logger.info("📡 可通过以下地址访问:")
        logger.info(f"   • http://localhost:{self.config.server_port}/sse (本机)")
        if local_ip != "未知":
            logger.info(f"   • http://{local_ip}:{self.config.server_port}/sse (内网)")
            logger.info(f"   • http://{local_ip}:{self.config.server_port}/sse (Docker容器访问)")
        
        logger.info("🔧 在n8n中配置:")
        if local_ip != "未知":
            logger.info(f"   MCP Server URL: http://{local_ip}:{self.config.server_port}/sse")
        else:
            logger.info(f"   MCP Server URL: http://localhost:{self.config.server_port}/sse")

        logger.info("🎯 MCP工具列表:")
        logger.info("   • test_connection - 测试MCP连接")
        logger.info("   • smart_publish_note - 发布小红书笔记（支持智能路径解析）")
        logger.info("   • check_task_status - 检查发布任务状态")
        logger.info("   • get_task_result - 获取已完成任务的结果")
        logger.info("   • login_xiaohongshu - 智能登录小红书")
        logger.info("   • get_creator_data_analysis - 获取创作者数据用于分析")
        logger.info("   • parse_xiaohongshu_url - 解析小红书URL，提取页面内容")
        logger.info("   • search_notes - 根据关键词搜索笔记")
        logger.info("   • get_note_content - 获取笔记内容（需要xsec_token）")
        logger.info("   • get_note_comments - 获取笔记评论（需要xsec_token）")

        logger.info("💡 新功能使用流程:")
        logger.info("   1. search_notes('关键词') -> 获取笔记列表")
        logger.info("   2. 从结果中获取带xsec_token的URL")
        logger.info("   3. get_note_content(url) -> 获取详细内容")
        logger.info("   4. get_note_comments(url) -> 获取评论列表")

        logger.info("🔧 按 Ctrl+C 停止服务器")
        logger.info("💡 终止时的ASGI错误信息是正常现象，可以忽略")

        # 初始化数据采集功能（无头模式）
        logger.info("📊 初始化数据采集功能（无头模式）...")
        try:
            asyncio.run(self._initialize_data_collection())
            if self.scheduler_initialized:
                logger.info("✅ 数据采集功能初始化完成（无头模式）")
            else:
                logger.info("ℹ️ 数据采集功能未启用或初始化失败")
        except Exception as e:
            logger.warning(f"⚠️ 数据采集功能初始化失败: {e}")

        try:
            # 使用FastMCP内置的run方法，禁用uvicorn的日志以避免干扰MCP通信
            import logging
            logging.getLogger("uvicorn").setLevel(logging.WARNING)
            logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

            self.mcp.run(transport="sse", port=self.config.server_port, host=self.config.server_host)

        except KeyboardInterrupt:
            logger.info("👋 收到停止信号，正在关闭服务器...")
        except Exception as e:
            logger.error(f"❌ 服务器启动失败: {e}")
            raise
        finally:
            # 清理资源
            try:
                # 停止数据采集调度器
                if self.scheduler_initialized and data_scheduler.is_running():
                    logger.info("🧹 停止数据采集调度器...")
                    asyncio.run(data_scheduler.stop())

                # 清理浏览器实例
                if hasattr(self.xhs_client, 'browser_manager') and self.xhs_client.browser_manager.is_initialized:
                    logger.info("🧹 清理残留的浏览器实例...")
                    self.xhs_client.browser_manager.close_driver()
            except Exception as cleanup_error:
                logger.warning(f"⚠️ 清理资源时出错: {cleanup_error}")

            logger.info("✅ 服务器已停止")


# 便捷函数
def create_mcp_server(config: XHSConfig) -> MCPServer:
    """
    创建MCP服务器的便捷函数
    
    Args:
        config: 配置管理器实例
        
    Returns:
        MCP服务器实例
    """
    return MCPServer(config)


def main():
    """主函数入口"""
    import sys
    from ..core.config import XHSConfig

    config = XHSConfig()
    server = MCPServer(config)

    # 检查是否通过stdio启动（Claude Desktop使用）
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        # 使用stdio模式
        server.start_stdio()
    else:
        # 默认使用SSE模式（用于其他客户端）
        server.start()


if __name__ == "__main__":
    main() 
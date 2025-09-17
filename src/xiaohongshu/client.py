"""
小红书客户端模块

负责与小红书平台的交互，包括笔记发布、搜索、用户信息获取等功能
"""

import asyncio
import time
from datetime import datetime
from typing import List, Dict, Any, Optional
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from ..core.config import XHSConfig
from ..core.browser import ChromeDriverManager
from ..core.exceptions import PublishError, NetworkError, handle_exception
from ..auth.cookie_manager import CookieManager
from ..utils.text_utils import clean_text_for_browser, clean_text_for_xiaohongshu, truncate_text
from ..utils.logger import get_logger
from .models import XHSNote, XHSSearchResult, XHSUser, XHSPublishResult, XHSUrlParseResult
from .components.content_filler import XHSContentFiller
from .constants import get_content_editor_selectors
from .constants import (XHSConfig)

logger = get_logger(__name__)


class XHSClient:
    """小红书客户端类"""
    
    def __init__(self, config: XHSConfig):
        """
        初始化小红书客户端
        
        Args:
            config: 配置管理器实例
        """
        self.config = config
        self.browser_manager = ChromeDriverManager(config)
        self.cookie_manager = CookieManager(config)
        self.session = requests.Session()
        self.content_filler = None  # 延迟初始化，需要browser_manager运行时才能创建
        self._setup_session()
    
    def _setup_session(self) -> None:
        """设置requests会话"""
        try:
            cookies = self.cookie_manager.load_cookies()
            if cookies:
                for cookie in cookies:
                    self.session.cookies.set(
                        name=cookie['name'],
                        value=cookie['value'],
                        domain=cookie['domain']
                    )
                logger.debug(f"已设置 {len(cookies)} 个cookies到会话")
        except Exception as e:
            logger.warning(f"设置会话cookies失败: {e}")
    
    @handle_exception
    async def publish_note(self, note: XHSNote) -> XHSPublishResult:
        """
        发布小红书笔记
        
        Args:
            note: 笔记对象
            
        Returns:
            发布结果
            
        Raises:
            PublishError: 当发布过程出错时
        """
        logger.info(f"📝 开始发布小红书笔记: {note.title}")
        
        try:
            # 创建浏览器驱动
            driver = self.browser_manager.create_driver()
            
            # 导航到创作者中心
            self.browser_manager.navigate_to_creator_center()
            
            # 加载cookies
            cookies = self.cookie_manager.load_cookies()
            cookie_result = self.browser_manager.load_cookies(cookies)
            
            logger.info(f"🍪 Cookies加载结果: {cookie_result}")
            
            # 访问发布页面
            return await self._publish_note_process(note)
            
        except Exception as e:
            if isinstance(e, PublishError):
                raise
            else:
                raise PublishError(f"发布笔记过程出错: {str(e)}", publish_step="初始化") from e
        finally:
            # 确保浏览器被关闭
            self.browser_manager.close_driver()
    
    async def _publish_note_process(self, note: XHSNote) -> XHSPublishResult:
        """执行发布笔记的具体流程"""
        driver = self.browser_manager.driver
        
        try:
            logger.info("🌐 直接访问小红书发布页面...")
            driver.get("https://creator.xiaohongshu.com/publish/publish?from=menu")
            await asyncio.sleep(5)  # 等待页面基本加载
            
            if "publish" not in driver.current_url:
                raise PublishError("无法访问发布页面，可能需要重新登录", publish_step="页面访问")
            
            logger.info("⏳ 等待页面元素完全渲染...")
            await asyncio.sleep(3)  # 等待页面元素完全渲染
            
            # 根据内容类型切换发布模式
            await self._switch_publish_mode(note)
            
            # 处理文件上传（图片/视频）
            await self._handle_file_upload(note)
            
            # 填写笔记内容
            await self._fill_note_content(note)

            if note.is_commercial:
                logger.info("🛒 开始勾选商业商品...")
                success = await self._fill_commercial_goods()
                if not success:
                    logger.warning("⚠️ 商品勾选失败，但继续发布流程")
            
            # 发布笔记
            return await self._submit_note(note)
            
        except Exception as e:
            self.browser_manager.take_screenshot("publish_error_screenshot.png")
            if isinstance(e, PublishError):
                raise
            else:
                raise PublishError(f"发布流程执行失败: {str(e)}", publish_step="流程执行") from e

    async def _fill_commercial_goods(self):
        """
        执行商品勾选

        Returns:
            勾选是否成功
        """
        driver = self.browser_manager.driver
        wait = WebDriverWait(driver, XHSConfig.DEFAULT_WAIT_TIME)
        logger.debug("🔍 查找下拉框")

        dropdown = driver.find_element(By.CSS_SELECTOR, 'div.description-collapse')
        if not dropdown:
            logger.error("❌ 未找到下拉框，无法添加商品")
            return False
        dropdown.click()
        logger.info("✅ 找到下拉框")

        await asyncio.sleep(3)
        # 2 找到button class multi-good-select-empty-btn并点击
        logger.debug("🔍 查找添加商品按钮")
        add_button = driver.find_element(By.CSS_SELECTOR, 'div.multi-good-select-empty-btn')
        if not add_button:
            logger.error("❌ 未找到添加商品按钮，无法添加商品")
            return False
        logger.info("✅ 找到添加商品按钮")
        add_button.click()
        await asyncio.sleep(3)


        # 查找goods-list-normal下面所有的<input type="checkbox">并点击
        logger.info("🔍 查找商品列表中的复选框")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'span.d-checkbox-simulator')
        if not checkboxes:
            logger.error("❌ 未找到商品复选框，无法添加商品")
            return False
        logger.info(f"✅ 找到 {len(checkboxes)} 个商品复选框")
        # 点击所有复选框
        for checkbox in checkboxes:
            checkbox.click()
            await asyncio.sleep(1)

        # 点击右下角的完成按钮d-button-content
        logger.info("🔍 查找完成按钮")
        complete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.d-button-with-content')

        if not complete_buttons:
            logger.error("❌ 未找到完成按钮，无法添加商品")
            return False
        # filter with inner "保存"
        complete_buttons = [btn for btn in complete_buttons if "保存" in btn.text]
        if not complete_buttons:
            logger.error("❌ 未找到包含'保存'的完成按钮，无法添加商品")
            return False
        complete_button = complete_buttons[0]
        logger.info("✅ 找到完成按钮")
        complete_button.click()
        await asyncio.sleep(1)
        return True


    async def _switch_publish_mode(self, note: XHSNote) -> None:
        """根据笔记内容类型切换发布模式（图文/视频）"""
        try:
            driver = self.browser_manager.driver
            
            # 判断内容类型
            has_images = note.images and len(note.images) > 0
            has_videos = note.videos and len(note.videos) > 0
            
            if has_images:
                logger.info("🔄 切换到图文发布模式...")
                # 查找"上传图文"选项卡
                try:
                    # 查找所有creator-tab元素
                    tabs = driver.find_elements(By.CSS_SELECTOR, ".creator-tab")
                    image_tab = None
                    
                    for tab in tabs:
                        if tab.is_displayed() and "上传图文" in tab.text:
                            # 确保元素在可见区域内（不是负坐标）
                            rect = tab.rect
                            if rect['x'] > 0 and rect['y'] > 0:
                                image_tab = tab
                                break
                    
                    if image_tab:
                        image_tab.click()
                        logger.info("✅ 已切换到图文发布模式")
                        await asyncio.sleep(2)  # 等待界面切换完成
                    else:
                        logger.warning("⚠️ 未找到图文发布选项卡，可能已经在图文模式")
                        
                except Exception as e:
                    logger.warning(f"⚠️ 切换图文模式时出错: {e}，继续执行...")
                    
            elif has_videos:
                logger.info("🔄 切换到视频发布模式...")
                # 页面默认就是视频模式，检查是否需要切换
                try:
                    tabs = driver.find_elements(By.CSS_SELECTOR, ".creator-tab")
                    video_tab = None
                    
                    for tab in tabs:
                        if tab.is_displayed() and "上传视频" in tab.text:
                            rect = tab.rect
                            if rect['x'] > 0 and rect['y'] > 0:
                                video_tab = tab
                                break
                    
                    if video_tab and "active" not in video_tab.get_attribute("class"):
                        video_tab.click()
                        logger.info("✅ 已切换到视频发布模式")
                        await asyncio.sleep(2)
                    else:
                        logger.info("✅ 已在视频发布模式")
                        
                except Exception as e:
                    logger.warning(f"⚠️ 切换视频模式时出错: {e}，继续执行...")
                    
        except Exception as e:
            logger.warning(f"⚠️ 模式切换过程出错: {e}，继续执行...")

    async def _handle_file_upload(self, note: XHSNote) -> None:
        """统一处理文件上传（图片/视频）"""
        try:
            driver = self.browser_manager.driver
            wait = WebDriverWait(driver, 30)
            
            # 合并图片和视频文件
            files_to_upload = []
            has_video = False
            
            if note.images:
                files_to_upload.extend(note.images)
                logger.info(f"📸 准备上传 {len(note.images)} 张图片...")
            if note.videos:
                files_to_upload.extend(note.videos)
                has_video = True
                logger.info(f"🎬 准备上传 {len(note.videos)} 个视频...")
            
            if files_to_upload:
                # 尝试多个可能的选择器查找上传元素
                upload_input = None
                upload_selectors = [
                    ".upload-input",
                    "input[type='file']",
                    "[class*='upload'][type='file']",
                    ".file-input",
                    ".uploader-input",
                    "[accept*='image']",
                    "[accept*='video']"
                ]
                
                logger.info("🔍 查找上传元素...")
                for selector in upload_selectors:
                    try:
                        elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        for element in elements:
                            if element.is_displayed():
                                upload_input = element
                                logger.info(f"✅ 找到可见的上传元素: {selector}")
                                break
                        if upload_input:
                            break
                    except Exception:
                        continue
                
                # 如果还是没找到，用xpath方式
                if not upload_input:
                    try:
                        upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
                        logger.info("✅ 通过XPath找到上传元素")
                    except Exception:
                        logger.error("❌ 无法找到任何文件上传元素")
                        # 继续执行，可能页面结构已改变
                        return
                
                # 发送文件路径
                upload_input.send_keys('\n'.join(files_to_upload))
                logger.info("✅ 文件上传指令已发送")
                
                # 给时间让上传开始
                await asyncio.sleep(3)
                
                # 如果有视频，等待上传完成
                if has_video:
                    await self._wait_for_video_upload_complete()
                else:
                    # 图片上传给少量时间
                    await asyncio.sleep(2)
                    
        except Exception as e:
            logger.warning(f"⚠️ 处理文件上传时出错: {e}")
            # 不抛出异常，继续后续流程
            
    async def _wait_for_video_upload_complete(self) -> None:
        """等待视频上传完成"""
        try:
            driver = self.browser_manager.driver
            
            logger.info("⏳ 等待视频上传完成...")
            
            # 等待上传成功标识出现 - 使用轮询方式
            success_selectors = [
                "//div[contains(text(), '上传成功')]",
                "//span[contains(text(), '上传成功')]", 
                "//*[contains(text(), '上传成功')]",
                "//div[contains(@class, 'success')]"
            ]
            
            max_wait_time = 120  # 最大等待2分钟，避免MCP超时
            check_interval = 2   # 每2秒检查一次
            elapsed_time = 0
            success_found = False
            
            while elapsed_time < max_wait_time and not success_found:
                # 检查所有可能的成功标识
                for selector in success_selectors:
                    try:
                        elements = driver.find_elements(By.XPATH, selector)
                        for element in elements:
                            if element.is_displayed() and "上传成功" in element.text:
                                logger.info("✅ 视频上传完成！")
                                success_found = True
                                break
                        if success_found:
                            break
                    except Exception:
                        continue
                
                if not success_found:
                    logger.debug(f"⏳ 继续等待上传完成... ({elapsed_time}s/{max_wait_time}s)")
                    await asyncio.sleep(check_interval)
                    elapsed_time += check_interval
            
            if not success_found:
                logger.warning(f"⚠️ 等待{max_wait_time}秒后未检测到上传成功标识，继续流程")
            
            # 尝试获取视频信息
            try:
                video_info_elements = driver.find_elements(
                    By.XPATH, "//div[contains(text(), '视频大小') or contains(text(), '视频时长')]"
                )
                for info in video_info_elements:
                    if info.is_displayed():
                        logger.info(f"📹 {info.text}")
            except:
                pass  # 视频信息获取失败不影响主流程
                
        except Exception as e:
            logger.warning(f"⚠️ 等待视频上传完成时出错: {e}")
            # 即使等待失败，也继续后续流程
    
    async def _fill_note_content(self, note: XHSNote) -> None:
        """填写笔记内容"""
        driver = self.browser_manager.driver
        wait = WebDriverWait(driver, 15)
        
        # 初始化content_filler（如果还没初始化）
        if not self.content_filler:
            self.content_filler = XHSContentFiller(self.browser_manager)
        
        await asyncio.sleep(2)  # 等待上传完成
        
        # 填写标题
        try:
            logger.info("✏️ 填写标题...")
            title = clean_text_for_browser(truncate_text(note.title, 20))
            
            # 尝试多个标题选择器
            title_selectors = [
                ".d-text",
                "[placeholder*='标题']",
                "[placeholder*='title']",
                "input[type='text']",
                ".title-input",
                ".input"
            ]
            
            title_input = None
            for selector in title_selectors:
                try:
                    title_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    if title_input.is_displayed():
                        logger.info(f"✅ 找到标题输入框: {selector}")
                        break
                except:
                    continue
            
            if not title_input:
                raise PublishError("无法找到标题输入框", publish_step="查找标题输入框")
            
            title_input.clear()
            title_input.send_keys(title)
            logger.info(f"✅ 标题已填写: {title}")
            
        except Exception as e:
            raise PublishError(f"填写标题失败: {str(e)}", publish_step="填写标题") from e
        
        # 填写内容
        try:
            logger.info("📝 填写内容...")
            
            # 使用更新后的内容选择器（基于真实DOM结构）
            content_selectors = get_content_editor_selectors()
            
            content_input = None
            for selector in content_selectors:
                try:
                    content_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    if content_input.is_displayed():
                        logger.info(f"✅ 找到内容输入框: {selector}")
                        break
                except:
                    continue
            
            if not content_input:
                raise PublishError("无法找到内容输入框", publish_step="查找内容输入框")
            
            content_input.clear()
            
            # 处理内容，支持换行
            from selenium.webdriver.common.keys import Keys
            cleaned_content = clean_text_for_xiaohongshu(note.content)
            
            # 分段输入，正确处理换行
            lines = cleaned_content.split('\n')
            for i, line in enumerate(lines):
                content_input.send_keys(line)
                if i < len(lines) - 1:
                    content_input.send_keys(Keys.ENTER)
                await asyncio.sleep(0.1)  # 短暂等待
            
            logger.info("✅ 内容已填写")
            
        except Exception as e:
            raise PublishError(f"填写内容失败: {str(e)}", publish_step="填写内容") from e
        
        # 填写话题
        if note.topics and len(note.topics) > 0:
            try:
                logger.info(f"🏷️ 开始填写话题: {note.topics}")
                success = await self.content_filler.fill_topics(note.topics)
                if success:
                    logger.info("✅ 话题填写成功")
                else:
                    logger.warning("⚠️ 话题填写失败，但继续发布流程")
            except Exception as e:
                logger.warning(f"⚠️ 话题填写出错: {e}，继续发布流程")
        else:
            logger.info("📋 没有话题需要填写")
        
        await asyncio.sleep(2)
    
    async def _submit_note(self, note: XHSNote) -> XHSPublishResult:
        """提交发布笔记"""
        driver = self.browser_manager.driver
        
        try:
            logger.info("🚀 点击发布按钮...")
            
            # 尝试多个发布按钮选择器
            publish_selectors = [
                ".publishBtn",
                "[class*='publish']",
                "button[type='submit']",
                "//button[contains(text(), '发布')]",
                "//button[contains(text(), '提交')]"
            ]
            
            submit_btn = None
            for selector in publish_selectors:
                try:
                    if selector.startswith("//"):
                        submit_btn = driver.find_element(By.XPATH, selector)
                    else:
                        submit_btn = driver.find_element(By.CSS_SELECTOR, selector)
                    
                    if submit_btn.is_displayed() and submit_btn.is_enabled():
                        logger.info(f"✅ 找到发布按钮: {selector}")
                        break
                except:
                    continue
            
            if not submit_btn:
                raise PublishError("无法找到发布按钮", publish_step="查找发布按钮")

            logger.info("✅ 发布前准备120s")
            await asyncio.sleep(120)


            submit_btn.click()
            logger.info("✅ 发布按钮已点击")
            await asyncio.sleep(3)
            
            current_url = driver.current_url
            logger.info(f"📍 发布后页面URL: {current_url}")
            
            return XHSPublishResult(
                success=True,
                message=f"笔记发布成功！标题: {note.title}",
                note_title=note.title,
                final_url=current_url
            )
            
        except Exception as e:
            raise PublishError(f"点击发布按钮失败: {str(e)}", publish_step="提交发布") from e

    @handle_exception
    async def upload_files_only(self, note: XHSNote) -> dict:
        """
        仅上传文件，不填写内容和发布
        用于分阶段操作，避免MCP超时
        
        Args:
            note: 笔记对象
            
        Returns:
            上传结果字典
        """
        logger.info(f"📤 开始仅上传文件阶段: {note.title}")
        
        try:
            # 初始化浏览器
            await self._init_browser()
            
            # 访问发布页面
            await self._navigate_to_publish_page()
            
            # 上传文件
            await self._handle_file_upload(note)
            
            # 保持浏览器打开，保存状态供后续使用
            # 不关闭浏览器，让下一个阶段继续使用
            
            return {
                "success": True,
                "message": f"文件上传完成！标题: {note.title}，请调用发布工具完成后续步骤。",
                "note_title": note.title
            }
            
        except Exception as e:
            logger.error(f"❌ 上传文件阶段失败: {e}")
            # 出错时关闭浏览器
            if hasattr(self, 'browser_manager') and self.browser_manager:
                await self.browser_manager.close()
            
            return {
                "success": False,
                "message": f"上传文件失败: {str(e)}",
                "note_title": note.title
            }
    
    @handle_exception
    async def fill_and_publish_existing(self) -> XHSPublishResult:
        """
        填写内容并发布已上传的笔记
        需要先调用upload_files_only
        
        Returns:
            发布结果
        """
        logger.info("📝 开始填写内容并发布阶段")
        
        try:
            # 检查浏览器是否还活着
            if not hasattr(self, 'browser_manager') or not self.browser_manager or not self.browser_manager.driver:
                raise PublishError("浏览器会话已失效，请重新上传文件", publish_step="检查浏览器状态")
            
            # 从当前页面获取之前保存的笔记信息（简化处理）
            # 实际项目中可以通过会话存储等方式传递
            dummy_note = XHSNote(
                title="",  # 将在页面中填写
                content="", # 将在页面中填写
                images=[],
                videos=[]
            )
            
            # 填写内容
            await self._fill_note_content_existing()
            
            # 提交发布
            result = await self._submit_note_existing()
            
            # 关闭浏览器
            await self.browser_manager.close()
            
            return result
            
        except Exception as e:
            logger.error(f"❌ 填写发布阶段失败: {e}")
            # 出错时关闭浏览器
            if hasattr(self, 'browser_manager') and self.browser_manager:
                await self.browser_manager.close()
            
            return XHSPublishResult(
                success=False,
                message=f"填写发布失败: {str(e)}",
                note_title="",
                final_url=""
            )
    
    async def _fill_note_content_existing(self) -> None:
        """填写已上传文件的笔记内容（从用户输入获取）"""
        driver = self.browser_manager.driver
        wait = WebDriverWait(driver, 15)
        
        await asyncio.sleep(2)  # 等待页面稳定
        
        # 由于这是分阶段操作，内容需要从页面现有的输入框获取或提示用户
        # 这里先做基础检查，确保页面状态正常
        try:
            # 检查标题输入框是否存在
            title_selectors = [
                ".d-text",
                "[placeholder*='标题']",
                "[placeholder*='title']",
                "input[type='text']",
                ".title-input",
                ".input"
            ]
            
            title_input = None
            for selector in title_selectors:
                try:
                    title_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    if title_input.is_displayed():
                        logger.info(f"✅ 确认标题输入框可用: {selector}")
                        break
                except:
                    continue
            
            if not title_input:
                raise PublishError("无法找到标题输入框", publish_step="检查标题输入框")
            
            # 检查内容输入框是否存在（使用更新后的选择器）
            content_selectors = get_content_editor_selectors()
            
            content_input = None
            for selector in content_selectors:
                try:
                    content_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                    if content_input.is_displayed():
                        logger.info(f"✅ 确认内容输入框可用: {selector}")
                        break
                except:
                    continue
            
            if not content_input:
                raise PublishError("无法找到内容输入框", publish_step="检查内容输入框")
            
            logger.info("✅ 页面状态正常，标题和内容输入框都可用")
            
        except Exception as e:
            raise PublishError(f"页面状态检查失败: {str(e)}", publish_step="检查页面状态") from e
    
    async def _submit_note_existing(self) -> XHSPublishResult:
        """提交发布已准备好的笔记"""
        driver = self.browser_manager.driver
        
        try:
            logger.info("🚀 检查发布按钮状态...")
            
            # 尝试多个发布按钮选择器
            publish_selectors = [
                ".publishBtn",
                "[class*='publish']",
                "button[type='submit']",
                "//button[contains(text(), '发布')]",
                "//button[contains(text(), '提交')]"
            ]
            
            submit_btn = None
            for selector in publish_selectors:
                try:
                    if selector.startswith("//"):
                        submit_btn = driver.find_element(By.XPATH, selector)
                    else:
                        submit_btn = driver.find_element(By.CSS_SELECTOR, selector)
                    
                    if submit_btn.is_displayed() and submit_btn.is_enabled():
                        logger.info(f"✅ 确认发布按钮可用: {selector}")
                        break
                except:
                    continue
            
            if not submit_btn:
                raise PublishError("无法找到可用的发布按钮", publish_step="检查发布按钮")
            
            # 点击发布
            submit_btn.click()
            logger.info("✅ 发布按钮已点击")
            await asyncio.sleep(3)
            
            current_url = driver.current_url
            logger.info(f"📍 发布后页面URL: {current_url}")
            
            return XHSPublishResult(
                success=True,
                message="笔记发布成功！",
                note_title="已发布",
                final_url=current_url
            )
            
        except Exception as e:
            raise PublishError(f"提交发布失败: {str(e)}", publish_step="提交发布") from e


    # ==================== 数据采集功能 ====================
    
    @handle_exception
    async def collect_creator_data(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        采集创作者数据中心的全部核心数据
        
        Args:
            date: 采集日期，默认当天
            
        Returns:
            结构化数据字典，包含账号概览、内容分析、粉丝数据
        """
        from .data_collector import collect_dashboard_data, collect_content_analysis_data, collect_fans_data
        
        logger.info("📊 开始采集创作者数据中心数据...")
        
        try:
            # 创建浏览器驱动
            driver = self.browser_manager.create_driver()
            
            # 加载cookies
            cookies = self.cookie_manager.load_cookies()
            cookie_result = self.browser_manager.load_cookies(cookies)
            logger.info(f"🍪 Cookies加载结果: {cookie_result}")
            
            # 采集结果
            result = {
                "success": True,
                "collect_time": datetime.now().isoformat(),
                "date": date or datetime.now().strftime("%Y-%m-%d"),
                "data": {}
            }
            
            try:
                # 采集账号概览数据
                logger.info("🏠 开始采集账号概览数据...")
                dashboard_data = collect_dashboard_data(driver, date)
                result["data"]["dashboard"] = dashboard_data
                
                # 等待间隔，遵守采集规范
                await asyncio.sleep(3)
                
                # 采集内容分析数据
                logger.info("📊 开始采集内容分析数据...")
                content_data = collect_content_analysis_data(driver, date)
                result["data"]["content_analysis"] = content_data
                
                # 等待间隔
                await asyncio.sleep(3)
                
                # 采集粉丝数据
                logger.info("👥 开始采集粉丝数据...")
                fans_data = collect_fans_data(driver, date)
                result["data"]["fans"] = fans_data
                
                logger.info("✅ 创作者数据采集完成")
                
            except Exception as e:
                logger.error(f"❌ 数据采集过程出错: {e}")
                result["success"] = False
                result["error"] = str(e)
                
        except Exception as e:
            logger.error(f"❌ 初始化数据采集环境失败: {e}")
            return {"success": False, "error": str(e)}
        finally:
            # 确保浏览器被关闭
            self.browser_manager.close_driver()
        
        return result
    
    @handle_exception
    async def collect_dashboard_data(self, date: Optional[str] = None, save_data: bool = True) -> Dict[str, Any]:
        """
        采集账号概览数据
        
        Args:
            date: 采集日期，默认当天
            save_data: 是否保存数据到存储
            
        Returns:
            账号概览数据字典
        """
        from .data_collector.dashboard import collect_dashboard_data
        
        logger.info("🏠 开始采集账号概览数据...")
        
        try:
            driver = self.browser_manager.create_driver()
            cookies = self.cookie_manager.load_cookies()
            self.browser_manager.load_cookies(cookies)
            
            result = await collect_dashboard_data(driver, date, save_data)
            
        except Exception as e:
            logger.error(f"❌ 采集账号概览数据失败: {e}")
            return {"success": False, "error": str(e)}
        finally:
            self.browser_manager.close_driver()
        
        return result
    
    @handle_exception
    async def collect_content_analysis_data(self, date: Optional[str] = None, 
                                               limit: int = 50, save_data: bool = True) -> Dict[str, Any]:
        """
        采集内容分析数据
        
        Args:
            date: 采集日期，默认当天
            limit: 最大采集笔记数量
            save_data: 是否保存数据到存储
            
        Returns:
            内容分析数据字典
        """
        from .data_collector.content_analysis import collect_content_analysis_data
        
        logger.info("📊 开始采集内容分析数据...")
        
        try:
            driver = self.browser_manager.create_driver()
            cookies = self.cookie_manager.load_cookies()
            self.browser_manager.load_cookies(cookies)
            
            result = await collect_content_analysis_data(driver, date, limit, save_data)
            
        except Exception as e:
            logger.error(f"❌ 采集内容分析数据失败: {e}")
            return {"success": False, "error": str(e)}
        finally:
            self.browser_manager.close_driver()
        
        return result
    
    @handle_exception
    async def collect_fans_data(self, date: Optional[str] = None, save_data: bool = True) -> Dict[str, Any]:
        """
        采集粉丝数据
        
        Args:
            date: 采集日期，默认当天
            save_data: 是否保存数据到存储
            
        Returns:
            粉丝数据字典
        """
        from .data_collector.fans import collect_fans_data
        
        logger.info("👥 开始采集粉丝数据...")
        
        try:
            driver = self.browser_manager.create_driver()
            cookies = self.cookie_manager.load_cookies()
            self.browser_manager.load_cookies(cookies)
            
            result = await collect_fans_data(driver, date, save_data)
            
        except Exception as e:
            logger.error(f"❌ 采集粉丝数据失败: {e}")
            return {"success": False, "error": str(e)}
        finally:
            self.browser_manager.close_driver()
        
        return result
    
    @handle_exception
    async def collect_note_detail_data(self, note_title: str) -> Dict[str, Any]:
        """
        采集单篇笔记的详细数据
        
        Args:
            note_title: 笔记标题（用于定位）
            
        Returns:
            笔记详细数据字典
        """
        from .data_collector.content_analysis import collect_note_detail_data
        
        logger.info(f"📋 开始采集笔记详细数据: {note_title}")
        
        try:
            driver = self.browser_manager.create_driver()
            cookies = self.cookie_manager.load_cookies()
            self.browser_manager.load_cookies(cookies)
            
            # 先访问内容分析页面
            driver.get("https://creator.xiaohongshu.com/statistics/data-analysis")
            await asyncio.sleep(3)
            
            result = collect_note_detail_data(driver, note_title)
            
        except Exception as e:
            logger.error(f"❌ 采集笔记详细数据失败: {e}")
            return {"success": False, "error": str(e)}
        finally:
            self.browser_manager.close_driver()
        
        return result

    @handle_exception
    async def parse_xiaohongshu_url(self, url: str, include_raw_html: bool = False) -> XHSUrlParseResult:
        """
        解析小红书URL，提取页面内容信息
        
        Args:
            url: 小红书页面URL
            include_raw_html: 是否在结果中包含原始HTML（用于调试）
            
        Returns:
            URL解析结果
            
        Raises:
            NetworkError: 当网络访问出错时
        """
        logger.info(f"🔍 开始解析小红书URL: {url}")
        
        try:
            # 创建浏览器驱动
            driver = self.browser_manager.create_driver()
            
            # 加载cookies以获得更好的访问权限
            cookies = self.cookie_manager.load_cookies()
            if cookies:
                # 先访问小红书主页设置cookies
                driver.get("https://www.xiaohongshu.com")
                await asyncio.sleep(2)
                
                cookie_result = self.browser_manager.load_cookies(cookies)
                logger.info(f"🍪 Cookies加载结果: {cookie_result}")
            
            # 访问目标URL
            logger.info(f"🌐 访问目标URL: {url}")
            driver.get(url)
            await asyncio.sleep(5)  # 等待页面加载
            
            # 获取页面HTML
            page_html = driver.page_source
            current_url = driver.current_url
            
            logger.info(f"📍 实际访问的URL: {current_url}")
            
            # 解析页面内容
            result = await self._parse_page_content(url, page_html, current_url)
            
            # 可选：包含原始HTML
            if include_raw_html:
                result.raw_html = page_html
            
            return result
            
        except Exception as e:
            logger.error(f"❌ 解析URL失败: {e}")
            return XHSUrlParseResult(
                success=False,
                url=url,
                error_message=f"解析URL失败: {str(e)}"
            )
        finally:
            # 确保浏览器被关闭
            self.browser_manager.close_driver()

    async def _parse_page_content(self, original_url: str, html: str, current_url: str) -> XHSUrlParseResult:
        """
        解析页面HTML内容，提取结构化数据
        
        Args:
            original_url: 原始请求URL
            html: 页面HTML内容
            current_url: 实际访问的URL
            
        Returns:
            解析结果
        """
        try:
            from bs4 import BeautifulSoup
            import re
            import json
            
            soup = BeautifulSoup(html, 'html.parser')
            
            # 判断页面类型
            page_type = self._detect_page_type(current_url, soup)
            logger.info(f"🔍 检测到页面类型: {page_type}")
            
            result = XHSUrlParseResult(
                success=True,
                url=original_url,
                page_type=page_type
            )
            
            if page_type == "note":
                # 解析笔记页面
                await self._parse_note_page(soup, result)
            elif page_type == "user":
                # 解析用户页面
                await self._parse_user_page(soup, result)
            else:
                # 通用解析
                await self._parse_generic_page(soup, result)
            
            return result
            
        except ImportError:
            logger.error("❌ 缺少BeautifulSoup库，请安装: pip install beautifulsoup4")
            return XHSUrlParseResult(
                success=False,
                url=original_url,
                error_message="缺少BeautifulSoup库，请安装: pip install beautifulsoup4"
            )
        except Exception as e:
            logger.error(f"❌ 解析页面内容失败: {e}")
            return XHSUrlParseResult(
                success=False,
                url=original_url,
                error_message=f"解析页面内容失败: {str(e)}"
            )

    def _detect_page_type(self, url: str, soup) -> str:
        """
        检测页面类型
        
        Args:
            url: 页面URL
            soup: BeautifulSoup对象
            
        Returns:
            页面类型: "note", "user", "topic", "unknown"
        """
        try:
            # 通过URL路径判断
            if "/explore/" in url or "/discovery/" in url:
                return "note"
            elif "/user/" in url or "/profile/" in url:
                return "user"
            elif "/topic/" in url:
                return "topic"
            
            # 通过页面元素判断
            if soup.find(attrs={"data-testid": "note-detail"}) or soup.find(class_=re.compile("note")):
                return "note"
            elif soup.find(attrs={"data-testid": "user-profile"}) or soup.find(class_=re.compile("profile")):
                return "user"
            
            return "unknown"
            
        except Exception as e:
            logger.warning(f"⚠️ 检测页面类型失败: {e}")
            return "unknown"

    async def _parse_note_page(self, soup, result: XHSUrlParseResult):
        """
        解析笔记页面内容
        
        Args:
            soup: BeautifulSoup对象
            result: 解析结果对象（会被修改）
        """
        try:
            import re
            import json
            
            # 尝试从JSON-LD中提取信息
            json_scripts = soup.find_all('script', type='application/ld+json')
            for script in json_scripts:
                try:
                    data = json.loads(script.string)
                    if isinstance(data, dict) and data.get('@type') == 'Article':
                        result.title = data.get('headline')
                        result.content = data.get('description') or data.get('text')
                        result.author = data.get('author', {}).get('name') if isinstance(data.get('author'), dict) else None
                        result.publish_time = data.get('datePublished')
                        break
                except:
                    continue
            
            # 尝试从页面元素中提取标题
            if not result.title:
                title_selectors = [
                    '[data-testid="note-title"]',
                    '.note-title',
                    'h1',
                    '.title',
                    '[class*="title"]'
                ]
                for selector in title_selectors:
                    title_elem = soup.select_one(selector)
                    if title_elem and title_elem.get_text(strip=True):
                        result.title = title_elem.get_text(strip=True)
                        break
            
            # 尝试从页面元素中提取内容
            if not result.content:
                content_selectors = [
                    '[data-testid="note-content"]',
                    '.note-content',
                    '.content',
                    '[class*="content"]',
                    'p'
                ]
                for selector in content_selectors:
                    content_elem = soup.select_one(selector)
                    if content_elem and content_elem.get_text(strip=True):
                        result.content = content_elem.get_text(strip=True)
                        break
            
            # 提取作者信息
            if not result.author:
                author_selectors = [
                    '[data-testid="author-name"]',
                    '.author-name',
                    '.username',
                    '[class*="author"]'
                ]
                for selector in author_selectors:
                    author_elem = soup.select_one(selector)
                    if author_elem and author_elem.get_text(strip=True):
                        result.author = author_elem.get_text(strip=True)
                        break
            
            # 提取图片
            img_elements = soup.find_all('img')
            images = []
            for img in img_elements:
                src = img.get('src') or img.get('data-src')
                if src and ('xiaohongshu' in src or 'xhscdn' in src):
                    if src.startswith('//'):
                        src = 'https:' + src
                    elif src.startswith('/'):
                        src = 'https://www.xiaohongshu.com' + src
                    images.append(src)
            
            if images:
                result.images = images[:9]  # 最多保存9张图片
            
            # 提取标签/话题
            tag_selectors = [
                '[data-testid="tag"]',
                '.tag',
                '.topic',
                '[class*="tag"]',
                '[class*="topic"]'
            ]
            tags = []
            for selector in tag_selectors:
                tag_elements = soup.select(selector)
                for tag_elem in tag_elements:
                    tag_text = tag_elem.get_text(strip=True)
                    if tag_text and tag_text.startswith('#'):
                        tags.append(tag_text)
            
            if tags:
                result.tags = list(set(tags))  # 去重
            
            # 提取互动数据（点赞、评论、分享）
            self._extract_interaction_data(soup, result)
            
            logger.info(f"✅ 笔记页面解析完成 - 标题: {result.title}")
            
        except Exception as e:
            logger.warning(f"⚠️ 解析笔记页面时出错: {e}")

    async def _parse_user_page(self, soup, result: XHSUrlParseResult):
        """
        解析用户页面内容
        
        Args:
            soup: BeautifulSoup对象
            result: 解析结果对象（会被修改）
        """
        try:
            # 提取用户名
            username_selectors = [
                '[data-testid="username"]',
                '.username',
                '.nickname',
                'h1',
                '[class*="name"]'
            ]
            for selector in username_selectors:
                username_elem = soup.select_one(selector)
                if username_elem and username_elem.get_text(strip=True):
                    result.author = username_elem.get_text(strip=True)
                    result.title = f"{result.author}的主页"
                    break
            
            # 提取简介
            bio_selectors = [
                '[data-testid="bio"]',
                '.bio',
                '.description',
                '.intro',
                '[class*="desc"]'
            ]
            for selector in bio_selectors:
                bio_elem = soup.select_one(selector)
                if bio_elem and bio_elem.get_text(strip=True):
                    result.content = bio_elem.get_text(strip=True)
                    break
            
            # 提取头像
            avatar_elem = soup.select_one('img[class*="avatar"], img[class*="profile"]')
            if avatar_elem:
                avatar_src = avatar_elem.get('src') or avatar_elem.get('data-src')
                if avatar_src:
                    if avatar_src.startswith('//'):
                        avatar_src = 'https:' + avatar_src
                    result.images = [avatar_src]
            
            logger.info(f"✅ 用户页面解析完成 - 用户: {result.author}")
            
        except Exception as e:
            logger.warning(f"⚠️ 解析用户页面时出错: {e}")

    async def _parse_generic_page(self, soup, result: XHSUrlParseResult):
        """
        通用页面解析
        
        Args:
            soup: BeautifulSoup对象
            result: 解析结果对象（会被修改）
        """
        try:
            # 提取页面标题
            title_elem = soup.find('title')
            if title_elem:
                result.title = title_elem.get_text(strip=True)
            
            # 提取meta描述
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                result.content = meta_desc.get('content', '').strip()
            
            # 提取页面主要文本内容
            if not result.content:
                # 尝试找到主要内容区域
                main_content_selectors = [
                    'main',
                    '[role="main"]',
                    '.main-content',
                    '.content',
                    'article',
                    '.post'
                ]
                for selector in main_content_selectors:
                    content_elem = soup.select_one(selector)
                    if content_elem:
                        text_content = content_elem.get_text(strip=True)
                        if len(text_content) > 50:  # 确保内容足够长
                            result.content = text_content[:500] + "..." if len(text_content) > 500 else text_content
                            break
            
            logger.info(f"✅ 通用页面解析完成 - 标题: {result.title}")
            
        except Exception as e:
            logger.warning(f"⚠️ 通用页面解析时出错: {e}")

    def _extract_interaction_data(self, soup, result: XHSUrlParseResult):
        """
        提取互动数据（点赞、评论、分享）
        
        Args:
            soup: BeautifulSoup对象
            result: 解析结果对象（会被修改）
        """
        try:
            import re
            
            # 寻找包含数字的元素，通常是互动数据
            interaction_selectors = [
                '[class*="like"]',
                '[class*="comment"]',
                '[class*="share"]',
                '[class*="collect"]',
                '[data-testid*="like"]',
                '[data-testid*="comment"]',
                '[data-testid*="share"]'
            ]
            
            for selector in interaction_selectors:
                elements = soup.select(selector)
                for elem in elements:
                    text = elem.get_text(strip=True)
                    # 提取数字
                    numbers = re.findall(r'\d+', text)
                    if numbers:
                        number = int(numbers[0])
                        if 'like' in elem.get('class', []) or 'like' in selector:
                            result.likes = number
                        elif 'comment' in elem.get('class', []) or 'comment' in selector:
                            result.comments = number
                        elif 'share' in elem.get('class', []) or 'share' in selector:
                            result.shares = number
            
        except Exception as e:
            logger.warning(f"⚠️ 提取互动数据时出错: {e}")


# 便捷函数
def create_xhs_client(config: XHSConfig) -> XHSClient:
    """
    创建小红书客户端的便捷函数
    
    Args:
        config: 配置管理器实例
        
    Returns:
        小红书客户端实例
    """
    return XHSClient(config) 
"""
Monica API 客户端主类
"""

import aiohttp
import json
import re
from typing import Optional, Dict, Any
from html import unescape

from .contact_manager import ContactManager
from .quick_fact_manager import QuickFactManager


class MonicaClient:
    """
    Monica API 客户端类
    用于与 Monica CRM API 进行交互
    """
    
    def __init__(self, token: str, base_url: str = "http://localhost:8080"):
        """
        初始化 Monica 客户端
        
        Args:
            token: API 认证 token
            base_url: Monica API 的基础 URL，默认为 http://localhost:8080
        """
        self.token = token
        self.base_url = base_url.rstrip('/')  # 移除末尾的斜杠
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self._csrf_token = None
        self._session: Optional[aiohttp.ClientSession] = None
        
        # 初始化各个管理器
        self.contacts = ContactManager(self)
        self.quick_facts = QuickFactManager(self)
    
    async def __aenter__(self):
        """异步上下文管理器入口"""
        await self._ensure_session()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        await self.close()
    
    async def _ensure_session(self):
        """确保 session 已创建"""
        if self._session is None or self._session.closed:
            # 创建 session 时使用默认的 cookie jar（会自动管理 cookies）
            # 注意：aiohttp 的 cookie jar 可能需要显式配置
            from aiohttp import CookieJar
            jar = CookieJar(unsafe=True)  # unsafe=True 允许所有域
            self._session = aiohttp.ClientSession(cookie_jar=jar)
            # 获取 CSRF token（用于 POST/PUT/DELETE 请求）
            await self._get_csrf_token()
    
    async def close(self):
        """关闭客户端 session"""
        if self._session and not self._session.closed:
            await self._session.close()
    
    async def _get_csrf_token(self):
        """
        获取 CSRF token
        根据 Monica 路由文件：GET /sanctum/csrf-cookie
        """
        try:
            async with self._session.get(
                f"{self.base_url}/sanctum/csrf-cookie",
                headers=self.headers
            ) as response:
                if response.status == 204:
                    import urllib.parse
                    import re
                    from yarl import URL
                    
                    # 确保响应完全读取，这样 cookie jar 才会更新
                    await response.read()
                    
                    # 使用 filter_cookies 方法从 cookie jar 中获取 cookie（推荐方法）
                    url_obj = URL(f"{self.base_url}/sanctum/csrf-cookie")
                    cookies = self._session.cookie_jar.filter_cookies(url_obj)
                    csrf_cookie = cookies.get('XSRF-TOKEN')
                    
                    if csrf_cookie:
                        # cookie.value 可能是 URL 编码的，需要解码
                        decoded_value = urllib.parse.unquote(csrf_cookie.value)
                        self._csrf_token = decoded_value
                        self.headers['X-XSRF-TOKEN'] = decoded_value
                        return
                    
                    # 备用方法: 从 response.cookies 中读取
                    response_cookies = response.cookies
                    if response_cookies and 'XSRF-TOKEN' in response_cookies:
                        csrf_value = response_cookies['XSRF-TOKEN'].value
                        decoded_value = urllib.parse.unquote(csrf_value)
                        self._csrf_token = decoded_value
                        self.headers['X-XSRF-TOKEN'] = decoded_value
                        return
                    
                    # 备用方法2: 从响应头中直接读取 Set-Cookie
                    set_cookie_headers = response.headers.getall('Set-Cookie', [])
                    if not set_cookie_headers:
                        set_cookie_headers = response.headers.getall('set-cookie', [])
                    
                    for set_cookie_header in set_cookie_headers:
                        if 'XSRF-TOKEN=' in set_cookie_header:
                            match = re.search(r'XSRF-TOKEN=([^;]+)', set_cookie_header)
                            if match:
                                raw_value = match.group(1)
                                decoded_value = urllib.parse.unquote(raw_value)
                                self._csrf_token = decoded_value
                                self.headers['X-XSRF-TOKEN'] = decoded_value
                                return
                    
                    # 如果所有方法都失败，打印调试信息
                    print(f"调试: 无法从响应中提取 CSRF token")
                    print(f"  响应状态: {response.status}")
                    print(f"  filter_cookies 结果: {dict(cookies)}")
                    print(f"  response.cookies: {dict(response_cookies) if response_cookies else 'None'}")
                    print(f"  Set-Cookie 头: {set_cookie_headers}")
        except Exception as e:
            print(f"警告: 获取 CSRF token 失败: {e}")
            import traceback
            traceback.print_exc()
    
    async def _request(self, method: str, endpoint: str, params: Optional[Dict] = None, 
                     data: Optional[Dict] = None, silent: bool = False, parse_html: bool = False,
                     use_form_data: bool = False) -> Optional[Dict[str, Any]]:
        """
        通用的 HTTP 请求方法
        
        Args:
            method: HTTP 方法 (GET, POST, PUT, DELETE 等)
            endpoint: API 端点路径（例如 '/api/user'）
            params: URL 查询参数
            data: 请求体数据（用于 POST/PUT）
            silent: 如果为 True，不打印错误信息（用于内部调用）
            parse_html: 如果为 True，尝试从 HTML 响应中提取 JSON 数据（用于 Web 路由）
            use_form_data: 如果为 True，使用表单数据格式而不是 JSON
        
        Returns:
            解析后的 JSON 响应，如果请求失败则返回 None
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            await self._ensure_session()
            
            # 对于 POST/PUT/DELETE 请求，确保有 CSRF token
            if method in ['POST', 'PUT', 'DELETE']:
                # 每次 POST/PUT/DELETE 请求前都重新获取 CSRF token
                # 因为 Laravel Sanctum 可能每次请求都生成新的 token
                await self._get_csrf_token()
                
                headers = self.headers.copy()
                if self._csrf_token:
                    headers['X-XSRF-TOKEN'] = self._csrf_token
                else:
                    # 如果仍然没有 token，尝试从 cookie jar 中获取
                    import urllib.parse
                    for cookie in self._session.cookie_jar:
                        if cookie.key == 'XSRF-TOKEN':
                            self._csrf_token = urllib.parse.unquote(cookie.value)
                            headers['X-XSRF-TOKEN'] = self._csrf_token
                            break
                
            else:
                headers = self.headers.copy()
            
            # 如果使用表单数据，修改 Content-Type
            if use_form_data and data:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            
            # 使用 session 以保持 cookies
            async with self._session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data if use_form_data and data else None,
                json=data if not use_form_data else None
            ) as response:
                # 获取响应内容类型
                content_type = response.headers.get('content-type', '')
                
                # 如果响应是 HTML，尝试提取 JSON 数据
                if parse_html or content_type.startswith('text/html'):
                    text = await response.text()
                    if response.status >= 400:
                        if not silent:
                            print(f"请求错误 ({method} {endpoint}): {response.status}")
                        return None
                    return self._parse_html_response(text)
                
                # 尝试解析 JSON
                try:
                    if response.status >= 400:
                        error_text = await response.text()
                        if not silent:
                            print(f"请求错误 ({method} {endpoint}): {response.status}")
                        try:
                            error_detail = json.loads(error_text)
                            if not silent:
                                print(f"错误详情: {json.dumps(error_detail, indent=2, ensure_ascii=False)}")
                            # 检查是否是路由未找到的错误
                            error_message = error_detail.get('message', '')
                            if error_message.endswith('could not be found.'):
                                if not silent:
                                    print(f"\n提示: 此 API 端点可能在当前 Monica 版本中不可用。")
                                    print(f"      请检查 Monica 版本是否支持此功能，或查看 API 文档确认。")
                            # 检查是否是模型未找到的错误（如模板不存在）
                            elif 'No query results for model' in error_message:
                                if not silent:
                                    print(f"\n提示: 请求的资源不存在（可能是 ID 错误或资源已被删除）。")
                                    print(f"      错误详情: {error_message}")
                        except:
                            if not silent:
                                print(f"响应内容: {error_text}")
                        return None
                    
                    result = await response.json()
                    return result
                except json.JSONDecodeError:
                    # 如果不是 JSON，返回原始文本
                    text = await response.text()
                    return {"raw": text}
                
        except aiohttp.ClientError as e:
            if not silent:
                print(f"请求错误 ({method} {endpoint}): {e}")
            return None
    
    def _parse_html_response(self, html_content: str) -> Optional[Dict[str, Any]]:
        """
        从 HTML 响应中提取 JSON 数据
        Monica 的 Web 路由会在 HTML 的 data-page 属性中嵌入 JSON 数据
        
        Args:
            html_content: HTML 内容
        
        Returns:
            解析后的 JSON 数据，如果解析失败则返回 None
        """
        try:
            # 查找 data-page 属性
            pattern = r'data-page=["\']([^"\']+)["\']'
            match = re.search(pattern, html_content)
            
            if match:
                # 提取并解码 JSON 数据
                json_str = unescape(match.group(1))
                data = json.loads(json_str)
                return data
            else:
                # 如果没有找到 data-page 属性，返回 None（不打印警告，因为可能是 JSON 响应）
                # 调用者会尝试其他解析方法
                return None
        except json.JSONDecodeError as e:
            print(f"解析 JSON 数据失败: {e}")
            return None
        except Exception as e:
            print(f"解析 HTML 响应失败: {e}")
            return None
    
    async def get_current_user(self) -> Optional[Dict[str, Any]]:
        """
        获取当前认证用户信息
        根据 Monica API 文档：GET /api/user
        
        Returns:
            包含用户信息的字典，格式: {'data': {...}}
        """
        return await self._request('GET', '/api/user')
    
    async def get_vaults(self) -> Optional[Dict[str, Any]]:
        """
        获取所有 vault 列表
        根据 Monica API 文档：GET /api/vaults
        
        Returns:
            包含 vault 列表的字典，格式: {'data': [...]}
        """
        return await self._request('GET', '/api/vaults')


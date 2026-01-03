"""
Monica API 客户端主类
"""

import requests
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
        self._session = requests.Session()
        
        # 初始化各个管理器
        self.contacts = ContactManager(self)
        self.quick_facts = QuickFactManager(self)
        
        # 获取 CSRF token（用于 POST/PUT/DELETE 请求）
        self._get_csrf_token()
    
    def _get_csrf_token(self):
        """
        获取 CSRF token
        根据 Monica 路由文件：GET /sanctum/csrf-cookie
        """
        try:
            response = self._session.get(
                f"{self.base_url}/sanctum/csrf-cookie",
                headers=self.headers
            )
            if response.status_code == 204:
                # 从 cookie 中提取 CSRF token
                csrf_cookie = response.cookies.get('XSRF-TOKEN')
                if csrf_cookie:
                    import urllib.parse
                    self._csrf_token = urllib.parse.unquote(csrf_cookie)
                    # 更新 headers 以包含 CSRF token
                    self.headers['X-XSRF-TOKEN'] = self._csrf_token
        except Exception as e:
            print(f"警告: 获取 CSRF token 失败: {e}")
    
    def _request(self, method: str, endpoint: str, params: Optional[Dict] = None, 
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
            # 对于 POST/PUT/DELETE 请求，确保有 CSRF token
            if method in ['POST', 'PUT', 'DELETE'] and self._csrf_token:
                headers = self.headers.copy()
                headers['X-XSRF-TOKEN'] = self._csrf_token
            else:
                headers = self.headers.copy()
            
            # 如果使用表单数据，修改 Content-Type
            if use_form_data and data:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            
            # 使用 session 以保持 cookies
            if use_form_data and data:
                # 使用表单数据格式
                response = self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    data=data
                )
            else:
                # 使用 JSON 格式
                response = self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=data
                )
            response.raise_for_status()  # 如果状态码不是 2xx，会抛出异常
            
            # 如果响应是 HTML，尝试提取 JSON 数据
            if parse_html or response.headers.get('content-type', '').startswith('text/html'):
                return self._parse_html_response(response.text)
            
            # 尝试解析 JSON
            try:
                result = response.json()
                return result
            except json.JSONDecodeError:
                # 如果不是 JSON，返回原始文本
                return {"raw": response.text}
                
        except requests.exceptions.RequestException as e:
            if not silent:
                print(f"请求错误 ({method} {endpoint}): {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    if not silent:
                        print(f"错误详情: {json.dumps(error_detail, indent=2, ensure_ascii=False)}")
                    # 检查是否是路由未找到的错误
                    if error_detail.get('message', '').endswith('could not be found.'):
                        if not silent:
                            print(f"\n提示: 此 API 端点可能在当前 Monica 版本中不可用。")
                            print(f"      请检查 Monica 版本是否支持此功能，或查看 API 文档确认。")
                except:
                    if not silent:
                        print(f"响应内容: {e.response.text}")
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
                print("警告: 未在 HTML 中找到 data-page 属性")
                return None
        except json.JSONDecodeError as e:
            print(f"解析 JSON 数据失败: {e}")
            return None
        except Exception as e:
            print(f"解析 HTML 响应失败: {e}")
            return None
    
    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """
        获取当前认证用户信息
        根据 Monica API 文档：GET /api/user
        
        Returns:
            包含用户信息的字典，格式: {'data': {...}}
        """
        return self._request('GET', '/api/user')
    
    def get_vaults(self) -> Optional[Dict[str, Any]]:
        """
        获取所有 vault 列表
        根据 Monica API 文档：GET /api/vaults
        
        Returns:
            包含 vault 列表的字典，格式: {'data': [...]}
        """
        return self._request('GET', '/api/vaults')


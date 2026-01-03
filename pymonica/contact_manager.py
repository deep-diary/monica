"""
联系人管理器类
负责处理所有联系人相关的操作
"""

from typing import Optional, Dict, Any, List


class ContactManager:
    """
    联系人管理器
    提供联系人的增删改查功能
    """
    
    def __init__(self, client):
        """
        初始化联系人管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    def list(self, vault_id: str, limit: int = 25, page: int = 1) -> Optional[Dict[str, Any]]:
        """
        获取联系人列表
        根据 Monica 路由文件：GET /vaults/{vault}/contacts
        注意：这是 Web 路由，返回 HTML，但数据嵌入在 HTML 中
        
        Args:
            vault_id: Vault ID（必填）
            limit: 每页数量，默认为 25
            page: 页码，默认为 1
        
        Returns:
            包含联系人列表的字典，格式: {'props': {'data': {'contacts': [...]}, 'paginator': {...}}}
        """
        params = {}
        
        if page:
            params['page'] = page
        
        # 使用 Web 路由，需要解析 HTML
        return self.client._request('GET', f'/vaults/{vault_id}/contacts', params=params, parse_html=True)
    
    def get(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        获取单个联系人详情
        根据 Monica 路由文件：GET /vaults/{vault}/contacts/{contact}
        注意：这是 Web 路由，返回 HTML，但数据嵌入在 HTML 中
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            包含联系人详情的字典
        """
        # 使用 Web 路由，需要解析 HTML
        return self.client._request('GET', f'/vaults/{vault_id}/contacts/{contact_id}', parse_html=True)
    
    def create(self, vault_id: str, first_name: str, last_name: str, 
               middle_name: str = "", nickname: str = "", prefix: str = "", 
               suffix: str = "", maiden_name: str = "", gender_id: str = "", 
               pronoun_id: str = "", template_id: str = "") -> Optional[Dict[str, Any]]:
        """
        创建联系人
        根据 Monica 路由文件：POST /vaults/{vault}/contacts
        
        Args:
            vault_id: Vault ID（必填）
            first_name: 名字（必填）
            last_name: 姓氏（必填）
            middle_name: 中间名（可选）
            nickname: 昵称（可选）
            prefix: 前缀（可选）
            suffix: 后缀（可选）
            maiden_name: 婚前姓氏（可选）
            gender_id: 性别 ID（可选）
            pronoun_id: 代词 ID（可选）
            template_id: 模板 ID（可选）
        
        Returns:
            包含创建结果的字典，格式: {'data': '联系人详情 URL'}
        """
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "nickname": nickname,
            "prefix": prefix,
            "suffix": suffix,
            "maiden_name": maiden_name,
            "gender_id": gender_id,
            "pronoun_id": pronoun_id,
            "template_id": template_id,
            "errors": []
        }
        
        return self.client._request('POST', f'/vaults/{vault_id}/contacts', data=data)
    
    def update(self, vault_id: str, contact_id: str, **kwargs) -> Optional[Dict[str, Any]]:
        """
        更新联系人信息
        根据 Monica 路由文件：POST /vaults/{vault}/contacts/{contact}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            **kwargs: 要更新的字段，支持以下字段：
                - first_name: 名字
                - last_name: 姓氏
                - middle_name: 中间名
                - nickname: 昵称
                - prefix: 前缀
                - suffix: 后缀
                - maiden_name: 婚前姓氏
                - gender_id: 性别 ID
                - pronoun_id: 代词 ID
                - template_id: 模板 ID
                以及其他联系人字段
        
        Returns:
            更新后的联系人信息
        """
        return self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}', data=kwargs)
    
    def delete(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        删除联系人
        根据 Monica 路由文件：DELETE /vaults/{vault}/contacts/{contact}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            删除结果
        """
        return self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}')
    
    def search(self, vault_id: str, query: str, page: int = 1) -> Optional[Dict[str, Any]]:
        """
        搜索联系人
        根据 Monica 路由文件：POST /vaults/{vault}/search/user/contacts
        
        注意：此功能在某些 Monica 版本中可能返回服务器错误（500）。
        如果遇到错误，建议使用 list() 方法获取所有联系人后手动过滤。
        
        Args:
            vault_id: Vault ID（必填）
            query: 搜索查询字符串（必填）
            page: 页码，默认为 1（当前版本可能不支持分页）
        
        Returns:
            包含搜索结果的联系人列表，格式: {'data': [{'id': '...', 'name': '...', 'url': '...'}]}
            如果搜索失败，返回 None
        """
        # 根据官方 API 格式，使用 searchTerm 作为搜索关键词
        # 注意：这些字段是 Laravel Inertia.js 表单的格式
        # 根据官方示例，使用布尔值和 null 而不是字符串
        data = {
            "searchTerm": query,
            "errors": {},
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        # 使用 JSON 格式（根据官方示例）
        result = self.client._request('POST', f'/vaults/{vault_id}/search/user/contacts', data=data)
        
        # 如果搜索失败，返回 None 并提示用户
        if result is None:
            print("提示: 搜索功能可能在当前 Monica 版本中不可用，或服务器返回错误。")
            print("      建议使用 list() 方法获取所有联系人后手动过滤。")
        
        return result
    
    def extract_contacts_from_response(self, response: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        从响应中提取联系人列表
        辅助方法，用于从不同的响应格式中提取联系人数据
        
        Args:
            response: API 响应字典
        
        Returns:
            联系人列表
        """
        contacts = []
        
        # 尝试不同的数据结构
        if 'props' in response and 'data' in response['props']:
            data = response['props']['data']
            if 'contacts' in data:
                contacts = data['contacts']
        elif 'data' in response:
            if 'contacts' in response['data']:
                contacts = response['data']['contacts']
            elif isinstance(response['data'], dict) and 'data' in response['data']:
                inner_data = response['data']['data']
                if 'contacts' in inner_data:
                    contacts = inner_data['contacts']
        
        return contacts if isinstance(contacts, list) else []


"""
联系人信息提取器类
负责从联系人详情页面（/tabs/information）提取所有信息
"""

import re
from typing import Optional, Dict, Any, List


class ContactInformationExtractor:
    """
    联系人信息提取器
    从联系人详情页面统一提取所有模块的信息
    """
    
    def __init__(self, client):
        """
        初始化联系人信息提取器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
        self._cached_data: Optional[Dict[str, Any]] = None
        self._cached_vault_id: Optional[str] = None
        self._cached_contact_id: Optional[str] = None
    
    async def get_full_information(self, vault_id: str, contact_id: str, 
                                   use_cache: bool = True) -> Optional[Dict[str, Any]]:
        """
        获取完整的联系人详情信息
        从 /tabs/information 端点获取并解析所有数据
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            包含所有联系人信息的字典，如果获取失败则返回 None
        """
        # 如果使用缓存且参数相同，直接返回缓存的数据
        if use_cache and self._cached_data and \
           self._cached_vault_id == vault_id and \
           self._cached_contact_id == contact_id:
            return self._cached_data
        
        # 获取联系人详情页面
        contact_info = await self.client._request(
            'GET', 
            f'/vaults/{vault_id}/contacts/{contact_id}/tabs/information', 
            parse_html=True
        )
        
        if not contact_info:
            return None
        
        # 缓存数据
        self._cached_data = contact_info
        self._cached_vault_id = vault_id
        self._cached_contact_id = contact_id
        
        return contact_info
    
    def get_contact_id(self, contact_detail: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        从联系人详情中提取联系人ID
        
        Args:
            contact_detail: 联系人详情字典（如果为None，使用缓存的数据）
        
        Returns:
            联系人ID，如果未找到则返回None
        """
        if contact_detail is None:
            contact_detail = self._cached_data
        
        if not contact_detail:
            return None
        
        # 尝试从多个位置提取ID
        data = self._get_data_from_detail(contact_detail)
        
        # 方法1: 从 contact_name.url.edit 中提取
        contact_name = data.get('contact_name', {})
        if isinstance(contact_name, dict):
            url = contact_name.get('url', {})
            if isinstance(url, dict):
                edit_url = url.get('edit', '')
                if edit_url:
                    # 从URL中提取contact_id: /vaults/{vault}/contacts/{contact_id}/edit
                    match = re.search(r'/contacts/([^/]+)/edit', edit_url)
                    if match:
                        return match.group(1)
        
        # 方法2: 从其他URL中提取
        url_obj = data.get('url', {})
        if isinstance(url_obj, dict):
            for url_key, url_value in url_obj.items():
                if isinstance(url_value, str) and '/contacts/' in url_value:
                    match = re.search(r'/contacts/([^/]+)', url_value)
                    if match:
                        return match.group(1)
        
        return None
    
    def get_contact_name(self, contact_detail: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        从联系人详情中提取联系人名称
        
        Args:
            contact_detail: 联系人详情字典（如果为None，使用缓存的数据）
        
        Returns:
            联系人名称，如果未找到则返回None
        """
        if contact_detail is None:
            contact_detail = self._cached_data
        
        if not contact_detail:
            return None
        
        data = self._get_data_from_detail(contact_detail)
        contact_name = data.get('contact_name', {})
        
        if isinstance(contact_name, dict):
            name = contact_name.get('name')
            if name:
                return name
        
        return None
    
    async def get_all_information_as_dict(self, vault_id: str, contact_id: str,
                                            use_cache: bool = True) -> Optional[Dict[str, Any]]:
        """
        获取所有联系人信息并以字典格式返回

        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）

        Returns:
            包含所有联系人信息的字典，如果获取失败则返回 None
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return None

        return {
            "contact_id": self.get_contact_id(contact_detail) or contact_id,
            "contact_name": self.get_contact_name(contact_detail),
            "calls": await self.get_calls(vault_id, contact_id, use_cache=True),
            "reminders": await self.get_reminders(vault_id, contact_id, use_cache=True),
            "notes": await self.get_notes(vault_id, contact_id, use_cache=True),
            "addresses": await self.get_addresses(vault_id, contact_id, use_cache=True),
            "contact_information": await self.get_contact_information(
                vault_id, contact_id, use_cache=True
            ),
            "dates": await self.get_dates(vault_id, contact_id, use_cache=True),
            "quick_facts": await self.get_quick_facts(vault_id, contact_id, use_cache=True),
            "quick_facts_list": await self.get_quick_facts_list(
                vault_id, contact_id, use_cache=True
            ),
            "all_modules": await self.get_all_modules(vault_id, contact_id, use_cache=True),
        }

    async def get_all_information_as_json(self, vault_id: str, contact_id: str, 
                                          use_cache: bool = True, 
                                          indent: int = 2) -> Optional[str]:
        """
        获取所有联系人信息并以JSON格式返回
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
            indent: JSON缩进空格数（默认 2）
        
        Returns:
            JSON格式的字符串，如果获取失败则返回None
        """
        import json

        all_info = await self.get_all_information_as_dict(
            vault_id, contact_id, use_cache=use_cache
        )
        if not all_info:
            return None

        return json.dumps(all_info, ensure_ascii=False, indent=indent)
    
    def _get_data_from_detail(self, contact_detail: Dict[str, Any]) -> Dict[str, Any]:
        """
        从联系人详情中提取 data 对象
        
        Args:
            contact_detail: 联系人详情字典
        
        Returns:
            data 字典
        """
        if 'props' in contact_detail and 'data' in contact_detail['props']:
            return contact_detail['props']['data']
        elif 'data' in contact_detail:
            return contact_detail['data']
        return {}
    
    def _get_modules_from_detail(self, contact_detail: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        从联系人详情中提取 modules 数组
        
        Args:
            contact_detail: 联系人详情字典
        
        Returns:
            modules 数组
        """
        data = self._get_data_from_detail(contact_detail)
        if 'modules' in data and isinstance(data['modules'], list):
            return data['modules']
        return []
    
    def _extract_module_data(self, contact_detail: Dict[str, Any], 
                             module_type: str, data_key: str = None, 
                             alternative_keys: List[str] = None) -> Any:
        """
        从联系人详情中提取指定类型模块的数据
        
        Args:
            contact_detail: 联系人详情字典
            module_type: 模块类型（如 "calls", "reminders", "notes" 等）
            data_key: 数据键名（如果为 None，则使用 module_type）
            alternative_keys: 备选键名列表（用于尝试不同的键名）
        
        Returns:
            提取的数据（通常是列表或字典）
        """
        if data_key is None:
            data_key = module_type
        
        # 准备所有可能的键名
        possible_keys = [data_key]
        if alternative_keys:
            possible_keys.extend(alternative_keys)
        # 添加单数形式（addresses -> address）
        if data_key.endswith('es'):
            possible_keys.append(data_key[:-2])
        elif data_key.endswith('s'):
            possible_keys.append(data_key[:-1])
        
        try:
            modules = self._get_modules_from_detail(contact_detail)
            
            # 从 modules 数组中查找指定类型的模块
            for module in modules:
                if isinstance(module, dict):
                    module_type_value = module.get('type')
                    # 尝试精确匹配和部分匹配
                    if module_type_value == module_type or \
                       (module_type_value and module_type in module_type_value) or \
                       (module_type_value and module_type_value in module_type):
                        module_data = module.get('data', {})
                        if isinstance(module_data, dict):
                            # 尝试所有可能的键名
                            for key in possible_keys:
                                if key in module_data:
                                    result = module_data[key]
                                    if isinstance(result, list) or isinstance(result, dict):
                                        return result
                            # 如果没找到，返回整个 module_data
                            return module_data
                        elif isinstance(module_data, list):
                            return module_data
                        return module_data
            
            # 备用路径：直接从 data 中查找
            data = self._get_data_from_detail(contact_detail)
            for key in possible_keys:
                if key in data:
                    result = data[key]
                    if isinstance(result, list) or isinstance(result, dict):
                        return result
            
        except Exception as e:
            print(f"提取模块数据时出错 ({module_type}): {e}")
        
        return None
    
    async def get_calls(self, vault_id: str, contact_id: str, 
                       use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取通话记录列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            通话记录列表
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        calls = self._extract_module_data(contact_detail, 'calls', 'calls')
        if isinstance(calls, list):
            return calls
        return []
    
    async def get_reminders(self, vault_id: str, contact_id: str, 
                           use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取提醒事项列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            提醒事项列表
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        reminders = self._extract_module_data(contact_detail, 'reminders', 'reminders')
        if isinstance(reminders, list):
            return reminders
        return []
    
    async def get_notes(self, vault_id: str, contact_id: str, 
                       use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取笔记列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            笔记列表
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        notes = self._extract_module_data(contact_detail, 'notes', 'notes')
        if isinstance(notes, list):
            return notes
        return []
    
    async def get_addresses(self, vault_id: str, contact_id: str, 
                           use_cache: bool = True, include_inactive: bool = False) -> List[Dict[str, Any]]:
        """
        获取地址列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
            include_inactive: 是否包含非活动地址（默认 False）
        
        Returns:
            地址列表
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        # 地址模块的数据结构：data.active_addresses 和 data.inactive_addresses
        module_data = self._extract_module_data(
            contact_detail, 
            'addresses', 
            'addresses'
        )
        
        if isinstance(module_data, dict):
            addresses = []
            # 获取活动地址
            if 'active_addresses' in module_data:
                active = module_data['active_addresses']
                if isinstance(active, list):
                    addresses.extend(active)
            # 如果需要，也包含非活动地址
            if include_inactive and 'inactive_addresses' in module_data:
                inactive = module_data['inactive_addresses']
                if isinstance(inactive, list):
                    addresses.extend(inactive)
            return addresses
        elif isinstance(module_data, list):
            return module_data
        
        return []
    
    async def get_contact_information(self, vault_id: str, contact_id: str, 
                                     use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取联系信息列表（邮箱、电话等）
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            联系信息列表
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        # 联系信息模块的数据结构：data.contact_information
        # 注意：模块类型是 'contact_information'（下划线），不是 'contactInformation'
        module_data = self._extract_module_data(
            contact_detail, 
            'contact_information', 
            'contact_information',
            alternative_keys=['contactInformation', 'contactInfo', 'contact_info', 'information']
        )
        
        if isinstance(module_data, dict):
            # 如果 module_data 是字典，尝试提取 contact_information 键
            if 'contact_information' in module_data:
                contact_info = module_data['contact_information']
                if isinstance(contact_info, list):
                    return contact_info
        elif isinstance(module_data, list):
            return module_data
        
        return []
    
    async def get_dates(self, vault_id: str, contact_id: str, 
                        use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取日期列表（生日、纪念日等重要日期）
        
        注意：dates 数据不在 modules 中，而是在 data.contact_information 列表中
        有一个 type="important_dates" 的项，其 data.dates 包含日期列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            日期列表（包括生日、纪念日、其他重要日期等）
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return []
        
        # dates 数据在 data.contact_information 列表中，类型为 "important_dates"
        data = self._get_data_from_detail(contact_detail)
        contact_information = data.get('contact_information', [])
        
        if isinstance(contact_information, list):
            for item in contact_information:
                if isinstance(item, dict) and item.get('type') == 'important_dates':
                    item_data = item.get('data', {})
                    if isinstance(item_data, dict) and 'dates' in item_data:
                        dates = item_data['dates']
                        if isinstance(dates, list):
                            return dates
        
        # 备用：尝试从模块中提取
        dates = self._extract_module_data(
            contact_detail, 
            'dates', 
            'dates',
            alternative_keys=['date', 'importantDates', 'important_dates']
        )
        if isinstance(dates, list):
            return dates
        
        return []
    
    async def get_all_modules(self, vault_id: str, contact_id: str, 
                             use_cache: bool = True) -> Dict[str, Any]:
        """
        获取所有模块的数据
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            包含所有模块数据的字典，格式：
            {
                "calls": [...],
                "reminders": [...],
                "notes": [...],
                "addresses": [...],
                "contactInformation": [...],
                "dates": [...],
                ...
            }
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return {}
        
        modules = self._get_modules_from_detail(contact_detail)
        result = {}
        
        # 提取所有模块的数据
        for module in modules:
            if isinstance(module, dict):
                module_type = module.get('type')
                module_data = module.get('data', {})
                
                if module_type:
                    # 如果 module_data 是字典，尝试提取常见的数据键
                    if isinstance(module_data, dict):
                        # 尝试使用模块类型作为键名
                        if module_type in module_data:
                            result[module_type] = module_data[module_type]
                        else:
                            # 否则使用整个 module_data
                            result[module_type] = module_data
                    else:
                        result[module_type] = module_data
        
        # 也从 data 中提取直接的数据（备用）
        data = self._get_data_from_detail(contact_detail)
        for key in ['calls', 'reminders', 'notes', 'addresses', 'contactInformation', 'dates']:
            if key in data and key not in result:
                result[key] = data[key]
        
        return result
    
    def clear_cache(self):
        """
        清除缓存的数据
        """
        self._cached_data = None
        self._cached_vault_id = None
        self._cached_contact_id = None
    
    async def get_module_by_type(self, vault_id: str, contact_id: str, 
                                module_type: str, use_cache: bool = True) -> Any:
        """
        根据模块类型获取数据（通用方法）
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            module_type: 模块类型（如 "calls", "reminders" 等）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            模块数据
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return None
        
        return self._extract_module_data(contact_detail, module_type)
    
    async def get_quick_facts(self, vault_id: str, contact_id: str, 
                              use_cache: bool = True) -> Dict[str, Any]:
        """
        获取快速事实（Quick Facts）信息
        
        注意：quickFacts 数据在 data.quick_fact_template_entries 中
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            包含快速事实信息的字典，格式：
            {
                "show_quick_facts": bool,
                "templates": [...],  # 模板列表
                "quick_facts": [...],  # 快速事实列表
                "url": {...}
            }
        """
        contact_detail = await self.get_full_information(vault_id, contact_id, use_cache)
        if not contact_detail:
            return {}
        
        data = self._get_data_from_detail(contact_detail)
        quick_fact_data = data.get('quick_fact_template_entries', {})
        
        if isinstance(quick_fact_data, dict):
            return quick_fact_data
        
        return {}
    
    async def get_quick_facts_list(self, vault_id: str, contact_id: str, 
                                   use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        获取快速事实列表（便捷方法）
        
        注意：quick_facts 数据结构是嵌套的：
        quick_fact_template_entries.quick_facts 是一个字典，包含：
        - template: 模板信息
        - quick_facts: 实际的快速事实列表
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            use_cache: 是否使用缓存（默认 True）
        
        Returns:
            快速事实列表
        """
        quick_facts_data = await self.get_quick_facts(vault_id, contact_id, use_cache)
        quick_facts_obj = quick_facts_data.get('quick_facts', {})
        
        # quick_facts 可能是一个字典，包含 template 和 quick_facts 键
        if isinstance(quick_facts_obj, dict):
            quick_facts_list = quick_facts_obj.get('quick_facts', [])
            if isinstance(quick_facts_list, list):
                return quick_facts_list
        # 或者直接是列表
        elif isinstance(quick_facts_obj, list):
            return quick_facts_obj
        
        return []
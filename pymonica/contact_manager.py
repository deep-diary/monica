"""
联系人管理器类
负责处理所有联系人相关的操作
"""

from typing import Optional, Dict, Any, List

# 可选依赖：pypinyin（用于中文转拼音）
try:
    from pypinyin import lazy_pinyin, Style
    HAS_PYPINYIN = True
except ImportError:
    HAS_PYPINYIN = False


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
    
    async def list(self, vault_id: str, limit: int = 25, page: int = 1) -> Optional[Dict[str, Any]]:
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
        return await self.client._request('GET', f'/vaults/{vault_id}/contacts', params=params, parse_html=True)
    
    async def get(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
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
        return await self.client._request('GET', f'/vaults/{vault_id}/contacts/{contact_id}', parse_html=True)
    
    async def create(self, vault_id: str, first_name: str, last_name: str, 
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
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts', data=data)
    
    async def update(self, vault_id: str, contact_id: str, **kwargs) -> Optional[Dict[str, Any]]:
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
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}', data=kwargs)
    
    async def delete(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        删除联系人
        根据 Monica 路由文件：DELETE /vaults/{vault}/contacts/{contact}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}')
    
    async def search(self, vault_id: str, query: str, page: int = 1) -> Optional[Dict[str, Any]]:
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
        result = await self.client._request('POST', f'/vaults/{vault_id}/search/user/contacts', data=data)
        
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
    
    @staticmethod
    def generate_nickname(last_name: str, first_name: str) -> str:
        """
        使用 pypinyin 将中文姓名转换为全拼，格式为全小写无空格（便于检索）
        
        Args:
            last_name: 姓氏
            first_name: 名字
        
        Returns:
            格式化的昵称，例如: machengxue
        
        Raises:
            ImportError: 如果未安装 pypinyin 库
        """
        if not HAS_PYPINYIN:
            raise ImportError(
                "未安装 pypinyin 库。请运行: pip install pypinyin\n"
                "generate_nickname 方法需要 pypinyin 库来将中文转换为拼音。"
            )
        
        # 将中文转换为拼音（全拼，不带声调）
        last_name_pinyin = ''.join(lazy_pinyin(last_name, style=Style.NORMAL))
        first_name_pinyin = ''.join(lazy_pinyin(first_name, style=Style.NORMAL))
        
        # 格式化为全小写无空格（便于检索）
        return f"{last_name_pinyin}{first_name_pinyin}".lower()
    
    @staticmethod
    def map_gender(gender_str: str) -> str:
        """
        将性别字符串映射到 gender_id
        
        Args:
            gender_str: 性别字符串，如 "男"、"女" 等
        
        Returns:
            gender_id 字符串，如 "1"、"2" 等
        """
        gender_map = {
            "男": "1",
            "女": "2",
            "male": "1",
            "female": "2",
            "m": "1",
            "f": "2",
        }
        
        # 去除空格并转换为小写进行比较
        gender_clean = gender_str.strip().lower() if isinstance(gender_str, str) else ""
        
        # 如果是中文，直接查找
        if gender_str.strip() in gender_map:
            return gender_map[gender_str.strip()]
        
        # 如果是英文，查找小写版本
        if gender_clean in gender_map:
            return gender_map[gender_clean]
        
        # 如果找不到匹配，返回空字符串（可选字段）
        return ""
    
    async def list_all(self, vault_id: str, limit: int = 100, verbose: bool = False) -> List[Dict[str, Any]]:
        """
        获取 vault 中的所有联系人（处理分页）
        
        Args:
            vault_id: Vault ID
            limit: 每页数量，默认为 100（减少请求次数）
            verbose: 是否打印详细信息（用于调试）
        
        Returns:
            所有联系人的列表
        """
        all_contacts = []
        page = 1
        
        if verbose:
            print("正在获取现有联系人列表...")
        
        while True:
            contacts_data = await self.list(vault_id=vault_id, limit=limit, page=page)
            
            if not contacts_data:
                break
            
            # 提取联系人列表
            contacts = self.extract_contacts_from_response(contacts_data)
            
            if not contacts:
                break
            
            all_contacts.extend(contacts)
            
            # 检查是否还有更多页面
            paginator = None
            if 'props' in contacts_data and 'data' in contacts_data['props']:
                paginator = contacts_data['props']['data'].get('paginator', {})
            elif 'data' in contacts_data:
                if isinstance(contacts_data['data'], dict):
                    paginator = contacts_data['data'].get('paginator', {})
            
            if paginator:
                current_page = paginator.get('current_page', page)
                last_page = paginator.get('last_page', 1)
                if current_page >= last_page:
                    break
            
            page += 1
        
        if verbose:
            print(f"已获取 {len(all_contacts)} 个现有联系人")
            
            # 打印现有联系人详细信息（用于调试）
            if all_contacts:
                print("\n现有联系人列表:")
                for i, contact in enumerate(all_contacts, 1):
                    contact_id = contact.get('id', 'N/A')
                    contact_name = contact.get('name', 'N/A')
                    contact_nickname = contact.get('nickname', 'N/A')
                    print(f"  {i}. ID: {contact_id}")
                    print(f"     姓名: {contact_name}")
                    print(f"     昵称: {contact_nickname}")
                    if 'first_name' in contact:
                        print(f"     first_name: {contact.get('first_name')}")
                    if 'last_name' in contact:
                        print(f"     last_name: {contact.get('last_name')}")
                    print()
                print()
        
        return all_contacts
    
    def find_existing(self, contacts: List[Dict[str, Any]], first_name: str, last_name: str, 
                     nickname: str = "", debug: bool = False) -> Optional[Dict[str, str]]:
        """
        在现有联系人列表中查找匹配的联系人
        
        匹配规则：
        1. 优先通过姓名匹配（last_name + first_name，去除空格）
        2. 如果姓名匹配，则认为是同一个联系人
        3. 也可以通过昵称匹配
        
        Args:
            contacts: 现有联系人列表
            first_name: 名字
            last_name: 姓氏
            nickname: 昵称（用于显示和匹配）
            debug: 是否打印调试信息
        
        Returns:
            如果找到匹配的联系人，返回包含 contact_id 和 match_type 的字典；否则返回 None
        """
        # 构建期望的姓名（格式：last_name + first_name，去除空格）
        expected_name = f"{last_name}{first_name}".strip().replace(' ', '')  # 格式: 马成学
        
        if debug:
            print(f"    调试: 查找联系人 - 期望姓名: {expected_name}, 昵称: {nickname}")
        
        # 构建姓名和昵称的映射表（去除空格，用于快速查找）
        # 使用字典存储：{去除空格后的姓名: contact_info}
        name_map = {}
        nickname_map = {}
        
        for contact in contacts:
            contact_id = contact.get('id')
            if not contact_id:
                continue
            
            # 构建姓名映射（去除空格）
            contact_name = contact.get('name', '').strip()
            if contact_name:
                contact_name_no_space = contact_name.replace(' ', '')
                if contact_name_no_space not in name_map:
                    name_map[contact_name_no_space] = {
                        'contact_id': contact_id,
                        'original_name': contact_name
                    }
            
            # 构建昵称映射
            contact_nickname = contact.get('nickname', '').strip()
            if contact_nickname:
                # 去除昵称中的方括号、空格等格式字符
                contact_nickname_clean = contact_nickname.strip('[]').replace(' ', '').lower()
                if contact_nickname_clean not in nickname_map:
                    nickname_map[contact_nickname_clean] = {
                        'contact_id': contact_id,
                        'original_nickname': contact_nickname
                    }
        
        # 首先通过姓名匹配（O(1) 查找）
        if expected_name in name_map:
            match_info = name_map[expected_name]
            if debug:
                print(f"    调试: ✓ 通过姓名匹配成功 (现有: '{match_info['original_name']}', 期望: '{expected_name}')")
            return {'contact_id': match_info['contact_id'], 'match_type': 'name'}
        
        # 如果姓名不匹配，尝试通过昵称匹配
        if nickname:
            nickname_clean = nickname.strip('[]').replace(' ', '').lower()
            if nickname_clean in nickname_map:
                match_info = nickname_map[nickname_clean]
                if debug:
                    print(f"    调试: ✓ 通过昵称匹配成功 (现有: '{match_info['original_nickname']}', 期望: '{nickname}')")
                return {'contact_id': match_info['contact_id'], 'match_type': 'nickname'}
        
        if debug:
            print(f"    调试: ✗ 未找到匹配的联系人")
        
        return None
    
    async def batch_create_or_update(self, vault_id: str, contacts_data: List[Dict[str, Any]], 
                                     verbose: bool = False, debug: bool = False) -> Dict[str, int]:
        """
        批量创建或更新联系人
        
        对于每个联系人数据：
        - 如果联系人已存在（通过姓名或昵称匹配），则更新
        - 如果联系人不存在，则创建
        
        Args:
            vault_id: Vault ID
            contacts_data: 联系人数据列表，每个字典应包含：
                - first_name: 名字（必填）
                - last_name: 姓氏（必填）
                - nickname: 昵称（可选，用于匹配）
                - gender_id: 性别 ID（可选）
                以及其他联系人字段
            verbose: 是否打印详细信息
            debug: 是否打印调试信息（用于查找匹配过程）
        
        Returns:
            包含统计信息的字典：
                - created: 创建的联系人数量
                - updated: 更新的联系人数量
                - failed: 失败的联系人数量
                - total: 总计处理数量
        """
        # 先获取所有现有联系人
        if verbose:
            print("正在获取现有联系人列表...")
        
        existing_contacts = await self.list_all(vault_id, verbose=verbose)
        
        # 构建姓名和昵称的映射表（一次性构建，提高效率）
        # 使用字典存储：{去除空格后的姓名: contact_info}
        name_map = {}
        nickname_map = {}
        
        for contact in existing_contacts:
            contact_id = contact.get('id')
            if not contact_id:
                continue
            
            # 构建姓名映射（支持多种格式）
            contact_name = contact.get('name', '').strip()
            contact_first_name = contact.get('first_name', '').strip()
            contact_last_name = contact.get('last_name', '').strip()
            
            # 如果同时有 first_name 和 last_name，构建两种格式的映射
            if contact_first_name and contact_last_name:
                # 格式1: last_name + first_name（如：王中亮）
                name_format1 = f"{contact_last_name}{contact_first_name}".replace(' ', '')
                if name_format1 not in name_map:
                    name_map[name_format1] = {
                        'contact_id': contact_id,
                        'original_name': contact_name or f"{contact_last_name}{contact_first_name}",
                        'contact': contact
                    }
                
                # 格式2: first_name + last_name（如：中亮王）
                name_format2 = f"{contact_first_name}{contact_last_name}".replace(' ', '')
                if name_format2 not in name_map:
                    name_map[name_format2] = {
                        'contact_id': contact_id,
                        'original_name': contact_name or f"{contact_first_name} {contact_last_name}",
                        'contact': contact
                    }
            
            # 如果只有 name 字段，尝试解析并构建映射
            if contact_name and not (contact_first_name and contact_last_name):
                # 去除空格后的姓名
                contact_name_no_space = contact_name.replace(' ', '')
                if contact_name_no_space not in name_map:
                    name_map[contact_name_no_space] = {
                        'contact_id': contact_id,
                        'original_name': contact_name,
                        'contact': contact
                    }
                
                # 如果 name 中包含空格，可能是 "first_name + 空格 + last_name" 格式
                # 尝试构建反向格式（last_name + first_name）
                if ' ' in contact_name:
                    parts = contact_name.split()
                    if len(parts) == 2:
                        # 假设格式是 "first_name + 空格 + last_name"
                        possible_first = parts[0]
                        possible_last = parts[1]
                        # 构建反向格式
                        reversed_name = f"{possible_last}{possible_first}".replace(' ', '')
                        if reversed_name not in name_map:
                            name_map[reversed_name] = {
                                'contact_id': contact_id,
                                'original_name': contact_name,
                                'contact': contact
                            }
            
            # 构建昵称映射
            contact_nickname = contact.get('nickname', '').strip()
            if contact_nickname:
                # 去除昵称中的方括号、空格等格式字符
                contact_nickname_clean = contact_nickname.strip('[]').replace(' ', '').lower()
                if contact_nickname_clean not in nickname_map:
                    nickname_map[contact_nickname_clean] = {
                        'contact_id': contact_id,
                        'original_nickname': contact_nickname,
                        'contact': contact  # 保留完整联系人信息
                    }
        
        if verbose:
            print(f"已构建姓名映射表: {len(name_map)} 个联系人")
            print(f"已构建昵称映射表: {len(nickname_map)} 个联系人（部分联系人可能没有昵称）")
            print(f"准备处理 {len(contacts_data)} 个联系人...\n")
        
        create_count = 0
        update_count = 0
        fail_count = 0
        
        for i, contact_data in enumerate(contacts_data, 1):
            first_name = contact_data.get('first_name', '').strip()
            last_name = contact_data.get('last_name', '').strip()
            nickname = contact_data.get('nickname', '').strip()
            gender_id = contact_data.get('gender_id', '')
            
            # 跳过无效数据
            if not first_name and not last_name:
                if verbose:
                    print(f"[{i}/{len(contacts_data)}] 跳过无效联系人数据（缺少姓名）\n")
                fail_count += 1
                continue
            
            if verbose:
                gender_str = contact_data.get('gender_str', gender_id)
                print(f"[{i}/{len(contacts_data)}] 处理联系人: {last_name}{first_name} (昵称: {nickname}, 性别: {gender_str})")
            
            try:
                # 构建期望的姓名（格式：last_name + first_name，去除空格）
                expected_name1 = f"{last_name}{first_name}".strip().replace(' ', '')  # 格式1: 王中亮
                expected_name2 = f"{first_name}{last_name}".strip().replace(' ', '')  # 格式2: 中亮王
                
                # 使用预构建的映射表进行快速查找
                existing = None
                
                if debug:
                    print(f"    调试: 查找联系人 - 期望姓名格式1: {expected_name1}, 格式2: {expected_name2}, 昵称: {nickname}")
                
                # 首先通过姓名匹配（O(1) 查找，检查两种格式）
                if expected_name1 in name_map:
                    match_info = name_map[expected_name1]
                    if debug:
                        print(f"    调试: ✓ 通过姓名匹配成功 (现有: '{match_info['original_name']}', 期望格式1: '{expected_name1}')")
                    existing = {'contact_id': match_info['contact_id'], 'match_type': 'name'}
                elif expected_name2 in name_map:
                    match_info = name_map[expected_name2]
                    if debug:
                        print(f"    调试: ✓ 通过姓名匹配成功 (现有: '{match_info['original_name']}', 期望格式2: '{expected_name2}')")
                    existing = {'contact_id': match_info['contact_id'], 'match_type': 'name'}
                
                # 如果姓名不匹配，尝试通过昵称匹配
                if not existing and nickname:
                    nickname_clean = nickname.strip('[]').replace(' ', '').lower()
                    if nickname_clean in nickname_map:
                        match_info = nickname_map[nickname_clean]
                        if debug:
                            print(f"    调试: ✓ 通过昵称匹配成功 (现有: '{match_info['original_nickname']}', 期望: '{nickname}')")
                        existing = {'contact_id': match_info['contact_id'], 'match_type': 'nickname'}
                
                if not existing and debug:
                    print(f"    调试: ✗ 未找到匹配的联系人")
                
                if existing:
                    # 联系人已存在，执行更新
                    contact_id = existing['contact_id']
                    match_type = existing['match_type']
                    
                    if verbose:
                        print(f"  → 联系人已存在 (ID: {contact_id}, 匹配方式: {match_type})，执行更新...")
                    
                    # 准备更新数据（排除不需要的字段）
                    update_data = {k: v for k, v in contact_data.items() 
                                  if k not in ['gender_str'] and v}
                    
                    result = await self.update(
                        vault_id=vault_id,
                        contact_id=contact_id,
                        **update_data
                    )
                    
                    if result:
                        update_count += 1
                        if verbose:
                            print(f"  ✓ 更新成功")
                    else:
                        fail_count += 1
                        if verbose:
                            print(f"  ✗ 更新失败: 未返回结果")
                else:
                    # 联系人不存在，执行创建
                    if verbose:
                        print(f"  → 联系人不存在，执行创建...")
                    
                    # 准备创建数据
                    create_data = {
                        'first_name': first_name,
                        'last_name': last_name,
                        'nickname': nickname,
                        'gender_id': gender_id if gender_id else "",
                    }
                    # 添加其他可选字段
                    for key in ['middle_name', 'prefix', 'suffix', 'maiden_name', 'pronoun_id', 'template_id']:
                        if key in contact_data and contact_data[key]:
                            create_data[key] = contact_data[key]
                    
                    result = await self.create(
                        vault_id=vault_id,
                        **create_data
                    )
                    
                    if result:
                        create_count += 1
                        if verbose:
                            print(f"  ✓ 创建成功")
                        
                        # 如果创建成功，尝试从结果中提取联系人 ID 并添加到映射表
                        # 这样可以避免重复数据导致的重复创建
                        contact_url = result.get('data', '')
                        if contact_url and '/contacts/' in contact_url:
                            contact_id = contact_url.split('/contacts/')[-1].split('?')[0].split('#')[0]
                            if contact_id:
                                # 构建新联系人的姓名（去除空格）
                                new_contact_name = f"{last_name}{first_name}".strip().replace(' ', '')
                                
                                # 将新联系人添加到姓名映射表
                                if new_contact_name not in name_map:
                                    name_map[new_contact_name] = {
                                        'contact_id': contact_id,
                                        'original_name': f"{last_name}{first_name}",
                                        'contact': {
                                            'id': contact_id,
                                            'name': f"{last_name}{first_name}",
                                            'nickname': nickname,
                                            'first_name': first_name,
                                            'last_name': last_name
                                        }
                                    }
                                
                                # 如果有昵称，也添加到昵称映射表
                                if nickname:
                                    nickname_clean = nickname.strip('[]').replace(' ', '').lower()
                                    if nickname_clean not in nickname_map:
                                        nickname_map[nickname_clean] = {
                                            'contact_id': contact_id,
                                            'original_nickname': nickname,
                                            'contact': {
                                                'id': contact_id,
                                                'name': f"{last_name}{first_name}",
                                                'nickname': nickname,
                                                'first_name': first_name,
                                                'last_name': last_name
                                            }
                                        }
                                
                                # 同时添加到现有联系人列表（保持兼容性）
                                existing_contacts.append({
                                    'id': contact_id,
                                    'name': f"{last_name}{first_name}",
                                    'nickname': nickname,
                                    'first_name': first_name,
                                    'last_name': last_name
                                })
                    else:
                        fail_count += 1
                        if verbose:
                            print(f"  ✗ 创建失败: 未返回结果")
                
            except Exception as e:
                fail_count += 1
                if verbose:
                    print(f"  ✗ 操作失败: {e}")
            
            if verbose:
                print()
        
        # 返回统计信息
        stats = {
            'created': create_count,
            'updated': update_count,
            'failed': fail_count,
            'total': len(contacts_data)
        }
        
        if verbose:
            print("=" * 50)
            print(f"批量处理完成!")
            print(f"  新建: {create_count} 个")
            print(f"  更新: {update_count} 个")
            print(f"  失败: {fail_count} 个")
            print(f"  总计: {len(contacts_data)} 个")
            print("=" * 50)
        
        return stats


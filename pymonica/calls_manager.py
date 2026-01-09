"""
通话记录管理器类
负责处理联系人通话记录的增删改查操作
"""

from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime, date


class CallsManager:
    """
    通话记录管理器
    提供通话记录的增删改查功能
    """
    
    # 通话类型枚举
    CALL_TYPE_AUDIO = "audio"  # 音频通话
    CALL_TYPE_VIDEO = "video"  # 视频通话
    
    # 发起人枚举
    WHO_INITIATED_ME = "me"  # 我发起的
    WHO_INITIATED_CONTACT = "contact"  # 联系人发起的
    
    def __init__(self, client):
        """
        初始化通话记录管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create(self, vault_id: str, contact_id: str,
                    who_initiated: str = WHO_INITIATED_ME,
                    called_at: str = "",
                    call_reason_id: int = 0,
                    description: str = "",
                    emotion_id: int = 0,
                    call_type: str = CALL_TYPE_AUDIO) -> Optional[Dict[str, Any]]:
        """
        创建通话记录
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/calls
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            who_initiated: 发起人（可选，默认="me"）
                - "me": 我发起的
                - "contact": 联系人发起的
            called_at: 通话日期，格式 "YYYY-MM-DD"（必填，例如 "2026-01-09"）
            call_reason_id: 通话原因 ID（可选，默认=0）
            description: 描述（可选，默认=""）
            emotion_id: 情绪 ID（可选，默认=0）
            call_type: 通话类型（可选，默认="audio"）
                - "audio": 音频通话
                - "video": 视频通话
        
        Returns:
            包含创建结果的字典，格式与请求 payload 相同
        """
        # 确保日期格式为 YYYY-MM-DD
        if called_at and len(called_at) == 10 and called_at.count('-') == 2:
            # 日期格式已经是 YYYY-MM-DD，直接使用
            formatted_date = called_at
        elif called_at:
            # 尝试解析其他格式的日期
            from datetime import datetime
            try:
                # 尝试解析常见日期格式
                dt = datetime.strptime(called_at, "%Y-%m-%d")
                formatted_date = dt.strftime("%Y-%m-%d")
            except ValueError:
                # 如果解析失败，使用原始值
                formatted_date = called_at
        else:
            formatted_date = ""
        
        data = {
            "who_initiated": who_initiated,
            "called_at": formatted_date,
            "call_reason_id": call_reason_id,
            "description": description,
            "emotion_id": emotion_id,
            "type": call_type,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/calls', data=data)
    
    async def list(self, vault_id: str, contact_id: str) -> Optional[List[Dict[str, Any]]]:
        """
        获取通话记录列表
        注意：Monica API 不直接支持 GET /vaults/{vault}/contacts/{contact}/calls
        此方法通过获取联系人的 information tab 页面来提取通话记录信息
        
        根据 getInformation.md，calls 信息在 /tabs/information 端点的响应中
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            通话记录列表，如果获取失败则返回 None
        """
        # 使用统一的联系人信息提取器
        calls = await self.client.contact_info.get_calls(vault_id, contact_id)
        return calls if calls else None
    
    def _extract_calls_from_contact_detail(self, contact_detail: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        从联系人详情中提取通话记录
        
        根据 getInformation.md 中的响应结构，calls 信息在 modules 数组中，
        找到 type 为 "calls" 的模块，然后从该模块的 data.calls 中获取通话记录列表。
        
        Args:
            contact_detail: 联系人详情字典（从 HTML 解析得到）
        
        Returns:
            通话记录列表
        """
        calls = []
        
        # 根据实际响应结构，calls 在 modules 数组中
        # 路径：props.data.modules -> 找到 type="calls" 的模块 -> data.calls
        try:
            if 'props' in contact_detail and 'data' in contact_detail['props']:
                data = contact_detail['props']['data']
                
                # 查找 modules 数组
                if 'modules' in data and isinstance(data['modules'], list):
                    for module in data['modules']:
                        if isinstance(module, dict) and module.get('type') == 'calls':
                            # 找到 calls 模块
                            module_data = module.get('data', {})
                            if isinstance(module_data, dict) and 'calls' in module_data:
                                calls_list = module_data['calls']
                                if isinstance(calls_list, list):
                                    calls = calls_list
                                    break
                
                # 备用路径：直接查找 data.calls
                if not calls and 'calls' in data:
                    calls_data = data['calls']
                    if isinstance(calls_data, list):
                        calls = calls_data
                    elif isinstance(calls_data, dict) and 'calls' in calls_data:
                        calls = calls_data['calls'] if isinstance(calls_data['calls'], list) else []
            
            # 备用路径：直接从 data 中查找
            elif 'data' in contact_detail:
                data = contact_detail['data']
                
                # 查找 modules 数组
                if 'modules' in data and isinstance(data['modules'], list):
                    for module in data['modules']:
                        if isinstance(module, dict) and module.get('type') == 'calls':
                            module_data = module.get('data', {})
                            if isinstance(module_data, dict) and 'calls' in module_data:
                                calls_list = module_data['calls']
                                if isinstance(calls_list, list):
                                    calls = calls_list
                                    break
                
                # 直接查找 calls
                if not calls and 'calls' in data:
                    calls_data = data['calls']
                    if isinstance(calls_data, list):
                        calls = calls_data
        
        except Exception as e:
            # 如果提取失败，返回空列表
            print(f"提取通话记录时出错: {e}")
            calls = []
        
        return calls if isinstance(calls, list) else []
    
    async def get(self, vault_id: str, contact_id: str, call_id: str) -> Optional[Dict[str, Any]]:
        """
        获取单个通话记录
        注意：Monica API 不直接支持 GET /vaults/{vault}/contacts/{contact}/calls/{call}
        此方法通过获取联系人详情页面来查找指定的通话记录
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            call_id: 通话记录 ID（必填，可以是数字 ID 或字符串 ID）
        
        Returns:
            包含通话记录详情的字典，如果未找到则返回 None
        """
        # 获取所有通话记录
        calls = await self.list(vault_id, contact_id)
        
        if not calls:
            return None
        
        # 查找指定 ID 的通话记录
        call_id_str = str(call_id)
        for call in calls:
            # 尝试不同的 ID 字段名
            if str(call.get('id', '')) == call_id_str:
                return call
        
        return None
    
    async def update(self, vault_id: str, contact_id: str, call_id: str,
                    who_initiated: str,
                    called_at: str,
                    call_reason_id: int,
                    description: str = "",
                    emotion_id: int = 0,
                    call_type: str = CALL_TYPE_AUDIO) -> Optional[Dict[str, Any]]:
        """
        更新通话记录
        根据协议文档：PUT /vaults/{vault}/contacts/{contact}/calls/{call}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            call_id: 通话记录 ID（必填）
            who_initiated: 发起人（必填，"me" 或 "contact"）
            called_at: 通话日期，格式 "YYYY-MM-DD"（必填，例如 "2026-01-09"）
            call_reason_id: 通话原因 ID（必填）
            description: 描述（可选，默认=""）
            emotion_id: 情绪 ID（可选，默认=0）
            call_type: 通话类型（可选，默认="audio"）
        
        Returns:
            更新后的通话记录信息
        """
        # 处理日期格式
        if called_at and len(called_at) == 10 and called_at.count('-') == 2:
            formatted_date = called_at
        elif called_at:
            from datetime import datetime
            try:
                dt = datetime.strptime(called_at, "%Y-%m-%d")
                formatted_date = dt.strftime("%Y-%m-%d")
            except ValueError:
                formatted_date = called_at
        else:
            formatted_date = ""
        
        # 构建更新数据
        data = {
            "who_initiated": who_initiated,
            "called_at": formatted_date,
            "call_reason_id": call_reason_id,
            "description": description,
            "emotion_id": emotion_id,
            "type": call_type,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/calls/{call_id}', data=data)
    
    async def delete(self, vault_id: str, contact_id: str, call_id: str) -> Optional[Dict[str, Any]]:
        """
        删除通话记录
        根据协议文档：DELETE /vaults/{vault}/contacts/{contact}/calls/{call}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            call_id: 通话记录 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/calls/{call_id}')
    
    async def get_last_call(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        获取最后一次通话记录
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            最后一次通话记录的字典，如果没有通话记录则返回 None
        """
        calls = await self.list(vault_id, contact_id)
        
        if not calls or len(calls) == 0:
            return None
        
        # 返回第一条记录（通常是最新的）
        return calls[0]
    
    def _parse_call_date(self, called_at: str) -> Optional[date]:
        """
        解析通话日期字符串
        
        支持的格式：
        - "YYYY-MM-DD" (例如 "2026-01-09")
        - "MMM DD, YYYY" (例如 "Jan 09, 2026")
        - "M月 DD, YYYY" (例如 "1月 09, 2026")
        
        Args:
            called_at: 日期字符串
        
        Returns:
            date 对象，如果解析失败则返回 None
        """
        if not called_at:
            return None
        
        # 尝试解析 "YYYY-MM-DD" 格式
        try:
            return datetime.strptime(called_at, "%Y-%m-%d").date()
        except ValueError:
            pass
        
        # 尝试解析 "MMM DD, YYYY" 格式（例如 "Jan 09, 2026"）
        try:
            return datetime.strptime(called_at, "%b %d, %Y").date()
        except ValueError:
            pass
        
        # 尝试解析中文格式 "M月 DD, YYYY"（例如 "1月 09, 2026"）
        try:
            # 替换中文月份
            month_map = {
                '1月': 'Jan', '2月': 'Feb', '3月': 'Mar', '4月': 'Apr',
                '5月': 'May', '6月': 'Jun', '7月': 'Jul', '8月': 'Aug',
                '9月': 'Sep', '10月': 'Oct', '11月': 'Nov', '12月': 'Dec'
            }
            for cn_month, en_month in month_map.items():
                if cn_month in called_at:
                    called_at_en = called_at.replace(cn_month, en_month)
                    return datetime.strptime(called_at_en, "%b %d, %Y").date()
        except ValueError:
            pass
        
        return None
    
    def _calculate_days_since(self, call_date: date) -> int:
        """
        计算从指定日期到现在经过的天数
        
        Args:
            call_date: 通话日期
        
        Returns:
            经过的天数（如果 call_date 是未来日期，返回负数）
        """
        today = date.today()
        delta = today - call_date
        return delta.days
    
    async def get_time_since_last_call(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        获取上次通话到现在的时间间隔
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            包含时间间隔信息的字典，格式：
            {
                "last_call": {...},  # 最后一次通话记录
                "days_since": 5,     # 距离今天的天数
                "weeks_since": 0,    # 距离今天的周数
                "months_since": 0,   # 距离今天的月数
                "years_since": 0,    # 距离今天的年数
                "formatted": "5天前" # 格式化的时间描述
            }
            如果没有通话记录则返回 None
        """
        last_call = await self.get_last_call(vault_id, contact_id)
        
        if not last_call:
            return None
        
        called_at_str = last_call.get('called_at', '')
        call_date = self._parse_call_date(called_at_str)
        
        if not call_date:
            # 如果无法解析日期，返回基本信息
            return {
                "last_call": last_call,
                "days_since": None,
                "weeks_since": None,
                "months_since": None,
                "years_since": None,
                "formatted": "无法解析日期",
                "raw_date": called_at_str
            }
        
        days_since = self._calculate_days_since(call_date)
        weeks_since = days_since // 7
        months_since = days_since // 30
        years_since = days_since // 365
        
        # 格式化时间描述
        if days_since < 0:
            formatted = f"{abs(days_since)}天后"
        elif days_since == 0:
            formatted = "今天"
        elif days_since == 1:
            formatted = "昨天"
        elif days_since < 7:
            formatted = f"{days_since}天前"
        elif days_since < 30:
            formatted = f"{weeks_since}周前"
        elif days_since < 365:
            formatted = f"{months_since}个月前"
        else:
            formatted = f"{years_since}年前"
        
        return {
            "last_call": last_call,
            "days_since": days_since,
            "weeks_since": weeks_since,
            "months_since": months_since,
            "years_since": years_since,
            "formatted": formatted,
            "call_date": call_date.isoformat() if call_date else None
        }
    
    async def get_last_call_with_interval(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        获取最后一次通话记录和时间间隔（便捷方法）
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            包含最后一次通话记录和时间间隔信息的字典
        """
        return await self.get_time_since_last_call(vault_id, contact_id)
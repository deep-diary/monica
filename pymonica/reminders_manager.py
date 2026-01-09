"""
提醒事项管理器类
负责处理联系人提醒事项的增删改查操作
"""

from typing import Optional, Dict, Any, List


class RemindersManager:
    """
    提醒事项管理器
    提供提醒事项的增删改查功能
    """
    
    # 提醒类型枚举
    REMINDER_CHOICE_ONE_TIME = "one_time"  # 一次性提醒
    REMINDER_CHOICE_RECURRING = "recurring"  # 重复提醒
    
    # 日期选择类型枚举
    CHOICE_FULL_DATE = "full_date"  # 完整日期
    CHOICE_MONTH_DAY = "month_day"  # 月日
    
    # 频率类型枚举
    FREQUENCY_TYPE_RECURRING_YEAR = "recurring_year"  # 每年重复
    FREQUENCY_TYPE_RECURRING_MONTH = "recurring_month"  # 每月重复
    FREQUENCY_TYPE_RECURRING_WEEK = "recurring_week"  # 每周重复
    FREQUENCY_TYPE_RECURRING_DAY = "recurring_day"  # 每天重复
    
    def __init__(self, client):
        """
        初始化提醒事项管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create(self, vault_id: str, contact_id: str,
                    label: str,
                    reminder_choice: str = REMINDER_CHOICE_ONE_TIME,
                    day: str = "",
                    month: str = "",
                    choice: str = CHOICE_FULL_DATE,
                    date: str = "",
                    frequency_type: str = FREQUENCY_TYPE_RECURRING_YEAR,
                    frequency_number: int = 1) -> Optional[Dict[str, Any]]:
        """
        创建提醒事项
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/reminders
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            label: 提醒标签（必填）
            reminder_choice: 提醒类型（可选，默认="one_time"）
                - "one_time": 一次性提醒
                - "recurring": 重复提醒
            day: 日期中的天数（可选，默认=""）
            month: 日期中的月份（可选，默认=""）
            choice: 日期选择类型（可选，默认="full_date"）
                - "full_date": 完整日期
                - "month_day": 月日
            date: 日期，格式 "YYYY-MM-DD"（可选，例如 "2026-01-09"）
            frequency_type: 频率类型（可选，默认="recurring_year"）
                - "recurring_year": 每年重复
                - "recurring_month": 每月重复
                - "recurring_week": 每周重复
                - "recurring_day": 每天重复
            frequency_number: 频率数字（可选，默认=1）
        
        Returns:
            包含创建结果的字典，格式与请求 payload 相同
        """
        data = {
            "label": label,
            "reminderChoice": reminder_choice,
            "day": day,
            "month": month,
            "choice": choice,
            "date": date,
            "frequencyType": frequency_type,
            "frequencyNumber": frequency_number,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/reminders', data=data)
    
    async def list(self, vault_id: str, contact_id: str) -> Optional[List[Dict[str, Any]]]:
        """
        获取提醒事项列表
        注意：Monica API 不直接支持 GET /vaults/{vault}/contacts/{contact}/reminders
        此方法通过获取联系人的 information tab 页面来提取提醒事项信息
        
        根据 getInformation.md，reminders 信息在 /tabs/information 端点的响应中
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            提醒事项列表，如果获取失败则返回 None
        """
        # 使用统一的联系人信息提取器
        reminders = await self.client.contact_info.get_reminders(vault_id, contact_id)
        return reminders if reminders else None
    
    def _extract_reminders_from_contact_detail(self, contact_detail: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        从联系人详情中提取提醒事项
        
        根据 getInformation.md 中的响应结构，reminders 信息在 modules 数组中，
        找到 type 为 "reminders" 的模块，然后从该模块的 data.reminders 中获取提醒事项列表。
        
        Args:
            contact_detail: 联系人详情字典（从 HTML 解析得到）
        
        Returns:
            提醒事项列表
        """
        reminders = []
        
        # 根据实际响应结构，reminders 在 modules 数组中
        # 路径：props.data.modules -> 找到 type="reminders" 的模块 -> data.reminders
        try:
            if 'props' in contact_detail and 'data' in contact_detail['props']:
                data = contact_detail['props']['data']
                
                # 查找 modules 数组
                if 'modules' in data and isinstance(data['modules'], list):
                    for module in data['modules']:
                        if isinstance(module, dict) and module.get('type') == 'reminders':
                            # 找到 reminders 模块
                            module_data = module.get('data', {})
                            if isinstance(module_data, dict) and 'reminders' in module_data:
                                reminders_list = module_data['reminders']
                                if isinstance(reminders_list, list):
                                    reminders = reminders_list
                                    break
                
                # 备用路径：直接查找 data.reminders
                if not reminders and 'reminders' in data:
                    reminders_data = data['reminders']
                    if isinstance(reminders_data, list):
                        reminders = reminders_data
                    elif isinstance(reminders_data, dict) and 'reminders' in reminders_data:
                        reminders = reminders_data['reminders'] if isinstance(reminders_data['reminders'], list) else []
            
            # 备用路径：直接从 data 中查找
            elif 'data' in contact_detail:
                data = contact_detail['data']
                
                # 查找 modules 数组
                if 'modules' in data and isinstance(data['modules'], list):
                    for module in data['modules']:
                        if isinstance(module, dict) and module.get('type') == 'reminders':
                            module_data = module.get('data', {})
                            if isinstance(module_data, dict) and 'reminders' in module_data:
                                reminders_list = module_data['reminders']
                                if isinstance(reminders_list, list):
                                    reminders = reminders_list
                                    break
                
                # 直接查找 reminders
                if not reminders and 'reminders' in data:
                    reminders_data = data['reminders']
                    if isinstance(reminders_data, list):
                        reminders = reminders_data
        
        except Exception as e:
            # 如果提取失败，返回空列表
            print(f"提取提醒事项时出错: {e}")
            reminders = []
        
        return reminders if isinstance(reminders, list) else []
    
    async def get(self, vault_id: str, contact_id: str, reminder_id: str) -> Optional[Dict[str, Any]]:
        """
        获取单个提醒事项
        注意：Monica API 不直接支持 GET /vaults/{vault}/contacts/{contact}/reminders/{reminder}
        此方法通过获取联系人详情页面来查找指定的提醒事项
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            reminder_id: 提醒事项 ID（必填，可以是数字 ID 或字符串 ID）
        
        Returns:
            包含提醒事项详情的字典，如果未找到则返回 None
        """
        # 获取所有提醒事项
        reminders = await self.list(vault_id, contact_id)
        
        if not reminders:
            return None
        
        # 查找指定 ID 的提醒事项
        reminder_id_str = str(reminder_id)
        for reminder in reminders:
            # 尝试不同的 ID 字段名
            if str(reminder.get('id', '')) == reminder_id_str:
                return reminder
        
        return None
    
    async def update(self, vault_id: str, contact_id: str, reminder_id: str,
                    label: str,
                    reminder_choice: str,
                    day: str = "",
                    month: str = "",
                    choice: str = CHOICE_FULL_DATE,
                    date: str = "",
                    frequency_type: str = FREQUENCY_TYPE_RECURRING_YEAR,
                    frequency_number: int = 1) -> Optional[Dict[str, Any]]:
        """
        更新提醒事项
        根据协议文档：PUT /vaults/{vault}/contacts/{contact}/reminders/{reminder}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            reminder_id: 提醒事项 ID（必填）
            label: 提醒标签（必填）
            reminder_choice: 提醒类型（必填，"one_time" 或 "recurring"）
            day: 日期中的天数（可选，默认=""）
            month: 日期中的月份（可选，默认=""）
            choice: 日期选择类型（可选，默认="full_date"）
            date: 日期，格式 "YYYY-MM-DD"（可选，例如 "2026-01-09"）
            frequency_type: 频率类型（可选，默认="recurring_year"）
            frequency_number: 频率数字（可选，默认=1）
        
        Returns:
            更新后的提醒事项信息
        """
        # 构建更新数据
        data = {
            "label": label,
            "reminderChoice": reminder_choice,
            "day": day,
            "month": month,
            "choice": choice,
            "date": date,
            "frequencyType": frequency_type,
            "frequencyNumber": frequency_number,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/reminders/{reminder_id}', data=data)
    
    async def delete(self, vault_id: str, contact_id: str, reminder_id: str) -> Optional[Dict[str, Any]]:
        """
        删除提醒事项
        根据协议文档：DELETE /vaults/{vault}/contacts/{contact}/reminders/{reminder}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            reminder_id: 提醒事项 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/reminders/{reminder_id}')

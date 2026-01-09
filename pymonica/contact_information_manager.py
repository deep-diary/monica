"""
联系人信息管理器类
负责处理联系人信息（邮箱、电话等）的增删改查操作
"""

from typing import Optional, Dict, Any


class ContactInformationManager:
    """
    联系人信息管理器
    提供联系人信息的增删改查功能
    """
    
    def __init__(self, client):
        """
        初始化联系人信息管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create_email(self, vault_id: str, contact_id: str, email: str) -> Optional[Dict[str, Any]]:
        """
        创建邮箱信息
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/contactInformation
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            email: 邮箱地址（必填）
        
        Returns:
            包含创建结果的字典，格式: {'data': {'id': ..., 'data': ..., 'contact_information_type': {...}}}
        """
        data = {
            "data": email,
            "contact_information_type_id": 1,  # 1 = 电子邮件地址
            "errors": []
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/contactInformation', data=data)
    
    async def create_phone(self, vault_id: str, contact_id: str, phone: str) -> Optional[Dict[str, Any]]:
        """
        创建电话信息
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/contactInformation
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            phone: 电话号码（必填）
        
        Returns:
            包含创建结果的字典，格式: {'data': {'id': ..., 'data': ..., 'contact_information_type': {...}}}
        """
        data = {
            "data": phone,
            "contact_information_type_id": 2,  # 2 = 电话
            "errors": []
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/contactInformation', data=data)
    
    async def create(self, vault_id: str, contact_id: str, data_value: str, contact_information_type_id: int) -> Optional[Dict[str, Any]]:
        """
        创建联系人信息（通用方法）
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/contactInformation
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            data_value: 信息内容（必填，如邮箱或电话）
            contact_information_type_id: 信息类型 ID（必填，1=邮箱, 2=电话）
        
        Returns:
            包含创建结果的字典
        """
        data = {
            "data": data_value,
            "contact_information_type_id": contact_information_type_id,
            "errors": []
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/contactInformation', data=data)
    
    async def update(self, vault_id: str, contact_id: str, contact_information_id: str, 
                    data_value: str, contact_information_type_id: int) -> Optional[Dict[str, Any]]:
        """
        更新联系人信息
        根据协议文档：PUT /vaults/{vault}/contacts/{contact}/contactInformation/{contactInformation}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            contact_information_id: 联系人信息 ID（必填）
            data_value: 新的信息内容（必填）
            contact_information_type_id: 信息类型 ID（必填，1=邮箱, 2=电话）
        
        Returns:
            更新后的联系人信息
        """
        data = {
            "data": data_value,
            "contact_information_type_id": contact_information_type_id,
            "errors": []
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/contactInformation/{contact_information_id}', data=data)
    
    async def update_email(self, vault_id: str, contact_id: str, contact_information_id: str, email: str) -> Optional[Dict[str, Any]]:
        """
        更新邮箱信息（便捷方法）
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            contact_information_id: 联系人信息 ID（必填）
            email: 新的邮箱地址（必填）
        
        Returns:
            更新后的联系人信息
        """
        return await self.update(vault_id, contact_id, contact_information_id, email, 1)
    
    async def update_phone(self, vault_id: str, contact_id: str, contact_information_id: str, phone: str) -> Optional[Dict[str, Any]]:
        """
        更新电话信息（便捷方法）
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            contact_information_id: 联系人信息 ID（必填）
            phone: 新的电话号码（必填）
        
        Returns:
            更新后的联系人信息
        """
        return await self.update(vault_id, contact_id, contact_information_id, phone, 2)
    
    async def delete(self, vault_id: str, contact_id: str, contact_information_id: str) -> Optional[Dict[str, Any]]:
        """
        删除联系人信息
        根据协议文档：DELETE /vaults/{vault}/contacts/{contact}/contactInformation/{contactInformation}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            contact_information_id: 联系人信息 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/contactInformation/{contact_information_id}')

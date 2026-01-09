"""
地址管理器类
负责处理联系人地址的增删改查操作
"""

from typing import Optional, Dict, Any


class AddressManager:
    """
    地址管理器
    提供地址的增删改查功能
    """
    
    # 地址类型枚举
    ADDRESS_TYPE_HOME = 1  # 主页
    ADDRESS_TYPE_SECONDARY = 2  # 第二居所
    ADDRESS_TYPE_WORK = 3  # 工作
    ADDRESS_TYPE_CABIN = 4  # 小木屋
    ADDRESS_TYPE_OTHER = 5  # 其他
    
    def __init__(self, client):
        """
        初始化地址管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create(self, vault_id: str, contact_id: str, 
                    line_1: str, city: str, province: str, country: str,
                    address_type_id: int = ADDRESS_TYPE_HOME,
                    line_2: str = "", postal_code: str = "",
                    existing_address: bool = False, existing_address_id: int = 0,
                    is_past_address: bool = False) -> Optional[Dict[str, Any]]:
        """
        创建地址
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/addresses
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            line_1: 地址第一行（必填）
            city: 城市（必填）
            province: 省份/州（必填）
            country: 国家（必填）
            address_type_id: 地址类型 ID（可选，默认=1主页）
                - 1: 主页
                - 2: 第二居所
                - 3: 工作
                - 4: 小木屋
                - 5: 其他
            line_2: 地址第二行（可选）
            postal_code: 邮政编码（可选）
            existing_address: 是否使用现有地址（可选，默认=False）
            existing_address_id: 现有地址 ID（可选，默认=0）
            is_past_address: 是否为过去地址（可选，默认=False）
        
        Returns:
            包含创建结果的字典，格式: {'data': {'id': ..., 'line_1': ..., 'type': {...}}}
        """
        data = {
            "existing_address": existing_address,
            "existing_address_id": existing_address_id,
            "type": "",
            "address_type_id": address_type_id,
            "is_past_address": is_past_address,
            "line_1": line_1,
            "line_2": line_2,
            "city": city,
            "province": province,
            "postal_code": postal_code,
            "country": country,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/addresses', data=data)
    
    async def update(self, vault_id: str, contact_id: str, address_id: str,
                    line_1: str, city: str, province: str, country: str,
                    address_type_id: int = ADDRESS_TYPE_HOME,
                    line_2: str = None, postal_code: str = None,
                    is_past_address: bool = False,
                    existing_address: bool = False, existing_address_id: int = 0) -> Optional[Dict[str, Any]]:
        """
        更新地址
        根据协议文档：PUT /vaults/{vault}/contacts/{contact}/addresses/{address}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            address_id: 地址 ID（必填）
            line_1: 地址第一行（必填）
            city: 城市（必填）
            province: 省份/州（必填）
            country: 国家（必填）
            address_type_id: 地址类型 ID（可选，默认=1主页）
            line_2: 地址第二行（可选，None 时发送 null）
            postal_code: 邮政编码（可选，None 时发送 null）
            is_past_address: 是否为过去地址（可选，默认=False）
            existing_address: 是否使用现有地址（可选，默认=False）
            existing_address_id: 现有地址 ID（可选，默认=0）
        
        Returns:
            更新后的地址信息
        """
        data = {
            "existing_address": existing_address,
            "existing_address_id": existing_address_id,
            "type": "",
            "address_type_id": address_type_id,
            "is_past_address": is_past_address,
            "line_1": line_1,
            "line_2": line_2 if line_2 is not None else None,
            "city": city,
            "province": province,
            "postal_code": postal_code if postal_code is not None else None,
            "country": country,
            "errors": [],
            "isDirty": True,
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/addresses/{address_id}', data=data)
    
    async def delete(self, vault_id: str, contact_id: str, address_id: str) -> Optional[Dict[str, Any]]:
        """
        删除地址
        根据协议文档：DELETE /vaults/{vault}/contacts/{contact}/addresses/{address}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            address_id: 地址 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/addresses/{address_id}')

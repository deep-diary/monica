"""
QuickFact 管理器类
负责处理联系人快速事实（Quick Facts）的增删改查操作
"""

from typing import Optional, Dict, Any, List


class QuickFactManager:
    """
    QuickFact 管理器
    提供快速事实的增删改查功能
    """
    
    def __init__(self, client):
        """
        初始化 QuickFact 管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create(self, vault_id: str, contact_id: str, template_id: str, content: str) -> Optional[Dict[str, Any]]:
        """
        创建快速事实
        根据 Monica 路由文件：POST /vaults/{vault}/contacts/{contact}/quickFacts/{template}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            template_id: 模板 ID（必填，例如：1=兴趣爱好, 2=食物偏好, 3=资源, 4=需求）
            content: 快速事实内容（必填）
        
        Returns:
            包含创建结果的字典，格式: {'data': {'id': ..., 'content': ..., 'url': {...}}}
        """
        data = {
            "content": content,
            "isDirty": True,
            "errors": {},
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/{template_id}', data=data)
    
    async def get(self, vault_id: str, contact_id: str, template_id: str) -> Optional[Dict[str, Any]]:
        """
        获取联系人的快速事实
        根据 Monica 路由文件：GET /vaults/{vault}/contacts/{contact}/quickFacts/{template}
        
        注意：此端点可能返回 HTML 或 JSON，本方法会尝试解析 HTML 中的 JSON 数据。
        如果无法解析，将返回原始响应。
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            template_id: 模板 ID（必填）
        
        Returns:
            包含快速事实信息的字典，如果解析失败则返回 None
        """
        # 先尝试 HTML 解析（静默模式，避免不必要的警告）
        result = await self.client._request('GET', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/{template_id}', parse_html=True, silent=True)
        
        # 如果 HTML 解析失败，尝试直接返回 JSON（如果响应是 JSON）
        if result is None:
            # 尝试不使用 HTML 解析
            result = await self.client._request('GET', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/{template_id}', parse_html=False, silent=True)
        
        return result
    
    async def update(self, vault_id: str, contact_id: str, template_id: str, quick_fact_id: str, content: str) -> Optional[Dict[str, Any]]:
        """
        更新快速事实
        根据 Monica 路由文件：PUT /vaults/{vault}/contacts/{contact}/quickFacts/{template}/{quickFact}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            template_id: 模板 ID（必填）
            quick_fact_id: 快速事实 ID（必填）
            content: 新的内容（必填）
        
        Returns:
            更新后的快速事实信息
        """
        data = {
            "content": content,
            "isDirty": True,
            "errors": {},
            "hasErrors": False,
            "processing": False,
            "progress": None,
            "wasSuccessful": False,
            "recentlySuccessful": False,
            "__rememberable": True
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/{template_id}/{quick_fact_id}', data=data)
    
    async def delete(self, vault_id: str, contact_id: str, template_id: str, quick_fact_id: str) -> Optional[Dict[str, Any]]:
        """
        删除快速事实
        根据 Monica 路由文件：DELETE /vaults/{vault}/contacts/{contact}/quickFacts/{template}/{quickFact}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            template_id: 模板 ID（必填）
            quick_fact_id: 快速事实 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/{template_id}/{quick_fact_id}')
    
    async def toggle(self, vault_id: str, contact_id: str) -> Optional[Dict[str, Any]]:
        """
        切换快速事实的显示状态
        根据 Monica 路由文件：PUT /vaults/{vault}/contacts/{contact}/quickFacts/toggle
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            切换结果
        """
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/quickFacts/toggle')


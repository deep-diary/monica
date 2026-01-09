"""
笔记管理器类
负责处理联系人笔记的增删改查操作
"""

from typing import Optional, Dict, Any, List


class NotesManager:
    """
    笔记管理器
    提供笔记的增删改查功能
    """
    
    def __init__(self, client):
        """
        初始化笔记管理器
        
        Args:
            client: MonicaClient 实例
        """
        self.client = client
    
    async def create(self, vault_id: str, contact_id: str,
                    title: str,
                    body: str = "",
                    emotion: int = 0) -> Optional[Dict[str, Any]]:
        """
        创建笔记
        根据协议文档：POST /vaults/{vault}/contacts/{contact}/notes
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            title: 笔记标题（必填）
            body: 笔记内容（可选，默认=""）
            emotion: 情绪 ID（可选，默认=0）
        
        Returns:
            包含创建结果的字典，格式: {'data': {...}}
        """
        data = {
            "title": title,
            "body": body,
            "emotion": emotion,
            "errors": []
        }
        
        return await self.client._request('POST', f'/vaults/{vault_id}/contacts/{contact_id}/notes', data=data)
    
    async def list(self, vault_id: str, contact_id: str) -> Optional[List[Dict[str, Any]]]:
        """
        获取笔记列表
        根据协议文档：GET /vaults/{vault}/contacts/{contact}/notes
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
        
        Returns:
            笔记列表，如果获取失败则返回 None
        """
        result = await self.client._request('GET', f'/vaults/{vault_id}/contacts/{contact_id}/notes')
        
        if not result:
            return None
        
        # 从响应中提取笔记列表
        # 根据 API 响应格式，可能是 {'data': [...]} 或直接是列表
        if isinstance(result, dict):
            if 'data' in result:
                notes = result['data']
                if isinstance(notes, list):
                    return notes
                elif isinstance(notes, dict) and 'notes' in notes:
                    return notes['notes'] if isinstance(notes['notes'], list) else []
            elif 'notes' in result:
                return result['notes'] if isinstance(result['notes'], list) else []
        elif isinstance(result, list):
            return result
        
        return []
    
    async def get(self, vault_id: str, contact_id: str, note_id: str) -> Optional[Dict[str, Any]]:
        """
        获取单个笔记
        注意：Monica API 可能不直接支持 GET /vaults/{vault}/contacts/{contact}/notes/{note}
        此方法通过获取笔记列表来查找指定的笔记
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            note_id: 笔记 ID（必填，可以是数字 ID 或字符串 ID）
        
        Returns:
            包含笔记详情的字典，如果未找到则返回 None
        """
        # 获取所有笔记
        notes = await self.list(vault_id, contact_id)
        
        if not notes:
            return None
        
        # 查找指定 ID 的笔记
        note_id_str = str(note_id)
        for note in notes:
            # 尝试不同的 ID 字段名
            if str(note.get('id', '')) == note_id_str:
                return note
        
        return None
    
    async def update(self, vault_id: str, contact_id: str, note_id: str,
                    title: str,
                    body: str = "",
                    emotion: int = 0) -> Optional[Dict[str, Any]]:
        """
        更新笔记
        根据协议文档：PUT /vaults/{vault}/contacts/{contact}/notes/{note}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            note_id: 笔记 ID（必填）
            title: 笔记标题（必填）
            body: 笔记内容（可选，默认=""）
            emotion: 情绪 ID（可选，默认=0）
        
        Returns:
            更新后的笔记信息
        """
        data = {
            "title": title,
            "body": body,
            "emotion": emotion,
            "errors": []
        }
        
        return await self.client._request('PUT', f'/vaults/{vault_id}/contacts/{contact_id}/notes/{note_id}', data=data)
    
    async def delete(self, vault_id: str, contact_id: str, note_id: str) -> Optional[Dict[str, Any]]:
        """
        删除笔记
        根据协议文档：DELETE /vaults/{vault}/contacts/{contact}/notes/{note}
        
        Args:
            vault_id: Vault ID（必填）
            contact_id: 联系人 ID（必填）
            note_id: 笔记 ID（必填）
        
        Returns:
            删除结果
        """
        return await self.client._request('DELETE', f'/vaults/{vault_id}/contacts/{contact_id}/notes/{note_id}')

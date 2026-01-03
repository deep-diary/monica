# PyMonica

Python client for Monica CRM API

## 安装

```bash
pip install -e .
```

## 使用示例

```python
from pymonica import MonicaClient

# 创建客户端
client = MonicaClient(
    token="your_api_token",
    base_url="http://localhost:8080"
)

# 获取用户信息
user = client.get_current_user()

# 获取 Vault 列表
vaults = client.get_vaults()

# 使用联系人管理器
vault_id = "your-vault-id"

# 获取联系人列表
contacts = client.contacts.list(vault_id)

# 创建联系人
new_contact = client.contacts.create(
    vault_id=vault_id,
    first_name="剑英",
    last_name="姚"
)

# 获取单个联系人
contact = client.contacts.get(vault_id, contact_id="contact-id")

# 更新联系人
client.contacts.update(
    vault_id=vault_id,
    contact_id="contact-id",
    first_name="新名字"
)

# 删除联系人
client.contacts.delete(vault_id, contact_id="contact-id")

# 搜索联系人
results = client.contacts.search(vault_id, query="搜索关键词")

# 使用 QuickFacts 管理器
contact_id = "contact-id"
template_id = "3"  # 1=兴趣爱好, 2=食物偏好, 3=资源, 4=需求

# 创建 QuickFact
quick_fact = client.quick_facts.create(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    content="擅长使用 Python 开发工具"
)

# 获取 QuickFact
quick_facts = client.quick_facts.get(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id
)

# 更新 QuickFact
client.quick_facts.update(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    quick_fact_id="quick-fact-id",
    content="更新的内容"
)

# 删除 QuickFact
client.quick_facts.delete(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    quick_fact_id="quick-fact-id"
)
```

## 功能

- ✅ 用户信息管理
- ✅ Vault 管理
- ✅ 联系人管理（增删改查）
- ✅ 联系人搜索
- ✅ QuickFacts 管理（增删改查）

## 注意事项

Monica 5.0.0-beta.5 版本的联系人 API 使用 Web 路由，返回 HTML 页面。
本库会自动解析 HTML 中的 JSON 数据。


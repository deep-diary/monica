# PyMonica

Python client for Monica CRM API

## 安装

```bash
pip install -e .
```

## 快速开始

```python
import asyncio
from pymonica import MonicaClient

async def main():
    # 创建客户端（使用异步上下文管理器）
    async with MonicaClient(
        token="your_api_token",
        base_url="http://localhost:8080"
    ) as client:
        # 获取用户信息
        user = await client.get_current_user()

        # 获取 Vault 列表
        vaults = await client.get_vaults()

        print(f"当前用户: {user}")
        print(f"Vaults: {vaults}")

asyncio.run(main())
```

## 功能模块

### 1. 联系人管理 (ContactManager)

```python
vault_id = "your-vault-id"
contact_id = "contact-id"

# 获取联系人列表
contacts = await client.contacts.list(vault_id, limit=25, page=1)

# 创建联系人
new_contact = await client.contacts.create(
    vault_id=vault_id,
    first_name="剑英",
    last_name="姚"
)

# 获取单个联系人
contact = await client.contacts.get(vault_id, contact_id)

# 更新联系人
await client.contacts.update(
    vault_id=vault_id,
    contact_id=contact_id,
    first_name="新名字"
)

# 删除联系人
await client.contacts.delete(vault_id, contact_id)

# 搜索联系人
results = await client.contacts.search(vault_id, query="搜索关键词")
```

### 2. QuickFacts 管理 (QuickFactManager)

```python
template_id = "13"  # 模板ID，如：13=兴趣爱好, 14=食物偏好

# 创建 QuickFact
quick_fact = await client.quick_facts.create(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    content="擅长使用 Python 开发工具"
)

# 获取 QuickFact
quick_facts = await client.quick_facts.get(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id
)

# 更新 QuickFact
await client.quick_facts.update(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    quick_fact_id="quick-fact-id",
    content="更新的内容"
)

# 删除 QuickFact
await client.quick_facts.delete(
    vault_id=vault_id,
    contact_id=contact_id,
    template_id=template_id,
    quick_fact_id="quick-fact-id"
)
```

### 3. 联系信息管理 (ContactInformationManager)

```python
# 创建邮箱
email = await client.contact_information.create_email(
    vault_id=vault_id,
    contact_id=contact_id,
    email="example@email.com"
)

# 创建电话
phone = await client.contact_information.create_phone(
    vault_id=vault_id,
    contact_id=contact_id,
    phone="13800138000"
)

# 更新联系信息
await client.contact_information.update(
    vault_id=vault_id,
    contact_id=contact_id,
    info_id="info-id",
    data="new-email@email.com"
)

# 删除联系信息
await client.contact_information.delete(
    vault_id=vault_id,
    contact_id=contact_id,
    info_id="info-id"
)
```

### 4. 地址管理 (AddressManager)

```python
# 创建地址
address = await client.addresses.create(
    vault_id=vault_id,
    contact_id=contact_id,
    line_1="北京市朝阳区",
    city="北京",
    province="北京市",
    country="中国",
    address_type_id=client.addresses.ADDRESS_TYPE_HOME,  # 1=主页, 2=第二居所, 3=工作, 4=小木屋, 5=其他
    postal_code="100000"
)

# 更新地址
await client.addresses.update(
    vault_id=vault_id,
    contact_id=contact_id,
    address_id="address-id",
    line_1="新地址",
    city="上海",
    province="上海市",
    country="中国"
)

# 删除地址
await client.addresses.delete(
    vault_id=vault_id,
    contact_id=contact_id,
    address_id="address-id"
)
```

### 5. 通话记录管理 (CallsManager)

```python
from datetime import datetime

# 创建通话记录
call = await client.calls.create(
    vault_id=vault_id,
    contact_id=contact_id,
    who_initiated=client.calls.WHO_INITIATED_ME,  # "me" 或 "contact"
    called_at="2026-01-09",  # YYYY-MM-DD 格式
    call_reason_id=5,
    description="讨论项目进展",
    emotion_id=3,
    call_type=client.calls.CALL_TYPE_AUDIO  # "audio" 或 "video"
)

# 获取通话记录列表
calls = await client.calls.list(vault_id, contact_id)

# 获取单个通话记录
call_detail = await client.calls.get(vault_id, contact_id, "call-id")

# 更新通话记录
await client.calls.update(
    vault_id=vault_id,
    contact_id=contact_id,
    call_id="call-id",
    who_initiated=client.calls.WHO_INITIATED_CONTACT,
    called_at="2026-01-10",
    call_reason_id=5,
    description="更新后的描述"
)

# 删除通话记录
await client.calls.delete(vault_id, contact_id, "call-id")

# 获取最后一次通话记录
last_call = await client.calls.get_last_call(vault_id, contact_id)

# 获取上次通话到现在的时间间隔
time_info = await client.calls.get_time_since_last_call(vault_id, contact_id)
# 返回: {"last_call": {...}, "days_since": 5, "formatted": "5天前", ...}
```

### 6. 笔记管理 (NotesManager)

```python
# 创建笔记
note = await client.notes.create(
    vault_id=vault_id,
    contact_id=contact_id,
    title="会议记录",
    body="讨论了项目进展和下一步计划",
    emotion=3
)

# 获取笔记列表
notes = await client.notes.list(vault_id, contact_id)

# 获取单个笔记
note_detail = await client.notes.get(vault_id, contact_id, "note-id")

# 更新笔记
await client.notes.update(
    vault_id=vault_id,
    contact_id=contact_id,
    note_id="note-id",
    title="更新的标题",
    body="更新的内容"
)

# 删除笔记
await client.notes.delete(vault_id, contact_id, "note-id")
```

### 7. 提醒事项管理 (RemindersManager)

```python
# 创建提醒事项
reminder = await client.reminders.create(
    vault_id=vault_id,
    contact_id=contact_id,
    label="生日提醒",
    reminder_choice=client.reminders.REMINDER_CHOICE_ONE_TIME,  # "one_time" 或 "recurring"
    choice=client.reminders.CHOICE_FULL_DATE,  # "full_date" 或 "month_day"
    date="2026-01-09",  # YYYY-MM-DD 格式
    frequency_type=client.reminders.FREQUENCY_TYPE_RECURRING_YEAR,  # 频率类型
    frequency_number=1
)

# 获取提醒事项列表
reminders = await client.reminders.list(vault_id, contact_id)

# 获取单个提醒事项
reminder_detail = await client.reminders.get(vault_id, contact_id, "reminder-id")

# 更新提醒事项
await client.reminders.update(
    vault_id=vault_id,
    contact_id=contact_id,
    reminder_id="reminder-id",
    label="更新的提醒",
    reminder_choice=client.reminders.REMINDER_CHOICE_RECURRING,
    date="2026-01-10"
)

# 删除提醒事项
await client.reminders.delete(vault_id, contact_id, "reminder-id")
```

### 8. 联系人信息提取器 (ContactInformationExtractor)

统一从联系人详情页面获取所有信息，支持缓存机制：

```python
# 获取完整的联系人详情信息
full_info = await client.contact_info.get_full_information(vault_id, contact_id)

# 获取联系人ID和名称
contact_id_extracted = client.contact_info.get_contact_id(full_info)
contact_name = client.contact_info.get_contact_name(full_info)

# 获取所有信息并以JSON格式返回
all_info_json = await client.contact_info.get_all_information_as_json(
    vault_id,
    contact_id,
    indent=2  # JSON缩进
)
print(all_info_json)

# 单独获取各类信息（使用缓存）
calls = await client.contact_info.get_calls(vault_id, contact_id)
reminders = await client.contact_info.get_reminders(vault_id, contact_id)
notes = await client.contact_info.get_notes(vault_id, contact_id)
addresses = await client.contact_info.get_addresses(vault_id, contact_id)
contact_info_list = await client.contact_info.get_contact_information(vault_id, contact_id)
dates = await client.contact_info.get_dates(vault_id, contact_id)  # 重要的日子（生日、纪念日等）
quick_facts = await client.contact_info.get_quick_facts(vault_id, contact_id)
quick_facts_list = await client.contact_info.get_quick_facts_list(vault_id, contact_id)

# 获取所有模块的数据
all_modules = await client.contact_info.get_all_modules(vault_id, contact_id)

# 清除缓存
client.contact_info.clear_cache()
```

## 完整示例

```python
import asyncio
from pymonica import MonicaClient

async def main():
    async with MonicaClient(
        token="your_api_token",
        base_url="http://localhost:8080"
    ) as client:
        vault_id = "your-vault-id"
        contact_id = "contact-id"

        # 获取所有联系人信息（JSON格式）
        all_info = await client.contact_info.get_all_information_as_json(
            vault_id,
            contact_id
        )
        print(all_info)

        # 创建新的通话记录
        await client.calls.create(
            vault_id=vault_id,
            contact_id=contact_id,
            who_initiated=client.calls.WHO_INITIATED_ME,
            called_at="2026-01-09",
            call_reason_id=5,
            call_type=client.calls.CALL_TYPE_AUDIO
        )

        # 创建提醒事项
        await client.reminders.create(
            vault_id=vault_id,
            contact_id=contact_id,
            label="生日",
            date="2026-01-02",
            reminder_choice=client.reminders.REMINDER_CHOICE_ONE_TIME
        )

asyncio.run(main())
```

## 功能列表

- ✅ 用户信息管理
- ✅ Vault 管理
- ✅ 联系人管理（增删改查、搜索）
- ✅ QuickFacts 管理（增删改查）
- ✅ 联系信息管理（邮箱、电话等）
- ✅ 地址管理（增删改查）
- ✅ 通话记录管理（增删改查、时间间隔计算）
- ✅ 笔记管理（增删改查）
- ✅ 提醒事项管理（增删改查）
- ✅ 联系人信息提取器（统一获取所有信息，支持缓存）

## 注意事项

1. **异步操作**: 所有 API 方法都是异步的，需要使用 `async/await` 语法
2. **上下文管理器**: 推荐使用 `async with` 语句来管理客户端生命周期
3. **Monica 版本**: Monica 5.0.0-beta.5 版本的联系人 API 使用 Web 路由，返回 HTML 页面。本库会自动解析 HTML 中的 JSON 数据
4. **缓存机制**: `ContactInformationExtractor` 支持缓存，避免重复请求同一联系人的信息
5. **日期格式**: 所有日期参数使用 `YYYY-MM-DD` 格式（如 "2026-01-09"）

## 版本

当前版本: 0.1.0

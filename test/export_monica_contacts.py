"""
导出 Monica 指定 Vault 下所有联系人的完整信息到 JSON 与 Excel。

用法（在项目根目录或 test 目录下）:
    python export_monica_contacts.py

可选环境变量:
    MONICA_TOKEN   - API Token
    MONICA_BASE_URL - 实例地址，默认 http://mem.deep-diary.com
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient

# 与 test_monica_client.py 保持一致，也可用环境变量覆盖
MONICA_TOKEN = os.environ.get(
    "MONICA_TOKEN", "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46"
)
MONICA_BASE_URL = os.environ.get("MONICA_BASE_URL", "http://mem.deep-diary.com")

# 需要导出的 3 个 Vault（Family / Friends / Work）
EXPORT_VAULTS = [
    {"name": "Family", "id": "019b6548-e77c-73ad-8431-846334b79395"},
    {"name": "Friends", "id": "019b83ae-f4bc-7360-bab1-84e226a00e43"},
    {"name": "Work", "id": "019b83b0-bd96-700c-bb9a-9bd74f99202f"},
]

MODULE_KEYS = [
    ("calls", "通话"),
    ("reminders", "提醒"),
    ("notes", "笔记"),
    ("addresses", "地址"),
    ("contact_information", "联系信息"),
    ("dates", "重要日期"),
    ("quick_facts_list", "快速事实"),
]


def _flatten_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _flatten_record(record: Dict[str, Any], prefix: str = "") -> Dict[str, Any]:
    flat: Dict[str, Any] = {}
    for key, value in record.items():
        col = f"{prefix}{key}" if not prefix else f"{prefix}_{key}"
        if isinstance(value, dict):
            for sub_key, sub_val in _flatten_record(value).items():
                flat[f"{col}_{sub_key}"] = sub_val
        else:
            flat[col] = _flatten_value(value)
    return flat


def _records_to_rows(
    records: Optional[List[Any]],
    vault_name: str,
    vault_id: str,
    contact_id: str,
    contact_name: Optional[str],
) -> List[Dict[str, Any]]:
    if not records or not isinstance(records, list):
        return []
    rows = []
    for item in records:
        if not isinstance(item, dict):
            continue
        row = {
            "vault_name": vault_name,
            "vault_id": vault_id,
            "contact_id": contact_id,
            "contact_name": contact_name or "",
        }
        row.update(_flatten_record(item))
        rows.append(row)
    return rows


def _write_sheet(ws, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        ws.append(["（无数据）"])
        return
    headers: List[str] = []
    for row in rows:
        for key in row:
            if key not in headers:
                headers.append(key)
    ws.append(headers)
    for row in rows:
        ws.append([row.get(h, "") for h in headers])


def save_excel(export_root: Dict[str, Any], path: str) -> None:
    from openpyxl import Workbook

    wb = Workbook()
    overview_ws = wb.active
    overview_ws.title = "联系人概览"
    overview_ws.append(
        [
            "vault_name",
            "vault_id",
            "contact_id",
            "contact_name",
            *[label for _, label in MODULE_KEYS],
        ]
    )

    module_sheets: Dict[str, List[Dict[str, Any]]] = {
        label: [] for _, label in MODULE_KEYS
    }

    for vault in export_root.get("vaults", []):
        vault_name = vault.get("name", "")
        vault_id = vault.get("id", "")
        for contact in vault.get("contacts", []):
            contact_id = contact.get("contact_id", "")
            contact_name = contact.get("contact_name", "")
            counts = {
                key: len(contact.get(key) or [])
                if isinstance(contact.get(key), list)
                else (1 if contact.get(key) else 0)
                for key, _ in MODULE_KEYS
            }
            overview_ws.append(
                [
                    vault_name,
                    vault_id,
                    contact_id,
                    contact_name,
                    *[counts[key] for key, _ in MODULE_KEYS],
                ]
            )
            for key, label in MODULE_KEYS:
                module_sheets[label].extend(
                    _records_to_rows(
                        contact.get(key),
                        vault_name,
                        vault_id,
                        contact_id,
                        contact_name,
                    )
                )

    for _, label in MODULE_KEYS:
        ws = wb.create_sheet(title=label[:31])
        _write_sheet(ws, module_sheets[label])

    wb.save(path)


async def export_vault_contacts(
    client: MonicaClient, vault_name: str, vault_id: str
) -> Dict[str, Any]:
    print(f"\n{'=' * 50}")
    print(f"Vault: {vault_name} ({vault_id})")
    print("=" * 50)

    contacts = await client.contacts.list_all(vault_id, verbose=True)
    print(f"共 {len(contacts)} 个联系人，开始拉取详情…")

    exported_contacts: List[Dict[str, Any]] = []
    for i, contact in enumerate(contacts, 1):
        contact_id = contact.get("id")
        contact_name = contact.get("name", "N/A")
        if not contact_id:
            print(f"  [{i}/{len(contacts)}] 跳过：无 ID")
            continue

        print(f"  [{i}/{len(contacts)}] {contact_name} ({contact_id}) …", end=" ", flush=True)
        info = await client.contact_info.get_all_information_as_dict(vault_id, contact_id)
        if info:
            exported_contacts.append(info)
            print("✓")
        else:
            print("✗ 获取失败")

    return {
        "name": vault_name,
        "id": vault_id,
        "contact_count": len(exported_contacts),
        "contacts": exported_contacts,
    }


async def main() -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "exports",
        f"monica_export_{timestamp}",
    )
    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, "monica_contacts_export.json")
    excel_path = os.path.join(output_dir, "monica_contacts_export.xlsx")

    print("Monica 联系人批量导出")
    print(f"服务器: {MONICA_BASE_URL}")
    print(f"Vault 数量: {len(EXPORT_VAULTS)}")
    print(f"输出目录: {output_dir}")

    async with MonicaClient(MONICA_TOKEN, MONICA_BASE_URL) as client:
        user = await client.get_current_user()
        user_name = ""
        if user and "data" in user:
            user_name = user["data"].get("name", "")

        export_data: Dict[str, Any] = {
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "base_url": MONICA_BASE_URL,
            "user_name": user_name,
            "vaults": [],
        }

        for vault in EXPORT_VAULTS:
            vault_export = await export_vault_contacts(
                client, vault["name"], vault["id"]
            )
            export_data["vaults"].append(vault_export)

        total_contacts = sum(v.get("contact_count", 0) for v in export_data["vaults"])
        export_data["total_contacts"] = total_contacts

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

    save_excel(export_data, excel_path)

    print("\n" + "=" * 50)
    print("导出完成")
    print("=" * 50)
    print(f"联系人总数: {total_contacts}")
    for v in export_data["vaults"]:
        print(f"  - {v['name']}: {v['contact_count']} 人")
    print(f"\nJSON:  {json_path}")
    print(f"Excel: {excel_path}")


if __name__ == "__main__":
    asyncio.run(main())

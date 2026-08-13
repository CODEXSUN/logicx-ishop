import json
from typing import Any

import frappe
from frappe import _

from logicx_ishop.api.demo_catalog import build_demo_catalog


ITEM_FIELDS = [
	"name",
	"item_code",
	"item_name",
	"erpnext_item",
	"availability",
	"item_group",
	"brand",
	"short_description",
	"full_description",
	"web_price",
	"mrp",
	"image",
	"highlights",
	"published",
	"modified",
]
ERP_ITEM_FIELDS = [
	"name",
	"item_code",
	"item_name",
	"item_group",
	"brand",
	"stock_uom",
	"description",
	"image",
	"disabled",
	"is_stock_item",
	"standard_rate",
	"modified",
]
CATALOG_FIELDS = [
	"name",
	"catalog_code",
	"catalog_name",
	"description",
	"catalog_image",
	"published",
	"modified",
]


def _require_catalog_access() -> None:
	roles = set(frappe.get_roles())
	if not roles.intersection({"System Manager", "LogicX iShop Manager"}):
		frappe.throw(_("LogicX iShop Manager access is required."), frappe.PermissionError)


@frappe.whitelist(methods=["GET"])
def get_catalog_snapshot() -> dict[str, Any]:
	_require_catalog_access()
	items = frappe.get_list("iShop Item", fields=ITEM_FIELDS, order_by="item_code asc", limit=0)
	linked_items = sorted({row.erpnext_item for row in items if row.erpnext_item})
	erpnext_items = frappe.get_list(
		"Item",
		filters={"name": ["in", linked_items]},
		fields=ERP_ITEM_FIELDS,
		order_by="item_code asc",
		limit=0,
	) if linked_items else []
	catalogs = frappe.get_list(
		"iShop Catalog", fields=CATALOG_FIELDS, order_by="catalog_code asc", limit=0
	)
	for catalog in catalogs:
		document = frappe.get_doc("iShop Catalog", catalog.name)
		catalog["catalog_items"] = [
			{"ishop_item": row.ishop_item, "display_order": row.display_order}
			for row in document.catalog_items
		]
	return {"items": items, "erpnext_items": erpnext_items, "catalogs": catalogs}


@frappe.whitelist(methods=["POST"])
def upsert_catalog_snapshot(payload: str | dict[str, Any]) -> dict[str, Any]:
	_require_catalog_access()
	data = json.loads(payload) if isinstance(payload, str) else payload
	if not isinstance(data, dict):
		frappe.throw(_("Catalog payload must be an object."))
	erpnext_items = data.get("erpnext_items") or []
	items = data.get("items") or []
	catalogs = data.get("catalogs") or []
	if not all(isinstance(rows, list) for rows in (erpnext_items, items, catalogs)):
		frappe.throw(_("Catalog collections must be arrays."))

	for row in erpnext_items:
		_upsert_erpnext_item(row)
	for row in items:
		_upsert_ishop_item(row)
	for row in catalogs:
		_upsert_catalog(row)
	return {
		"erpnext_items": len(erpnext_items),
		"items": len(items),
		"catalogs": len(catalogs),
		"snapshot": get_catalog_snapshot(),
	}


@frappe.whitelist(methods=["POST"])
def seed_dummy_catalog() -> dict[str, Any]:
	_require_catalog_access()
	return upsert_catalog_snapshot(build_demo_catalog())


def _upsert_erpnext_item(row: dict[str, Any]) -> None:
	item_code = _required(row, "item_code")
	item_group = str(row.get("item_group") or "Products")
	_ensure_named_document("Item Group", item_group, {"item_group_name": item_group})
	brand = str(row.get("brand") or "")
	if brand:
		_ensure_named_document("Brand", brand, {"brand": brand})
	values = {
		"item_code": item_code,
		"item_name": str(row.get("item_name") or item_code),
		"item_group": item_group,
		"brand": brand or None,
		"stock_uom": str(row.get("stock_uom") or "Nos"),
		"description": str(row.get("description") or ""),
		"image": row.get("image") or None,
		"disabled": int(bool(row.get("disabled", 0))),
		"is_stock_item": int(bool(row.get("is_stock_item", 1))),
		"standard_rate": float(row.get("standard_rate") or 0),
	}
	_upsert_document("Item", item_code, values)


def _upsert_ishop_item(row: dict[str, Any]) -> None:
	item_code = _required(row, "item_code")
	values = {key: row.get(key) for key in ITEM_FIELDS if key not in {"name", "modified"}}
	values.update({"item_code": item_code, "item_name": str(row.get("item_name") or item_code)})
	_upsert_document("iShop Item", item_code, values)


def _upsert_catalog(row: dict[str, Any]) -> None:
	catalog_code = _required(row, "catalog_code")
	values = {key: row.get(key) for key in CATALOG_FIELDS if key not in {"name", "modified"}}
	values.update({"catalog_code": catalog_code, "catalog_name": str(row.get("catalog_name") or catalog_code)})
	document = frappe.get_doc("iShop Catalog", catalog_code) if frappe.db.exists("iShop Catalog", catalog_code) else frappe.new_doc("iShop Catalog")
	document.update(values)
	document.set("catalog_items", [])
	for child in row.get("catalog_items") or []:
		document.append("catalog_items", {
			"ishop_item": _required(child, "ishop_item"),
			"display_order": int(child.get("display_order") or 0),
		})
	document.save() if document.name else document.insert()


def _upsert_document(doctype: str, name: str, values: dict[str, Any]) -> None:
	document = frappe.get_doc(doctype, name) if frappe.db.exists(doctype, name) else frappe.new_doc(doctype)
	document.update(values)
	document.save() if document.name else document.insert()


def _ensure_named_document(doctype: str, name: str, values: dict[str, Any]) -> None:
	if frappe.db.exists(doctype, name):
		return
	document = frappe.new_doc(doctype)
	document.update(values)
	document.insert()


def _required(row: dict[str, Any], key: str) -> str:
	value = str(row.get(key) or "").strip()
	if not value:
		frappe.throw(_("{0} is required.").format(key))
	return value

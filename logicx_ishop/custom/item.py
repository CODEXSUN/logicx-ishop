from typing import Any

import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


ITEM_CUSTOM_FIELDS = {
	"Item": [
		{
			"fieldname": "ishop_tab",
			"label": "iShop",
			"fieldtype": "Tab Break",
			"insert_after": "details",
		},
		{
			"fieldname": "ishop_item_details_html",
			"label": "iShop Item Details",
			"fieldtype": "HTML",
			"insert_after": "ishop_tab",
			"read_only": 1,
		},
	]
}
LINKED_ITEM_FIELDS = [
	"name",
	"item_code",
	"item_name",
	"availability",
	"item_group",
	"brand",
	"short_description",
	"highlights",
	"web_price",
	"mrp",
	"image",
	"published",
	"modified",
]


def setup_item_custom_fields() -> None:
	create_custom_fields(ITEM_CUSTOM_FIELDS, ignore_validate=True)


@frappe.whitelist(methods=["GET"])
def get_linked_ishop_items(item: str) -> dict[str, Any]:
	item = str(item or "").strip()
	if not item:
		frappe.throw(_("Item is required."))

	if not frappe.db.exists("Item", item):
		frappe.throw(_("Item {0} not found.").format(item), frappe.DoesNotExistError)

	if not frappe.has_permission("Item", doc=item):
		frappe.throw(_("You do not have permission to read Item {0}.").format(item), frappe.PermissionError)

	if not frappe.has_permission("iShop Item", "read"):
		return {"items": [], "can_read": False, "can_create": False}

	items = frappe.get_list(
		"iShop Item",
		filters={"erpnext_item": item},
		fields=LINKED_ITEM_FIELDS,
		order_by="item_code asc",
		limit=0,
	)
	return {
		"items": items,
		"can_read": True,
		"can_create": bool(frappe.has_permission("iShop Item", "create")),
	}

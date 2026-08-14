import frappe

from logicx_ishop.custom.item import setup_item_custom_fields


def execute():
	"""Move the Item iShop tab from after `details` to after `uoms`."""
	setup_item_custom_fields()
	frappe.clear_cache(doctype="Item")

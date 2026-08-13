import frappe
from frappe import _


def execute():
	"""Fail early with a readable message when the new unique index cannot be created."""
	duplicates = frappe.db.sql(
		"""
		select erpnext_item, count(name) as linked
		from `tabiShop Item`
		where ifnull(erpnext_item, '') != ''
		group by erpnext_item
		having count(name) > 1
		""",
		as_dict=True,
	)
	if not duplicates:
		return

	details = ", ".join(f"{row.erpnext_item} ({row.linked})" for row in duplicates)
	frappe.throw(
		_("Each ERPNext Item can be linked to one iShop Item only. Remove these duplicate links first: {0}").format(
			details
		),
		frappe.UniqueValidationError,
	)

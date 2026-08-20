import frappe


def execute():
	"""Remove the Report record left behind by the Item Group Statistics rename.

	Version 1.0.13 shipped the report as `Item Statistics`. Version 1.0.16 renamed it to
	`Item Group Statistics`, and migrate inserts the new standard record without removing
	the old one, so the stale report would stay in the report list and in search.
	"""
	if not frappe.db.exists("Report", "Item Statistics"):
		return

	# ignore_on_trash skips the guard that blocks deleting a standard report outside developer mode
	frappe.delete_doc(
		"Report",
		"Item Statistics",
		force=True,
		ignore_permissions=True,
		ignore_on_trash=True,
	)

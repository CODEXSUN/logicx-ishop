import frappe


def execute():
	"""Clear the role restriction on the LogicX iShop Desktop Icon.

	Version 1.0.12 restricted the icon to `TM User`, `TM Admin`, `LogicX iShop Manager`,
	and `System Manager`. Two of those roles belong to another application, so the icon
	disappeared for every Desk user without one of them. An empty role list restores the
	icon for all Desk users.
	"""
	if not frappe.db.exists("DocType", "Desktop Icon"):
		return

	for icon_name in frappe.get_all("Desktop Icon", filters={"app": "logicx_ishop"}, pluck="name"):
		icon = frappe.get_doc("Desktop Icon", icon_name)
		if not icon.meta.get_field("roles") or not icon.get("roles"):
			continue

		icon.set("roles", [])
		icon.save(ignore_permissions=True)

	frappe.clear_cache()

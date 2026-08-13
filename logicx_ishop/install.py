import frappe


APP_LOGO_URL = "/assets/logicx_ishop/images/logicx-ishop-logo.svg?v=1"


def after_install():
	update_desktop_icon_logo()


def update_desktop_icon_logo():
	icon_name = frappe.db.get_value("Desktop Icon", {"app": "logicx_ishop"})
	if not icon_name:
		return

	frappe.db.set_value(
		"Desktop Icon",
		icon_name,
		"logo_url",
		APP_LOGO_URL,
		update_modified=False,
	)

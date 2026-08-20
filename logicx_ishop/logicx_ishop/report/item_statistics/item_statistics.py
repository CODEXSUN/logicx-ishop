import frappe
from frappe import _


# Each "Type" the user can pick maps to a fixed SQL condition on `tabiShop Item`.
# The filter value only looks up a key, so nothing user-supplied reaches the query.
TYPE_CONDITIONS = {
	"Published": "item.published = 1",
	"Non-Published": "IFNULL(item.published, 0) = 0",
	"Image Set": "IFNULL(item.image, '') != ''",
	"Image Not Set": "IFNULL(item.image, '') = ''",
	"Price Set": "IFNULL(item.web_price, 0) > 0",
	"Price Not Set": "IFNULL(item.web_price, 0) <= 0",
	"All Items": "1 = 1",
}

DEFAULT_TYPE = "Published"


def execute(filters=None):
	filters = frappe._dict(filters or {})
	selected_type = filters.get("type") or DEFAULT_TYPE
	if selected_type not in TYPE_CONDITIONS:
		frappe.throw(_("Invalid Type: {0}").format(selected_type))

	return get_columns(selected_type), get_data(selected_type)


def get_columns(selected_type):
	return [
		{
			"label": _("Item Group"),
			"fieldname": "item_group",
			"fieldtype": "Link",
			"options": "Item Group",
			"width": 300,
		},
		{
			"label": _("Brand"),
			"fieldname": "brand",
			"fieldtype": "Link",
			"options": "Brand",
			"width": 250,
		},
		{
			# the count column is labelled with the Type being counted, e.g. "Image Not Set"
			"label": _(selected_type),
			"fieldname": "count",
			"fieldtype": "Int",
			"width": 130,
		},
	]


def get_data(selected_type):
	return frappe.db.sql(
		f"""
		SELECT
			item.item_group,
			item.brand,
			COUNT(item.name) AS count
		FROM `tabiShop Item` item
		WHERE {TYPE_CONDITIONS[selected_type]}
		GROUP BY item.item_group, item.brand
		ORDER BY count DESC, item.item_group, item.brand
		""",
		as_dict=True,
	)

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

	return get_columns(), get_data(selected_type, filters)


def get_columns():
	return [
		{
			"label": _("Item Group"),
			"fieldname": "item_group",
			"fieldtype": "Link",
			"options": "Item Group",
			"width": 200,
		},
		{
			"label": _("Brand"),
			"fieldname": "brand",
			"fieldtype": "Link",
			"options": "Brand",
			"width": 140,
		},
		{
			# the iShop Item is named after its Item Code, so the link column is the Item ID
			"label": _("Item ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "iShop Item",
			"width": 140,
		},
		{
			"label": _("Item Name"),
			"fieldname": "item_name",
			"fieldtype": "Data",
			"width": 260,
		},
		{
			"label": _("Web Price"),
			"fieldname": "web_price",
			"fieldtype": "Currency",
			"width": 110,
		},
		{
			"label": _("MRP"),
			"fieldname": "mrp",
			"fieldtype": "Currency",
			"width": 110,
		},
		{
			"label": _("Published"),
			"fieldname": "published",
			"fieldtype": "Check",
			"width": 90,
		},
		{
			"label": _("Availability"),
			"fieldname": "availability",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Highlights"),
			"fieldname": "highlights",
			"fieldtype": "Data",
			"width": 260,
		},
	]


def get_data(selected_type, filters):
	conditions = [TYPE_CONDITIONS[selected_type]]
	params = {}
	if filters.get("item_group"):
		conditions.append("item.item_group = %(item_group)s")
		params["item_group"] = filters["item_group"]
	if filters.get("brand"):
		conditions.append("item.brand = %(brand)s")
		params["brand"] = filters["brand"]

	return frappe.db.sql(
		f"""
		SELECT
			item.item_group,
			item.brand,
			item.name,
			item.item_name,
			item.web_price,
			item.mrp,
			item.published,
			item.availability,
			item.highlights
		FROM `tabiShop Item` item
		WHERE {" AND ".join(conditions)}
		ORDER BY item.item_group, item.brand, item.item_name
		""",
		params,
		as_dict=True,
	)

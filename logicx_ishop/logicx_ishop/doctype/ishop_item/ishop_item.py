import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import strip_html


HIGHLIGHTS_LENGTH = 140


class IShopItem(Document):
	def before_validate(self):
		if self.erpnext_item:
			self._fill_missing_erpnext_values()

	def validate(self):
		if not self.published:
			return

		if not self.short_description:
			frappe.throw(_("Short Description is required when Published is checked."))

		if not self.image:
			frappe.throw(_("Image is required when Published is checked."))

	def _fill_missing_erpnext_values(self):
		values = get_erpnext_item_defaults(self.erpnext_item)
		for fieldname, value in values.items():
			if not self.get(fieldname) and value not in (None, ""):
				self.set(fieldname, value)


@frappe.whitelist(methods=["GET"])
def get_erpnext_item_defaults(item_name: str):
	item = frappe.get_doc("Item", item_name)
	if not item.has_permission("read"):
		frappe.throw(_("You do not have permission to read Item {0}.").format(item_name), frappe.PermissionError)

	description = item.description or ""
	plain_description = _plain_text(description)
	return {
		"item_code": item.item_code,
		"item_name": item.item_name,
		"item_group": item.item_group,
		"brand": item.brand,
		"short_description": plain_description,
		"full_description": description,
		"web_price": _selling_price(item),
		"image": item.image,
		"highlights": plain_description[:HIGHLIGHTS_LENGTH],
	}


def _selling_price(item):
	price = frappe.get_all(
		"Item Price",
		filters={"item_code": item.item_code, "selling": 1},
		fields=["price_list_rate"],
		order_by="valid_from desc, modified desc",
		limit_page_length=1,
	)
	return price[0].price_list_rate if price else item.standard_rate


def _plain_text(value: str):
	return " ".join(strip_html(value).split())


iShopItem = IShopItem

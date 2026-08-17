import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import strip_html


class IShopItem(Document):
	def before_validate(self):
		if self.is_new() and self.erpnext_item:
			self._fill_missing_erpnext_values()

	def validate(self):
		self._validate_unique_erpnext_item()

		if not self.published:
			return

		if not self.short_description:
			frappe.throw(_("Short Description is required when Published is checked."))

		if not self.image:
			frappe.throw(_("Image is required when Published is checked."))

	def _validate_unique_erpnext_item(self):
		if not self.erpnext_item:
			return

		linked = frappe.db.get_value(
			"iShop Item",
			{"erpnext_item": self.erpnext_item, "name": ["!=", self.name]},
			"name",
		)
		if linked:
			frappe.throw(
				_("ERPNext Item {0} is already linked to iShop Item {1}.").format(
					self.erpnext_item, linked
				),
				frappe.UniqueValidationError,
			)

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

	# Full Description and Highlights stay author-owned and are never copied from the ERPNext Item.
	return {
		"item_code": item.item_code,
		"item_name": item.item_name,
		"item_group": item.item_group,
		"brand": item.brand,
		"short_description": _plain_text(item.description or ""),
		"image": item.image,
	}


def _plain_text(value: str):
	return " ".join(strip_html(value).split())


iShopItem = IShopItem

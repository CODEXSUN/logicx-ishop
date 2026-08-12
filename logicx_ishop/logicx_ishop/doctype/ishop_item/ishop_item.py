import frappe
from frappe import _
from frappe.model.document import Document


class IShopItem(Document):
	def validate(self):
		if not self.published:
			return

		if not self.short_description:
			frappe.throw(_("Short Description is required when Published is checked."))

		if not self.image:
			frappe.throw(_("Image is required when Published is checked."))


iShopItem = IShopItem

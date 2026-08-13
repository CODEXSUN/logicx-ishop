import frappe
from frappe.tests import IntegrationTestCase

from logicx_ishop.logicx_ishop.doctype.ishop_item.ishop_item import get_erpnext_item_defaults


class TestIShopItem(IntegrationTestCase):
	def test_erpnext_item_defaults_are_ready_to_save(self):
		item = frappe.get_doc(
			doctype="Item",
			item_code="TEST-ISHOP-AUTOFILL",
			item_name="Autofill Item",
			item_group="All Item Groups",
			stock_uom="Nos",
			description="<p>Fast and reliable.</p>",
			standard_rate=125,
			image="/files/autofill-item.png",
		).insert()
		frappe.get_doc(
			doctype="Item Price",
			item_code=item.name,
			price_list="Standard Selling",
			price_list_rate=150,
		).insert()

		values = get_erpnext_item_defaults(item.name)
		ishop_item = frappe.new_doc("iShop Item")
		ishop_item.erpnext_item = item.name
		ishop_item.availability = "Immediately"
		ishop_item.run_method("before_validate")

		self.assertEqual(values["web_price"], 150)
		self.assertEqual(ishop_item.item_code, item.item_code)
		self.assertEqual(ishop_item.item_name, item.item_name)
		self.assertEqual(ishop_item.item_group, item.item_group)
		self.assertEqual(ishop_item.short_description, "Fast and reliable.")
		self.assertEqual(ishop_item.web_price, 150)
		self.assertEqual(ishop_item.image, item.image)

	def test_full_description_and_highlights_are_never_autofilled(self):
		item = frappe.get_doc(
			doctype="Item",
			item_code="TEST-ISHOP-NO-AUTOFILL",
			item_name="No Autofill Item",
			item_group="All Item Groups",
			stock_uom="Nos",
			description="<p>Fast and reliable.</p>",
		).insert()

		values = get_erpnext_item_defaults(item.name)
		ishop_item = frappe.new_doc("iShop Item")
		ishop_item.erpnext_item = item.name
		ishop_item.availability = "Immediately"
		ishop_item.run_method("before_validate")

		self.assertNotIn("full_description", values)
		self.assertNotIn("highlights", values)
		self.assertFalse(ishop_item.full_description)
		self.assertFalse(ishop_item.highlights)

	def test_erpnext_item_can_be_linked_only_once(self):
		item = frappe.get_doc(
			doctype="Item",
			item_code="TEST-ISHOP-UNIQUE-LINK",
			item_name="Unique Link Item",
			item_group="All Item Groups",
			stock_uom="Nos",
		).insert()
		frappe.get_doc(
			doctype="iShop Item",
			erpnext_item=item.name,
			item_code="TEST-ISHOP-UNIQUE-LINK-WEB",
			item_name="Unique Link Web Item",
			availability="Immediately",
		).insert()

		duplicate = frappe.get_doc(
			doctype="iShop Item",
			erpnext_item=item.name,
			item_code="TEST-ISHOP-UNIQUE-LINK-WEB-2",
			item_name="Duplicate Link Web Item",
			availability="Immediately",
		)

		with self.assertRaises(frappe.UniqueValidationError):
			duplicate.insert()

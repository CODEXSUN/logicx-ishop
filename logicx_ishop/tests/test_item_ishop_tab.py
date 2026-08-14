import frappe
from frappe.tests import IntegrationTestCase

from logicx_ishop.custom.item import get_linked_ishop_items, setup_item_custom_fields


class TestItemIShopTab(IntegrationTestCase):
	def test_custom_fields_add_ishop_tab_to_item(self):
		setup_item_custom_fields()

		self.assertEqual(
			frappe.db.get_value(
				"Custom Field", {"dt": "Item", "fieldname": "ishop_tab"}, ["fieldtype", "insert_after"]
			),
			("Tab Break", "uoms"),
		)
		self.assertEqual(
			frappe.db.get_value(
				"Custom Field",
				{"dt": "Item", "fieldname": "ishop_item_details_html"},
				["fieldtype", "insert_after"],
			),
			("HTML", "ishop_tab"),
		)

	def test_ishop_tab_is_moved_after_uoms_on_existing_sites(self):
		setup_item_custom_fields()
		field = frappe.get_doc("Custom Field", {"dt": "Item", "fieldname": "ishop_tab"})
		field.insert_after = "details"
		field.flags.ignore_validate = True
		field.save()

		setup_item_custom_fields()

		self.assertEqual(
			frappe.db.get_value("Custom Field", {"dt": "Item", "fieldname": "ishop_tab"}, "insert_after"),
			"uoms",
		)

	def test_linked_ishop_items_are_reported_per_item(self):
		item = frappe.get_doc(
			doctype="Item",
			item_code="TEST-ISHOP-TAB",
			item_name="iShop Tab Item",
			item_group="All Item Groups",
			stock_uom="Nos",
		).insert()
		unlinked_item = frappe.get_doc(
			doctype="Item",
			item_code="TEST-ISHOP-TAB-UNLINKED",
			item_name="Unlinked Item",
			item_group="All Item Groups",
			stock_uom="Nos",
		).insert()
		frappe.get_doc(
			doctype="iShop Item",
			erpnext_item=item.name,
			item_code="TEST-ISHOP-TAB-WEB",
			item_name="iShop Tab Web Item",
			availability="Immediately",
		).insert()

		linked = get_linked_ishop_items(item.name)
		unlinked = get_linked_ishop_items(unlinked_item.name)

		self.assertTrue(linked["can_read"])
		self.assertEqual([row.item_code for row in linked["items"]], ["TEST-ISHOP-TAB-WEB"])
		self.assertEqual(unlinked["items"], [])

	def test_unknown_item_is_rejected(self):
		with self.assertRaises(frappe.DoesNotExistError):
			get_linked_ishop_items("TEST-ISHOP-TAB-MISSING")

		with self.assertRaises(frappe.ValidationError):
			get_linked_ishop_items("  ")

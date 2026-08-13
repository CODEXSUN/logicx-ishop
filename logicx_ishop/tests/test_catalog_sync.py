import frappe
from frappe.tests import IntegrationTestCase

from logicx_ishop.api.catalog_sync import get_catalog_snapshot, seed_dummy_catalog


class TestCatalogSync(IntegrationTestCase):
	def test_seed_and_snapshot_include_all_catalog_layers(self):
		original_user = frappe.session.user
		try:
			frappe.set_user("Administrator")
			result = seed_dummy_catalog()
			snapshot = get_catalog_snapshot()
		finally:
			frappe.set_user(original_user)

		self.assertEqual(result["items"], 50)
		self.assertEqual(result["erpnext_items"], 50)
		self.assertEqual(result["catalogs"], 10)
		self.assertTrue(any(row.item_code == "CXSHOP-DEMO-LAPTOP-01" for row in snapshot["erpnext_items"]))
		self.assertTrue(any(row.item_code == "CXSHOP-DEMO-LAPTOP-01" for row in snapshot["items"]))
		self.assertTrue(any(row.catalog_code == "CXSHOP-DEMO-LAPTOPS" for row in snapshot["catalogs"]))

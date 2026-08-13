frappe.ui.form.on("iShop Item", {
	async erpnext_item(frm) {
		const selectedItem = frm.doc.erpnext_item;
		if (!selectedItem) {
			return;
		}

		const { message } = await frappe.call({
			method:
				"logicx_ishop.logicx_ishop.doctype.ishop_item.ishop_item.get_erpnext_item_defaults",
			type: "GET",
			args: { item_name: selectedItem },
			freeze: true,
			freeze_message: __("Loading ERPNext item"),
		});

		if (frm.doc.erpnext_item !== selectedItem || !message) {
			return;
		}

		await frm.set_value(message);
		frappe.show_alert({ message: __("ERPNext item details loaded"), indicator: "green" });
	},
});

function render_image_preview(frm) {
	const field = frm.get_field("image_preview");
	if (!field) {
		return;
	}

	field.$wrapper.empty();
	frm.toggle_display("image_preview", !!frm.doc.image);

	if (!frm.doc.image) {
		return;
	}

	field.$wrapper.append(
		$("<img>")
			.attr("src", frm.doc.image)
			.attr("alt", frm.doc.item_name || __("Image"))
			.css({
				width: "100%",
				height: "auto",
				"max-height": "70vh",
				"object-fit": "contain",
				"border-radius": "var(--border-radius-md)",
				border: "1px solid var(--border-color)",
			})
	);
}

frappe.ui.form.on("iShop Item", {
	refresh(frm) {
		render_image_preview(frm);
	},

	image(frm) {
		render_image_preview(frm);
	},

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

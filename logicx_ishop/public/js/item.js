frappe.ui.form.on("Item", {
	refresh(frm) {
		render_ishop_items(frm);
	},
});

async function render_ishop_items(frm) {
	const field = frm.get_field("ishop_item_details_html");
	if (!field) {
		return;
	}

	const $wrapper = field.$wrapper.empty();

	if (frm.is_new()) {
		$wrapper.append(empty_state(__("Save this Item to see its linked iShop Items.")));
		return;
	}

	const item = frm.doc.name;
	let response;
	try {
		response = await frappe.call({
			method: "logicx_ishop.custom.item.get_linked_ishop_items",
			type: "GET",
			args: { item },
		});
	} catch (error) {
		$wrapper.append(empty_state(__("Could not load iShop Items for this Item.")));
		return;
	}

	if (frm.doc.name !== item || !response || !response.message) {
		return;
	}

	const { items = [], can_read, can_create } = response.message;

	if (!can_read) {
		$wrapper.append(empty_state(__("You do not have permission to read iShop Items.")));
		return;
	}

	if (!items.length) {
		$wrapper.append(
			empty_state(__("This Item is not linked to any iShop Item yet."))
		);
		if (can_create) {
			$wrapper.append(create_button(frm));
		}
		return;
	}

	$wrapper.append(
		$(`<div class="text-muted small mb-3">${frappe.utils.escape_html(
			__("Linked iShop Item")
		)}</div>`)
	);
	items.forEach((row) => $wrapper.append(item_card(row)));
}

function item_card(row) {
	const details = [
		[__("Item Code"), frappe.utils.escape_html(row.item_code || "")],
		[__("Item Name"), frappe.utils.escape_html(row.item_name || "")],
		[__("Availability"), frappe.utils.escape_html(row.availability || "")],
		[__("Item Group"), frappe.utils.escape_html(row.item_group || "")],
		[__("Brand"), frappe.utils.escape_html(row.brand || "")],
		[__("Web Price"), format_currency_value(row.web_price)],
		[__("MRP"), format_currency_value(row.mrp)],
		[__("Published"), row.published ? __("Yes") : __("No")],
		[__("Highlights"), frappe.utils.escape_html(row.highlights || "")],
		[__("Short Description"), frappe.utils.escape_html(row.short_description || "")],
		[__("Last Updated"), frappe.datetime.str_to_user(row.modified)],
	];

	const rows = details
		.map(
			([label, value]) => `
				<div class="col-sm-6 mb-2">
					<div class="text-muted small">${label}</div>
					<div>${value || "-"}</div>
				</div>`
		)
		.join("");

	const link = `/app/ishop-item/${encodeURIComponent(row.name)}`;
	const image = row.image
		? `<img src="${frappe.utils.escape_html(row.image)}" alt="${frappe.utils.escape_html(
				row.item_name || row.item_code || ""
		  )}" style="max-height: 80px; border-radius: var(--border-radius);">`
		: "";

	return $(`
		<div class="frappe-card mb-4 p-3">
			<h6 class="mb-2">${frappe.utils.escape_html(row.item_name || row.item_code || row.name)}</h6>
			<div class="d-flex align-items-center mb-3" style="gap: var(--margin-sm);">
				${image}
				<a class="btn btn-xs" href="${link}" style="background-color: #000; border-color: #000; color: #fff;">${__(
					"Open iShop Item"
				)}</a>
			</div>
			<div class="row">${rows}</div>
		</div>
	`);
}

function format_currency_value(value) {
	if (value === null || value === undefined || value === "") {
		return "";
	}
	return frappe.utils.escape_html(format_currency(value));
}

function empty_state(message) {
	return $(
		`<div class="text-muted mb-3">${frappe.utils.escape_html(message)}</div>`
	);
}

function create_button(frm) {
	const $button = $(
		`<button class="btn btn-primary btn-sm">${__("Create iShop Item")}</button>`
	);
	$button.on("click", () => {
		frappe.route_options = { erpnext_item: frm.doc.name };
		frappe.new_doc("iShop Item");
	});
	return $button;
}

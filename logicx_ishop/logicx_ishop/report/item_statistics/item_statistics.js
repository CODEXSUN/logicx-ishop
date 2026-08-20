frappe.query_reports["Item Statistics"] = {
	filters: [
		{
			fieldname: "type",
			label: __("Type"),
			fieldtype: "Select",
			options: [
				"Published",
				"Non-Published",
				"Image Set",
				"Image Not Set",
				"Price Set",
				"Price Not Set",
				"All Items",
			].join("\n"),
			default: "Published",
			reqd: 1,
		},
	],
};

app_name = "logicx_ishop"
app_title = "LogicX iShop"
app_publisher = "LogicX"
app_description = "LogicX online shopping experience."
app_email = "ashok@logicx.in"
app_license = "mit"
app_icon = "shopping-cart"
app_color = "#172554"
app_logo_url = "/assets/logicx_ishop/images/logicx-ishop-logo.svg?v=1"

after_install = "logicx_ishop.install.after_install"

add_to_apps_screen = [
	{
		"name": app_name,
		"logo": app_logo_url,
		"title": app_title,
		"route": "/app/ishop-catalog",
	}
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "logicx_ishop",
# 		"logo": "/assets/logicx_ishop/logo.png",
# 		"title": "LogicX iShop",
# 		"route": "/logicx_ishop",
# 		"has_permission": "logicx_ishop.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/logicx_ishop/css/logicx_ishop.css"
# app_include_js = "/assets/logicx_ishop/js/logicx_ishop.js"

# include js, css files in header of web template
# web_include_css = "/assets/logicx_ishop/css/logicx_ishop.css"
# web_include_js = "/assets/logicx_ishop/js/logicx_ishop.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "logicx_ishop/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "logicx_ishop/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "logicx_ishop.utils.jinja_methods",
# 	"filters": "logicx_ishop.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "logicx_ishop.install.before_install"
# after_install = "logicx_ishop.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "logicx_ishop.uninstall.before_uninstall"
# after_uninstall = "logicx_ishop.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "logicx_ishop.utils.before_app_install"
# after_app_install = "logicx_ishop.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "logicx_ishop.utils.before_app_uninstall"
# after_app_uninstall = "logicx_ishop.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "logicx_ishop.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "logicx_ishop.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"logicx_ishop.tasks.all"
# 	],
# 	"daily": [
# 		"logicx_ishop.tasks.daily"
# 	],
# 	"hourly": [
# 		"logicx_ishop.tasks.hourly"
# 	],
# 	"weekly": [
# 		"logicx_ishop.tasks.weekly"
# 	],
# 	"monthly": [
# 		"logicx_ishop.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "logicx_ishop.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "logicx_ishop.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "logicx_ishop.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "logicx_ishop.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["logicx_ishop.utils.before_request"]
# after_request = ["logicx_ishop.utils.after_request"]

# Job Events
# ----------
# before_job = ["logicx_ishop.utils.before_job"]
# after_job = ["logicx_ishop.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"logicx_ishop.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

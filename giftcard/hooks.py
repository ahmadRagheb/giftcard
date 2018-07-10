# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "giftcard"
app_title = "Giftcard"
app_publisher = "ahmad ragheb"
app_description = "issue gift cards and consum it in pos and sales invoice"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ahmedragheb75@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/giftcard/css/giftcard.css"
# app_include_js = "/assets/giftcard/js/giftcard.js"

# include js, css files in header of web template
# web_include_css = "/assets/giftcard/css/giftcard.css"
# web_include_js = "/assets/giftcard/js/giftcard.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "giftcard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "giftcard.install.before_install"
# after_install = "giftcard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "giftcard.notifications.get_notification_config"

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
#	}
# }

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Payment Entry": {
		"on_submit": "giftcard.gift_api.consum_gift_card",
		"on_cancel": "giftcard.gift_api.consum_gift_card"
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"giftcard.tasks.all"
# 	],
# 	"daily": [
# 		"giftcard.tasks.daily"
# 	],
# 	"hourly": [
# 		"giftcard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"giftcard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"giftcard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "giftcard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "giftcard.event.get_events"
# }


# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
import frappe.www.list
from frappe import _

no_cache = 1


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	lessons_completed = frappe.get_all(
        "LMS Course Progress",
        filters={"member": frappe.session.user, "status": "Complete"},
        # fields=["lesson"],
    )
	lessons_count = frappe.get_all("Course Lesson", fields=["name"])
	context.lessons_count = len(lessons_count)
	context.lessons_completed = len(lessons_completed)
	context.current_user = frappe.get_doc("User", frappe.session.user)
	context.show_sidebar = False

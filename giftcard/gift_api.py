# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import frappe
import frappe.handler
import frappe.client
from frappe.utils.response import build_response
from frappe import _
from six.moves.urllib.parse import urlparse, urlencode
from frappe.utils.data import today

def consum_gift_card(doc,method):
	type_payment= "بطاقة هدايا"

	if doc.mode_of_payment == type_payment:
		card_number = doc.gift_card_number
		if len(card_number)<1:
			frappe.throw("Please enter Gift Card number")

		q = frappe.get_all('Gift Card', filters={'card_number':card_number }, fields=['name'])
		if len(q) == 0:
			frappe.throw("Wrong Gift Card Number")		
		else:
			gift_doc = frappe.get_doc("Gift Card",q[0].name)
			if method == "on_cancel":
				gift_doc.add_balance(doc.paid_amount)
			else:
				if gift_doc.allow_only_once == 1:
					if gift_doc.check_used():
						frappe.throw("One time use card can't be used twice")
					else:
						gift_doc.update_balance(doc.paid_amount)
				elif gift_doc.is_expired():
					frappe.throw("Expired Card")

				else:
					gift_doc.update_balance(doc.paid_amount)



			gift_doc.save()
			frappe.db.commit()
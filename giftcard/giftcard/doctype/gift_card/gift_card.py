# -*- coding: utf-8 -*-
# Copyright (c) 2018, ahmad ragheb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import string
from random import randint
from frappe.utils.data import flt

class GiftCard(Document):
	
	def validate(self):
		if not self.card_number:
			self.create_card_number()
		if flt(self.amount) <=0:
			frappe.throw("Amount Should be Positive number")
		if not self.balance:
			self.balance = self.amount

	def update_balance(self,x):
		if x <= 0 : 
			frappe.throw("Not allowed nigative number")

		elif self.balance < x :
			frappe.throw("Value used Bigger than GiftCard balance")

		else:
			self.balance = flt(self.balance) - flt(x) 

	def create_card_number(self):			
		data = list(string.ascii_lowercase)
		[data.append(n) for n in range(0, 10)]
		random_list = [str(data[randint(0, len(data)-1)]) for n in range(0, 21)]
		random_string = ''.join(random_list)
		self.card_number = random_string

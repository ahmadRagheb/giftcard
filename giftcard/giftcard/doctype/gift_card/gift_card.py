# -*- coding: utf-8 -*-
# Copyright (c) 2018, ahmad ragheb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import string
from random import randint
from frappe.utils.data import flt
from frappe.utils.data import today
import time
import datetime

class GiftCard(Document):
	
	def validate(self):
 		if not self.card_number:
 			self.create_card_number()
 		if flt(self.amount) <=0:
 			frappe.throw("Amount Should be Positive number")
 		if not self.balance:
 			self.balance = self.amount
 		self.is_expired_on_validate()

	def update_balance(self,x):
		if self.balance < x :
			frappe.throw("Paid Amount exceeded GiftCard balance")

		else:
			self.balance = flt(self.balance) - flt(x) 

	def add_balance(self,x):
		self.balance = flt(self.balance) + flt(x) 

	
	def check_used(self):
		if self.balance == self.amount:
			return False
		else:
			return True 

	# ignored for using js lib
	def create_card_number(self):
		# data = list(string.ascii_lowercase)
		data = []
		[data.append(n) for n in range(0, 10)]
		random_list = [str(data[randint(0, len(data)-1)]) for n in range(0, 11)]
		random_string = ''.join(random_list)
		self.card_number = random_string

	def is_expired(self):
		if self.expiry_date :
			expiry_date = self.expiry_date
			today_v = today()
			newdate1 = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d") 
			now_date = datetime.datetime.strptime(today_v, "%Y-%m-%d") 
			if newdate1 < now_date:
				return True
			else:
				return False
		else:
			frappe.throw("Please insert expiry date")

	def is_expired_on_validate(self):
		if self.expiry_date :
			expiry_date = self.expiry_date
			today_v = today()
			newdate1 = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d") 
			now_date = datetime.datetime.strptime(today_v, "%Y-%m-%d") 
			if newdate1 < now_date:
				frappe.throw("Please insert expiry date more than current date ")
			else:
				return False
		else:
			frappe.throw("Please insert expiry date")
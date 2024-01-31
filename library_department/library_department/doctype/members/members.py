# Copyright (c) 2023, NEW INDIA and contributors Members
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import regex as re

class Members(Document):

	def validate(self):
		
		if self.first_name and self.last_name:
			self.full_name = self.first_name + " " + self.last_name
		else:
			frappe.throw("Plese Enter First Name, Last Name")		
   
		self.validate_dob()
		self.validate_address()
		self.validate_phone()
		self.validate_email()
		self.unique_ids()
		self.validate_photo_format()
		self.after_save()
		
  
	def after_save(self):
		frappe.msgprint("Congratulations...!!   Form Saved Successfully")
  
	@frappe.whitelist()
	def validate_dob(self):
		# if self.date_of_birth == None:
		# 	frappe.throw("Please Enter Date of Birth")
		dob = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
		cur_date = datetime.now().date()

		age = cur_date.year - dob.year - ((cur_date.month,cur_date.day) < (dob.month,dob.day))

		if dob == cur_date:
			frappe.throw("Dob is Same as Current Date")
		elif dob > cur_date:
			frappe.throw("Date Of birth can't be furture date")
		elif age == 0:
			frappe.throw("Enter Valid Age (Greater than 1 year)")
		else:
			self.age = age

	@frappe.whitelist()
	def validate_photo_format(self):
		if self.photo:
			path = self.photo.split(".")  
			path_format = path[-1]
			if path_format not in ['jpg','jpeg','pdf','png']:
				frappe.throw('Enter Valid Format including(jpg,jpeg,pdf,png ONLY)')
		

	@frappe.whitelist()		
	def validate_address(self):
		# if self.full_address == None:
		# 	frappe.throw("Please Enter Full Address")
		add = self.full_address
		if self.full_address:
			add = self.full_address.split("\n")
		if len(add) < 4:
			frappe.throw("Write at least 4 lines of Address")

	@frappe.whitelist()
	def validate_phone(self):
		# if self.phone == None:
		# 	frappe.throw("Please Enter Phone Number")
		check_contact = r'^[1-9][0-9]{9}$'
		if re.fullmatch(check_contact,self.phone):
			pass
		else:
			frappe.throw("Please Enter 10 Digit Numbers with Integers Only")
   
   
	@frappe.whitelist()
	def validate_email(self):
		# if self.email == None:
		# 	frappe.throw("Please Enter Email Address")
		check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
		if re.fullmatch(check_email, self.email):
		    pass
		else:
		    frappe.throw("Enter a Valid Email Address")
   
	
	def unique_ids(self):
		members = frappe.get_all('Members', fields=['name','full_name', 'email', 'phone'])
		for i in members:
			if i.get('email') == self.email and i.name != self.name:
				frappe.throw("Email Already Exist")
    
    
    
# Copyright (c) 2023, NEW INDIA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import regex as re
import os

class LibraryMember(Document):
    
    def before_save(self):
        self.full_name = self.first_name + " " + self.last_name
        self.check_mail()
        self.contact_check()
        self.id_format_check()
									
    def check_mail(self):
        check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(check_email, self.email_address):
            print("******Valid Email**********")
        else:
            raise ValueError("Invalid Email Format")

    def contact_check(self):
        check_contact = r'^[1-9][0-9]{9}$'
        if re.fullmatch(check_contact,self.phone):
            print("Valid Contact No")
        else:
            raise ValueError("Invalid no")
        
    def id_format_check(self):
        extensions_must_be = [".pdf", ".docx",".txt",".jpg"]
        temp = self.id_proof.split('.')[-1]
        if '.'+temp in extensions_must_be:
            print("Valid Format")
        else:
            raise ValueError("Invalid format")            

            
    
              
        

    


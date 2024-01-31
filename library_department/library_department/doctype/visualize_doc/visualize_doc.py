# Copyright (c) 2023, NEW INDIA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from flask import jsonify
import pandas as pd
import pygwalker as pyg
from frappe import _
import requests

class VisualizeDoc(Document):

	def validate(self):

		data = frappe.db.sql("""select v.name1 as name,v.surname,v.age,f.name1 as child_name,f.relation from `tabVisualize Doc` as v join `tabFamily` as f ON v.name=f.parent ORDER BY v.name;""", as_dict=1)
		df = pd.DataFrame.from_records(data)
		file_path = '/home/dhiraj/csv_files/test.csv'
		df.to_csv(file_path, index=False)  

		
	@frappe.whitelist()
	def execute_colab_code_cell(code):
		notebook_url = "https://cocalc.com/features/jupyter-notebook/"

		api_endpoint = f"{notebook_url}/api/execute"

		code = """
				import pandas as pd
				import pygwalker as pyg

				# Read data and generate pyg_walker
				file_path = '/home/dhiraj/csv_files/test.csv'
				df = pd.read_csv(file_path)
				pyg_walker = pyg.walk(df, hideDataSourceConfig=True, vegaTheme='g2')

				# Display pyg_walker
				print(pyg_walker)
				"""

		payload = {
			"code": code 
		}

		try:
			response = requests.post(api_endpoint, json=payload)
			if response.status_code == 200:
				return "Code cell executed successfully in Google Colab"
			else:
				return f"Error: {response.text}"
		except Exception as e:
			return f"Exception: {str(e)}"



	# @frappe.whitelist()
	# def my_template(doc):
	# 	app_path = frappe.get_app_path('library_department')
	# 	template_path = f"{app_path}/library_department/templates/pages/my_template.html"
	# 	try:
	# 		html_content = frappe.render_template(template_path, {'data': doc})
	# 		return html_content
	# 	except Exception as e:
	# 		frappe.throw(f"Error: {e}")



	# @frappe.whitelist()
	# def my_template(doc):
	# 	app_path = frappe.get_app_path('library_department')
	# 	template_path = f"{app_path}/library_department/templates/pages/my_template.html"
	# 	return frappe.render_template('/my_template.html', {'data': doc})



		# df = pd.read_csv(file_path)
		# pyg_walker = pyg.walk(df,hideDataSourceConfig=True,vegaTheme='g2')  
		# print('****************',pyg_walker)
		# return jsonify({"pyg_walk": pyg_walker})  

		








































		# self.get_pygwalker_data()
  #**************************************************************************************
  
	# def get_pygwalker_data():
	# 	data=frappe.db.sql("""select v.name1 as name,v.surname,v.age,f.name1 as child_name,f.relation from `tabVisualize Doc` as v join `tabFamily` as f ON v.name=f.parent ORDER BY v.name;""",as_dict=1)
	# 	df=pd.DataFrame.from_records(data)
	# 	print(df.to_csv('/home/dhiraj/csv_files/test.csv'))
	# 	df = pd.read_csv('/home/dhiraj/csv_files/test.csv')
	# 	st.set_page_config(
	# 		page_title = "USe Pygwalker in Streamlit",
	# 		layout = "wide"
	# 	)
	# 	st.title("use pygwalker in streamlit")
	# 	pyg_html = pyg.walk(df, return_html=True)
	# 	components.html(pyg_html,height=1000,scrolling=True)
		

   #**************************************************************************************
		# data=frappe.db.sql("""select v.name1 as name,v.surname,v.age,f.name1 as child_name,f.relation from `tabVisualize Doc` as v join `tabFamily` as f ON v.name=f.parent ORDER BY v.name;""",as_dict=1)
		# df=pd.DataFrame.from_records(data)
		# print(df.to_csv('/home/dhiraj/csv_files/test.csv'))
  
		# command = "streamlit run ./custom_app.py"
  
		# try:
		# 	subprocess.run(command,shell=True,check=True)
		# except subprocess.CalledProcessError as e:
		# 	print(f"Error : {e}")
   
   # ***********************************************************
  
  
  
  
  
  
  
  
  

  
  
		# get_pygwalker_output(walker)
		

		# @frappe.whitelist()
		# def get_pygwalker_output(walker):
		# 	pyg_output = walker.get_output()  # This method name might vary based on the PygWalker library
		# 	return {"pyg_output": pyg_output}








	# records = frappe.db.get_list('Visualize Doc')
		# print(records)
  
		# fields = [fieldname for fieldname in frappe.get_meta('Visualize Doc').fields]
		# print(fields)

		#************************************************************
		# doctype = 'Visualize Doc'
		# records = DatabaseQuery(doctype).execute()
		# print(records)

		# file_path = '/home/dhiraj/csv_files/visualizedoc.csv' 

		# records_data = []
  
		# for i in records:
		# 	records_data.append(i['name'])
   
		# print(records_data)

		# for record_name in records_data:
		# 	doc = frappe.get_doc('Visualize Doc', record_name)
		# 	print(doc)
		
		# print(f"Fields for {record_name}:")
  
		# for field in doc.fields:
		# 	print(f"{field}: {doc.get(field)}")
		# print('\n') 
		#**************************************************************
		#**************************************************************
  
  
		# list_of_records = frappe.db.get_list('Visualize Doc')
		# # print(list_of_records)
		# record_names = frappe.db.get_list('Visualize Doc', pluck='name')
		# # print(record_names)
  
		# for i in record_names:
		# 	# print(f"Fields for {i}: ")
		# 	doc = frappe.get_doc('Visualize Doc',str(i))
		# 	# print(doc.family_members_list)
   
		# 	parent_doctype = 'Visualize Doc'
		# 	parent_name = i

		# 	# Fetch the parent document
		# 	parent_doc = frappe.get_doc(parent_doctype, parent_name)

		# 	# Get all child table rows
		# 	if parent_doc.get('family_members_list'):
		# 		for child in parent_doc.get('family_members_list'):
		# 			child_doc = frappe.get_doc('Family', child.name)
		# 			print(f"Child Table Data: {child_doc.as_dict()}")
		# 	else:
		# 		print("No child table records found.")
  
#******************************************************************************************

		# parents=frappe.db.get_list('Visualize Doc',fields=['name','name1','surname','age'])
		# print(parents)
  
		# Child=frappe.db.get_list('Family',fields=['name','name1','relation'])
		# print(Child)
		#****************************************************************************************************
		# for parent in parents:
		# 	parent_doc = frappe.get_doc('Visualize Doc', parent.name)
		# 	# print(parent_doc)
		# 	print(f"Parent Record: {parent.name} - {parent.name1} {parent.surname}, Age: {parent.age}")
			
		# 	if parent_doc.family_members_list:
		# 		for child in parent_doc.family_members_list:
		# 			# print(child)
		# 			print(f"family members - Name: {child.name1}, Relation: {child.relation}")  
		# 	else:
		# 		print("child table empty")
#****************************************************************************************************
		#***************MAIN CODE**************************
  
		# parents=frappe.db.get_list('Visualize Doc',fields=['name','name1','surname','age'])
		# print(parents)
  		# data = {}

		# for parent in parents:
		# 	parent_doc = frappe.get_doc('Visualize Doc', parent.name)
		# 	parent_data = {
		# 		'Name': parent.name1,
		# 		'Surname': parent.surname,
		# 		'Age': parent.age,
		# 		'Children': []
		# 	}

		# 	if parent_doc.family_members_list:
		# 		for child in parent_doc.family_members_list:
		# 			child_data = {
		# 				'Name': child.name1,
		# 				'Relation': child.relation
		# 			}
		# 			parent_data['Children'].append(child_data)
			
		# 	data[parent.name] = parent_data
   
		  
		# df=pd.DataFrame.from_records(data)

		# print(df.to_csv('/home/dhiraj/csv_files/testmycsv.csv'))



















	# 	def convert_to_csv(self,VisualizeDoc,file_path ):            # ,file_path 
	
	# 	records = frappe.get_all(VisualizeDoc)

	# 	fields = [fieldname for fieldname in frappe.get_meta(VisualizeDoc).fields]

	# 	# with open(file_path, 'w', newline='') as csvfile:
	# 	# 	writer = csv.DictWriter(csvfile, fieldnames=fields)
	# 	# 	writer.writeheader()
	# 	# 	writer.writerows(records)

	# 	print(fields)

	# self.convert_to_csv('VisualizeDoc')                # , '/home/dhiraj/csv_files/visualizedoc.csv'





























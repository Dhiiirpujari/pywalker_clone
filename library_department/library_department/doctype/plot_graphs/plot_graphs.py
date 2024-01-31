# Copyright (c) 2023, NEW INDIA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import matplotlib
matplotlib.use('TkAgg')                  # Qt5Agg,WXAgg
import matplotlib.pyplot as plt
import pandas as pd

class PlotGraphs(Document):
	
	def validate(self):
		pass
  
	@frappe.whitelist()
	def get_fields_names(self):
		meta = frappe.get_meta(self.document)
		field_names = [field.fieldname for field in meta.fields]
		return field_names

	@frappe.whitelist()
	def get_fields_names_second(self):
		meta = frappe.get_meta(self.second_document)
		field_names = [field.fieldname for field in meta.fields]
		return field_names	

	@frappe.whitelist()
	def generate_graph(self,selected_graph_type):
		x = []
		y = []
		x2 = []
		y2 = []
  
		user_doc_selection = self.document
		second_doc_selection = self.second_document
		print("&&&&&&&&&&&&&",user_doc_selection)
		print("&&&&&&&&&&&&&",second_doc_selection)
  
  
		first_doctype_records_all = frappe.get_all(user_doc_selection)  
		print('***********',first_doctype_records_all)
  
		second_doctype_records_all = frappe.get_all(second_doc_selection)  
		print('***********',second_doctype_records_all)
  

		for i in first_doctype_records_all:
			field_values = frappe.get_doc(user_doc_selection,i['name'])
			x.append(frappe.db.get_value(user_doc_selection,i['name'],self.x_axis))
			y.append(frappe.db.get_value(user_doc_selection,i['name'],self.y_axis))
		print(x)
		print(y)
  
		for i in second_doctype_records_all:
			field_values = frappe.get_doc(second_doc_selection,i['name'])
			x2.append(frappe.db.get_value(second_doc_selection,i['name'],self.x_axis_second))
			y2.append(frappe.db.get_value(second_doc_selection,i['name'],self.y_axis_second))
		print(x2)
		print(y2)
    


		if selected_graph_type == 'scatter plots':
			plt.scatter(x, y)
			plt.scatter(x2, y2)
			plt.xlabel('X-axis Label')
			plt.ylabel('Y-axis Label')
			plt.title('Scatter Plot')
			plt.legend()
			plt.show()
		elif selected_graph_type == 'line plots':
			plt.plot(x, y)
			plt.plot(x2, y2)
			plt.xlabel('X-axis Label')
			plt.ylabel('Y-axis Label')
			plt.title('Line Plot')
			plt.legend()
			plt.show()
		elif selected_graph_type == 'bar plots':
			plt.bar(x, y)
			plt.bar(x2, y2, alpha=0.5)  
			plt.xlabel('X-axis Label')
			plt.ylabel('Y-axis Label')
			plt.title('Bar Plot')
			plt.legend()
			plt.show()
		elif selected_graph_type == 'area plots':
			plt.plot(x, y)
			plt.plot(x2, y2)
			plt.fill_between(x, y, y2, color='skyblue', alpha=0.5)
			plt.xlabel('X-axis Label')
			plt.ylabel('Y-axis Label')
			plt.title('Area Between Lines')
			plt.legend()
			plt.show()
		else:
			frappe.throw('Invalid graph type')



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

	# def generate_scatter_plot(self,x_values, y_values):          # scatter plot
	# 	plt.scatter(x_values, y_values)
	# 	plt.xlabel('X-axis Label')
	# 	plt.ylabel('Y-axis Label')
	# 	plt.title('Scatter Plot')
	# 	return plt.show()

	# def generate_line_plot(self,x_values, y_values):              # line plot
	# 	plt.plot(x_values, y_values)
	# 	plt.xlabel('X-axis Label')
	# 	plt.ylabel('Y-axis Label')
	# 	plt.title('Line Plot')
	# 	return plt.show()

	# def generate_bar_plot(self,x_values, y_values):    		      # bar plot
	# 	plt.bar(x_values, y_values)
	# 	plt.xlabel('X-axis Label')
	# 	plt.ylabel('Y-axis Label')
	# 	plt.title('Bar Plot')
	# 	return plt.show()



		# if selected_graph_type == 'scatter plots':
		# 	self.generate_scatter_plot(x, y)
		# elif selected_graph_type == 'line plots':
		# 	self.generate_line_plot(x, y)
		# elif selected_graph_type == 'bar plots':
		# 	self.generate_bar_plot(x, y)
		# else:
		# 	frappe.throw('Invalid graph type')



# doctype_name = self.document
		# meta = frappe.get_meta(doctype_name)
		# field_names = [field.fieldname for field in meta.fields]
		# print(field_names)      # fields present in that perticular doctype

		# def get_document_records(self,selected_document):
		# 	records = frappe.get_all(selected_document, fields=['name'])
		# 	print([record['name'] for record in records])
  
  
  	# self.get_document_records(user_doc_selection)
		# print(self.x_axis)
		# print(self.y_axis)
		# print(self.graph_type)
  
		


		# x_axis_field = frappe.get_value('PlotGraphs', filters={'name': 'Data for graph'}, fieldname='x_axis')
		# y_axis_field = frappe.get_value('PlotGraphs', filters={'name': 'Data for graph'}, fieldname='y_axis')

		# doctype_records = frappe.get_all('Data for graph', fields=[x_axis_field, y_axis_field])
		# print('********',doctype_records)  
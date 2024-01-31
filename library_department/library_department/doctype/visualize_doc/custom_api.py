from flask import Flask, jsonify, current_app
from visualize_doc import VisualizeDoc  # Import VisualizeDoc from your module

app = Flask(__name__)

@app.route('/get_pyg_data', methods=['GET'])
def get_pyg_data():
    with app.app_context():
        # Fetch data and generate PyGwaker output
        pyg_walker = VisualizeDoc().generate_pyg_walk_api()  # Assuming VisualizeDoc is your Frappe document

        # Convert PyGwaker output to a format suitable for JSON serialization
        # For instance, convert pyg_walker to a JSON-compatible dictionary
        pyg_data = {"pyg_walker_data": pyg_walker}

        return jsonify(pyg_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)





































































# data=frappe.db.sql("""select v.name1 as name,v.surname,v.age,f.name1 as child_name,f.relation from `tabVisualize Doc` as v join `tabFamily` as f ON v.name=f.parent ORDER BY v.name;""",as_dict=1)
# df=pd.DataFrame.from_records(data)
# print(df.to_csv('/home/dhiraj/csv_files/test.csv'))

# data=frappe.db.sql("""select v.name1 as name,v.surname,v.age,f.name1 as child_name,f.relation from `tabVisualize Doc` as v join `tabFamily` as f ON v.name=f.parent ORDER BY v.name;""",as_dict=1)
# df=pd.DataFrame.from_records(data)
# print(df.to_csv('/home/dhiraj/csv_files/test.csv'))
# df = pd.read_csv('/home/dhiraj/csv_files/test.csv')
# pyg_html = pyg.walk(df)
# return pyg_walk


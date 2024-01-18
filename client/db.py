from flet import *
from controls import return_control_reference
from form_helper import FormHelper
import requests
import json

control_map = return_control_reference()

class Database():
    
    def load_data(self, order="id"):
        control_map["AppDataTable"].controls[0].controls[0].rows.clear()
        if order == "fio":
            response = requests.get('http://server:5000/api/v1.0/tasks=order')
        else:
            response = requests.get('http://server:5000/api/v1.0/tasks')
        json_data = json.dumps(response.json())
        rows = json.loads(json_data)
        for row in rows:
            data = DataRow(cells=[])
            for val in row:
                data.cells.append(
                    DataCell(FormHelper(val))     
                )
            control_map["AppDataTable"].controls[0].controls[0].rows.append(data)
        control_map["AppDataTable"].controls[0].controls[0].update()

    def write(self, data):
        json_data = {"cab":data[0], "fio":data[1], "description":data[2]}
        response = requests.post('http://server:5000/api/v1.0/tasks', json=json_data)
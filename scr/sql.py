import sqlite3
from flet import *
from controls import return_control_reference
from form_helper import FormHelper

control_map = return_control_reference()

class Database():
    def __init__(self) -> None:
        self.connection = sqlite3.connect('pj_database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Jobs (
            id INTEGER PRIMARY KEY,
            cab TEXT NOT NULL,
            fio TEXT NOT NULL,
            description TEXT NOT NULL
            )'''
                       )
    def write(self, data):
        sql = "INSERT INTO Jobs (cab, fio, description) VALUES (?, ?, ?)"
        self.cursor.execute(sql,data)
        self.connection.commit()

    def load_data(self, order="id"):
        sql = "SELECT id, cab, fio, description FROM Jobs ORDER BY " + order 
        self.cursor.execute(sql)
        bd_data = self.cursor.fetchall()
        control_map["AppDataTable"].controls[0].controls[0].rows.clear()
        for row in bd_data:
            data = DataRow(cells=[])
            for val in row:
                data.cells.append(
                    DataCell(FormHelper(val))     
                )
            control_map["AppDataTable"].controls[0].controls[0].rows.append(data)
        control_map["AppDataTable"].controls[0].controls[0].update()

    def __del__(self):
        self.connection.close()
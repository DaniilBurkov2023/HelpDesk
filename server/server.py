from flask import Flask, jsonify, request
from sql import Db

app = Flask(__name__)

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    db = Db()
    data = db.get()
    return jsonify(data), 201

@app.route('/api/v1.0/tasks=order', methods=['GET'])
def get_tasks_by_order():
    db = Db()
    data = db.get("fio")
    return jsonify(data), 201

@app.route('/api/v1.0/tasks', methods=['POST'])
def create_task():
    db = Db()
    task = [request.json.get('cab', ""), request.json.get('fio', ""), request.json.get('description', "")]
    db.write(task)
    return jsonify({"task":task}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
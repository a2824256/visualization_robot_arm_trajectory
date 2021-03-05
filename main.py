from flask import Flask, abort, request, jsonify, render_template
import sqlite3
import os
from flask_cors import *
app = Flask(__name__)
sqlite_path = './data'
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    global sqlite_path
    path = request.form.get('path')
    dirs_arr = []
    for root, dirs, files in os.walk(sqlite_path):
        for dir in dirs:
            dirs_arr.append(os.path.join('.', 'data', dir, 'ArmData.db'))
    print("path:", path)
    if path is None:
        temp_path = dirs_arr[0]
        print('None')
    else:
        temp_path = path
    conn = sqlite3.connect(temp_path)
    cursor = conn.cursor()
    sql = "select * from ArmData"
    values = cursor.execute(sql)
    data = {}
    data['data'] = []
    for i in values:
        data['data'].append([i[0], i[1], i[2]])
    # data['len'] = len(data['data'])
    data['dirs'] = dirs_arr
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8383, debug=True)
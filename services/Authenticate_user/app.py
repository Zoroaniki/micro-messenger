from flask import Flask, render_template, request, redirect, url_for, session, jsonify,make_response
import pymysql
import mysql.connector
import requests
from uuid import uuid4
import json

app = Flask(__name__, template_folder='Templates')
app.secret_key = 'your_secret_key'


# Настройка подключения к базе данных
def get_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3306',
                                             database='users',
                                             user='root',
                                             password='AFDG56478')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Подключено к серверу MySQL версии", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Вы подключены к базе данных:", record)
            return connection

    except Exception as ex:
        print("Ошибка при подключении к MySQL")
    '''
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Соединение с MySQL закрыто")
    '''


@app.route('/success')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        number = request.form['number']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT uuid FROM users WHERE name = %s AND pass = %s AND number = %s", (username, password, number))
        user = cursor.fetchone()
        if user:
            uuid = user
            session['uuid'] = uuid
            return redirect('http://localhost:8001/poisk')
        else:
            return 'Invalid username or password'
    return render_template('login.html')


@app.route('/users/<id>', methods=['GET', 'POST'])
def ilya(id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = {} ".format(id))
    user = cursor.fetchone()
    print(user)
    r = json.dumps(user)
    return r


def send_request(url="http://127.0.0.1:5000/poisk"):
    response = requests.get(url="0.0.0.0:8001/poisk")
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        number = request.form['number']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, pass, number, uuid) VALUES (%s, %s, %s, %s)", (username, password, number, str(uuid4())))
        conn.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8002)




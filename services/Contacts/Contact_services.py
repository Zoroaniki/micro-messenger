from flask import Flask, render_template, request, redirect, url_for, make_response, session
import pymysql
import os
from dotenv import load_dotenv, dotenv_values
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'
load_dotenv()

user = os.getenv("BD_USER_NAME")
password = os.getenv("BD_PASSWORD")
bd_name = os.getenv("BD_NAME")
print(user)
print(password)
print(bd_name)


def get_bd_conectin():
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user=user,
            password=password,
            database=bd_name,
            cursorclass=pymysql.cursors.DictCursor,
        )
    except Exception as ex:
        print("Connection refuse")
        print(ex)
    return connection

def get_db():
    pass


def create_table_if_not_exists():
    connection = get_bd_conectin()
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'users_friends'")
    if cursor.fetchone() is None:
        cursor.execute("""
            CREATE TABLE users_friends (
                friends_id INT,
                user_id varchar(255)
            )
        """)
        print("Таблица users создана")
    else:
        print("Таблица users уже существует")
        '''
        try:

            # Добавление в таблицу информации
            
            with connection.cursor() as cursor:
                insert_user = "INSERT INTO users (id_users, number_users, name_users) VALUE ('1', 1111, 'Anna');"
                cursor.execute(insert_user)
                connection.commit()



            with connection.cursor() as cursor:
                insert_user = "INSERT INTO users (id_users, number_users, name_users) VALUE ('22', 89132482, 'Max');"
                cursor.execute(insert_user)
                connection.commit()
            

            # Извлечение из таблицы данных
            with connection.cursor() as cursor:
                select_row = "SELECT * FROM users;"
                cursor.execute(select_row)
                rows = cursor.fetchall()
           
      
        finally:

            connection.close()
            print("successfully connection")
        
        return connection
'''


@app.route("/poisk")
def index():
    connection = get_bd_conectin()
    uuid = session.get('uuid')
    print(uuid)
    if uuid:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE uuid != %s", (uuid,))
            rows = cursor.fetchall()
            return render_template('poisk.html', rows=rows)
    else:
        return 'UUID not found in session'


@app.route('/friends', methods=['GET', 'POST'])
def friends():
    if request.method == 'POST':
        user_id = request.form.get('id')
        connection = get_bd_conectin()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO friends (id_friends, name_friends, number_friends) SELECT id, name, number FROM users WHERE id = %s;",
            (user_id,))
        connection.commit()
        return redirect(url_for('friends'))
    connection = get_bd_conectin()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM friends")
    friends = cursor.fetchall()
    return render_template('friends.html', friends=friends)


@app.route('/chat', methods=['GET', 'POST'])
def chatuser():
    conn = get_bd_conectin()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM friends")
    friends = cursor.fetchall()
    return render_template('chat.html', friends=friends)



@app.route('/users/<id>', methods=['GET', 'POST'])
def ilya(id: int):
    conn = get_bd_conectin()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM friends WHERE id_friends = {}".format(id))
    user = cursor.fetchone()
    return user["name_friends"]

def create_chat(partisipants: [], name: "str"):
    requests_data = ""
    for partisipant in partisipants:
        request_data += "user=" + str(partisipant) + "&"
    requests_data += "name={}".format(name)
    requests.post("http://0.0.0.0:8000/create_chat?{}".format(request_data))


def request_uuid(user_id: int):
    response = requests.get("http://0.0.0.0:8002/user/{}/uuid".format(user_id))
    return response.text
if __name__ == "__main__":
    create_table_if_not_exists()
    app.run(debug=True, host="0.0.0.0", port=8001)

from flask import Flask, render_template, request, redirect, url_for, make_response, session
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv, dotenv_values
import requests
import json
import sys

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app, supports_credentials=True)
load_dotenv()

user = os.getenv("BD_USER_NAME")
password = os.getenv("BD_PASSWORD")
bd_name = os.getenv("BD_NAME")
redirect_address = os.getenv("REDIRECT_ADDRESS")
print(user)
print(password)
print(bd_name)


def get_bd_conectin():
    try:
        connection = pymysql.connect(
            host="62.217.187.32",
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

@app.route("/to_poisk")
def find_users():
    return redirect("{}:8001/poisk".format(redirect_address))

@app.route("/to_friend")
def to_friends():
    return redirect("{}:8001/friends".format(redirect_address))

@app.route('/friends', methods=['GET', 'POST'])
def friends():
    uuid = session.get('uuid')
    print(uuid)
    if request.method == 'POST':
        users_id = request.form.get('id')
        print(users_id)
        connection = get_bd_conectin()
        cursor = connection.cursor()
        #cursor.execute("INSERT INTO friends (id_friends, name_friends, number_friends) SELECT id, name, number FROM users WHERE id = %s;",(users_id,))
        cursor.execute("SELECT id from users WHERE id = %s", (users_id))
        save_id_f = cursor.fetchall()
        save_id_f_value = save_id_f[0]['id']
        cursor.execute("INSERT INTO users_friends (user_id, friends_id) VALUES (%s, %s)", (uuid, save_id_f_value))
        connection.commit()
        return redirect(url_for('friends'))
    connection = get_bd_conectin()
    cursor = connection.cursor()
    cursor.execute("SELECT name, id FROM users WHERE id IN (SELECT friends_id FROM users_friends WHERE user_id = %s)", (uuid,))
    friends = cursor.fetchall()
    print("friends: {}".format(friends), file=sys.stderr)
    print(get_current_user_id(), file=sys.stderr)
    chats = request_chat(get_current_user_id())
    print(type(chats), file=sys.stderr)
    print(chats, file=sys.stderr)
    print("json {}".format(json.loads(chats)), file=sys.stderr)

    
    return render_template('friends.html', friends=friends, chats=json.loads(chats))


#@app.route('/chat', methods=['GET', 'POST'])
#def chatuser():
    #conn = get_bd_conectin()
    #cursor = conn.cursor()
    # cursor.execute("SELECT * FROM friends")
    #friends = cursor.fetchall()
#    return render_template('chat.html', friends=friends)

def get_current_user_id():
    connection = get_bd_conectin()
    cursor = connection.cursor()
    uuid = session.get('uuid')
    print("uuid: {}".format(uuid), sys.stderr)
    cursor.execute("SELECT users.id FROM users WHERE uuid = %s", (uuid,))
    user = cursor.fetchall()
    cursor.execute("SELECT * FROM users")
    cursortest = cursor.fetchall()
    print("aaaaa: {}".format(cursortest), sys.stderr)
    print(user, file=sys.stderr)
    return user[0]["id"]

@app.route('/users/<int:id>')
def give_user_name(id: int):
    connection = get_bd_conectin()
    cursor = connection.cursor()
    cursor.execute("SELECT users.name FROM users WHERE id = %s", (id,))
    user = cursor.fetchall()
    print("user: {}".format(user), file=sys.stderr)
    return user[0]["name"]


@app.route('/test/<int:id>', methods=['POST', 'GET'])
def ilya(id: int):
    partisipants = []
    partisipants.append(id)
    partisipants.append(get_current_user_id())
    print(id, file=sys.stderr)
    create_chat(partisipants, "")
    return redirect('{}:8001/friends'.format(redirect_address))

@app.route('/chat/<int:id>', methods=['GET', 'POST'])
def go_to_chat(id: int):
    print("Chat_id: {}".format(id), file=sys.stderr)
    session['uuid'] = session.get('uuid')
    return redirect("{}:8000/api/{}".format(redirect_address, id))

def request_chat(user_id: int):
    response = requests.get("{}:8000/api/get_chats/{}".format(redirect_address, user_id))
    return response.text

def create_chat(partisipants: [], name: str):
    request_data = ""
    print(partisipants, file=sys.stderr)
    for partisipant in partisipants:
        request_data += "user=" + str(partisipant) + "&"
    request_data += "name={}".format(name)
    print(request_data, file=sys.stderr)
    requests.post("{}:8000/api/create_chat?{}".format(redirect_address, request_data))


def request_uuid(user_id: int):
    response = requests.get("{}:8002/user/{}/uuid".format(redirect_address, user_id))
    return response.text
if __name__ == "__main__":
    create_table_if_not_exists()
    app.run(debug=True, host="0.0.0.0", port=8001)

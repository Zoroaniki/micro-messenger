from flask import Flask, render_template, request, redirect, url_for
from config import host, db_name, user, password
import pymysql
import requests

app = Flask(__name__)


def get_bd_conectin():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
        )

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
        '''

        return connection


    except Exception as ex:
        print("Connection refuse")
        print(ex)





@app.route("/poisk")
def index():
    connection = get_bd_conectin()
    with connection.cursor() as cursor:
        select_row = "SELECT * FROM users;"
        cursor.execute(select_row)
        rows = cursor.fetchall()
        return render_template('index.html', rows=rows)


@app.route('/friends', methods=['GET', 'POST'])
def friends():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        connection = get_bd_conectin()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO friends (id_friends, name_friends, number_friends) SELECT id_users, name_users, number_users FROM users WHERE id_users = %s;",
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


def send_request(url="http://62.217.187.32:8000/api/messages"):
    response = requests.get(url="http://62.217.187.32:8000/api/messages")
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/users/<id>', methods=['GET', 'POST'])
def ilya(id: int):
    conn = get_bd_conectin()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM friends WHERE id_friends = {}".format(id))
    user = cursor.fetchone()
    return user["name_friends"]


if __name__ == "__main__":
    app.run(debug=True)

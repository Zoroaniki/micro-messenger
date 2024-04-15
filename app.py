import Creator
import sqlalchemy as SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'There was an issue adding your account'
    else:
        return render_template('register.html')


@app.route('/login')
def login():
    return "Login Page"


def writedb():
    db = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="250702",
        database="users"
    )

    # Создание курсора
    cursor = db.cursor()

    # SQL запрос для создания таблицы
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    );
    """

    # Выполнение запроса
    cursor.execute(sql_create_table)

    # Подтверждение изменений
    db.commit()

    print("Таблица создана успешно.")

    # Подготовка данных для вставки
    data = [
        ("John Doe", "25asd"),
        ("Jane Doe", "26asd"),
        ("Denis", "qwerty321")
    ]

    # SQL запрос для вставки данных
    sql_insert_data = "INSERT INTO users (name, pass) VALUES (%s, %s)"

    # Выполнение запроса для каждой строки данных
    cursor.executemany(sql_insert_data, data)

    # Подтверждение изменений
    db.commit()

    print(cursor.rowcount, "записей вставлено.")

    cursor.close()
    db.close()


if __name__ == '__main__':
    app.run(debug=True)

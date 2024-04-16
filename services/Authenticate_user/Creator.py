import mysql.connector

def create():
        # Подключение к базе данных
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
        phone VARCHAR(255) NOT NULL UNIQUE
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


import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='users',
                                         user='root',
                                         password='250702')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Подключено к серверу MySQL версии", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Вы подключены к базе данных:", record)

except Error as e:
    print("Ошибка при подключении к MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Соединение с MySQL закрыто")


import bcrypt
from socket import create_connection


def authenticate_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result is not None:
        stored_password = result[0]
        return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
    else:
        return False

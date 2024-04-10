from socket import create_connection


def authenticate_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result is not None

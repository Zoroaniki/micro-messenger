# Работы по микросервисам

Для корректной работы необходимо создать бд:
'''
CREATE DATABASE users;
USE users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    pass VARCHAR(45) NOT NULL,
    number VARCHAR(45) NOT NULL,
    uuid VARCHAR(255) NOT NULL
);

CREATE TABLE friends (
    id_friends INT AUTO_INCREMENT PRIMARY KEY,
    name_friends TEXT,
    number_friends TEXT
);

CREATE DATABASE chat_service_db;
'''

также необходимо добавить .env файл в каждый сервис с таким содержанием:
'''
BD_USER_NAME="имя пользователя бд"
BD_PASSWORD="пароль"
BD_NAME="название бд" # для chat_service chat_service_db, для остальных users
REDIRECT_IP=""
HOST="0.0.0.0"
def main():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if authenticate_user(username, password):
        print("Авторизация успешна!")
    else:
        print("Неверное имя пользователя или пароль.")


if __name__ == "__main__":
    main()

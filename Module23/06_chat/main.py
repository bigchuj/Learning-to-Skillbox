# TODO здесь писать код


import json
from textwrap import indent


def registration_users():

    global login
    if not login:

        while True:
            login = input("Введите логин: ")

            if login in identificaton:
                print("Данный логин уже используется, попробуйте другой.\n")
                continue
            break

    password = input("Введите пароль: ")
    identificaton[login] = password

    with open("data.json", "w", encoding="utf-8") as data:
        json.dump(identificaton, data, indent=4)

    print("Регистрация пройдена успешно.")

    return True


def verification():

    global login
    while True:

        login = input("Введите логин: ")

        if login in identificaton:

            while True:

                password = input("Введите пароль: ")

                if password == identificaton[login]:
                    print("Авторизация пройдена успешно.")
                    return True

                elif password == "n":
                    print("Авторизация прервана.")
                    return False

                else:
                    print("Введен неверный пароль. \
Повторите снова или нажмите 'n' для выхода.")

        else:
            print("Пользователь не найден.")
            option = input(
                "Введите 'r' для регистрации, 'n' для выхода, любую кнопку для повторной попытки входа: ")

            if option == "r":
                return registration_users()

            elif option == "n":
                print("Авторизация прервана.")
                return False

            else:
                continue


def help():

    return """
Для работы используйте следующие команды:
help (h) - вызов справки по командам
chat (c) - посмотреть/обновить сообщения чата
message (m) - отправить сообщение в чат
user (u) - сменить пользователя\n
"""


def options(option):

    if option in ("help", "h", "р"):
        return help()
    elif option in ("chat", "c", "с"):
        return chat()
    elif option in ("message", "m", "ь"):
        return message()


def chat():

    try:

        with open("chat.txt", "r", encoding="utf-8") as ch:
            print()
            for line in ch:
                print(line)

            return "~Конец чата~\n"

    except FileNotFoundError:
        return "Чат пустой, выберете команду 'message' или 'm', чтобы ввести сообщение"


def message():

    with open("chat.txt", "a", encoding="utf-8") as ch:
        message_inp = input("\nВведите текст сообщения: ")
        ch.write(f"{login}:\n{message_inp}\n\n")

    return "\n~Сообщение отправлено~\n"


def welcome():

    print("Добро пожаловать в наш мессенджер.")
    print(help())
    print("Для начала вам нужно авторизоваться")

    option = input("Вы зарегистрированы? (да/нет) ").lower()

    return verification() if option in ("да", "lf") else registration_users()


def menu():

    welc = welcome()

    while welc:
        option = input("Введите команду: ").lower()

        if option in ("user", "u", "г"):
            return True

        print(options(option))

    return False


with open("data.json", "r", encoding="utf-8") as data:
    identificaton = json.load(data)

while True:

    login = None
    menu()

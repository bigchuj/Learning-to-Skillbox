# TODO здесь писать код


def search_contact(surname):

    found_contacts = list()
    for names in contacts.keys():
        if surname[:-2] in names[1]:
            found_contacts.append((*names, contacts[names]))

    return found_contacts


contacts = dict()

while True:
    action = input("""Введите номер действия:
 1. Добавить контакт
 2. Найти человека
""")

    if action == "1":
        names = tuple(
            input(
                "Введите имя и фамилию нового контакта (через пробел): ").title().split()
        )
        if contacts.get(names):
            print("Такой человек уже есть в контактах.")

        else:
            number = int(input("Введите номер телефона: "))
            contacts[names] = number

        print("Текущий словарь контактов:", contacts)

    elif action == "2":
        surname = input("Введите фамилию для поиска: ").title()

        result_search = search_contact(surname)
        if result_search:
            [print(*contact) for contact in result_search]
        else:
            print("Такого контакта нет в телефонной книге.")

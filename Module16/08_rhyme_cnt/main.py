# TODO здесь писать код

quantity_peoples = [
    i + 1 for i in range(int(input("Кол-во человек: ")))
]
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number}-й человек")
i_number_people = 0


def correct_i_number(i_number, list_):

    while i_number >= len(list_):
        i_number -= len(list_)

    return i_number


while len(quantity_peoples) != 1:

    print("\nТекущий круг людей:", quantity_peoples)
    print("Начало счёта с номера", quantity_peoples[i_number_people])
    # новый индекс:
    if len(quantity_peoples) < number:

        i_number_people = number % len(quantity_peoples) - 1 + i_number_people
        i_number_people = correct_i_number(i_number_people, quantity_peoples)

    else:
        i_number_people += number - 1
        i_number_people = correct_i_number(i_number_people, quantity_peoples)

    print("Выбывает человек под номером", quantity_peoples[i_number_people])
    quantity_peoples.remove(quantity_peoples[i_number_people])
    i_number_people = correct_i_number(i_number_people, quantity_peoples)

print("\nОстался человек под номером", *quantity_peoples)

from operator import le


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:

    print("Сейчас на вечеринке", len(guests), "человек:", guests)
    variant = input("Гость пришёл или ушёл? ").lower()

    if variant == "пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break

    elif not guests and variant == "ушел":
        print("Некому уходить, дом пуст!")
        break


    name_guest = input("Имя гостя: ").capitalize()

    if variant == "пришел":

        if len(guests) < 6:

            guests.append(name_guest)
            print(f"Привет, {name_guest}!\n")

        else:
            print(f"Прости, {name_guest}, но мест нет.\n")

    elif variant == "ушел":
        
        if guests:

            guests.remove(name_guest)
            print(f"Пока, {name_guest}!\n")

    


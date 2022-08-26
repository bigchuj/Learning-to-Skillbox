# TODO здесь писать код

numbers = {
    0: "Первая", 1: "Вторая",
    2: "Третья", 3: "Четвертая",
    4: "Пятая", 5: "Шестая",
    6: "Седьмая", 7: "Восьмая",
    8: "Девятая", 9: "Десятая"
}

quantity_coup = int(input("Введите количество пар слов: "))
words_synonims = dict()

for i in range(quantity_coup):
    temp_couple = input(f"{numbers[i]} пара: ").split("-")
    words_synonims[temp_couple[0].strip().capitalize()] =\
        temp_couple[1].strip().capitalize()

while True:
    word = input("\nВведите слово: ").capitalize()

    for item in words_synonims.items():
        item = list(item)
        if word in item:
            item.pop(item.index(word))
            print("Синоним: {}".format(*item))
            break
    else:
        print("Такого слова в словаре нет.")
        continue

    break

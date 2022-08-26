# TODO здесь писать код

numbers = {
    0: ["Первая", "Первый"], 1: ["Вторая", "Второй"],
    2: ["Третья", "Третий"], 3: ["Четвертая", "Четвертый"],
    4: ["Пятая", "Пятый"], 5: ["Шестая", "Шестой"],
    6: ["Седьмая", "Седьмой"], 7: ["Восьмая", "Восьмой"],
    8: ["Девятая", "Девятый"], 9: ["Десятая", "Десятый"]
}

quantity_country = int(input("Количество стран: "))
citys = dict()

for i in range(quantity_country):

    country = input(f"{numbers[i][0]} страна: ").lower().split()
    citys[country[0]] = country[1:]

for j in range(3):

    city = input(f"\n{numbers[j][1]} город: ").lower()

    for city_item in citys.keys():
        if city in citys[city_item]:
            print(
                f"Город {city.capitalize()} расположен в стране {city_item.capitalize()}."
            )
            break
    else:
        print(f"По городу {city.capitalize()} данных нет.")

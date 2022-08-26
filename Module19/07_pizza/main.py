# TODO здесь писать код


numbers = {
    0: "Первый", 1: "Второй",
    2: "Третий", 3: "Четвертый",
    4: "Пятый", 5: "Шестой",
    6: "Седьмой", 7: "Восьмой",
    8: "Девятый", 9: "Десятый"
}

quantity = int(input("Введите количество заказов: "))
orders = dict()

for i in range(quantity):
    order = input(f"{numbers[i]} заказ: ").split()

    if order[0] in orders:

        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] += int(order[2])

        else:
            orders[order[0]][order[1]] = int(order[2])

    else:
        orders[order[0]] = dict()
        orders[order[0]][order[1]] = int(order[2])

print("\n")
for name in sorted(orders.keys()):
    print(f"{name}:")

    for food, quantity_food in sorted(orders[name].items()):
        print(f"\t{food}: {quantity_food}")

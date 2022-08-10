# TODO здесь писать код

size_skates =[
    int(
        input(f"Размер {i + 1}-й пары: ")
    ) for i in range(int(input("Кол-во коньков: ")))
]

size_legs =[
    int(
        input(f"Размер ноги {i + 1}-го человека: ")
    ) for i in range(int(input("\nКол-во людей: ")))
]

count = 0
for leg in size_legs:
    for skate in size_skates:
        if leg <= skate:
            size_skates.remove(skate)
            count += 1

print("\nНаибольшее кол-во людей, которые могут взять ролики:", count)
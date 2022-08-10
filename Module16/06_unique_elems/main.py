# TODO здесь писать код

first_numbers =[
    int(
        input(f"Введите {i + 1}-е число для первого списка: ")
    ) for i in range(3)
]
copy_first_numbers = first_numbers[:]

second_numbers =[
    int(
        input(f"Введите {i + 1}-е число для второго списка: ")
    ) for i in range(7)
]

first_numbers.extend(second_numbers)

for i in first_numbers:
    for _ in range(first_numbers.count(i) - 1):
        first_numbers.remove(i)


print("\nПервый список:", copy_first_numbers)
print("Второй список:", second_numbers)
print("\nНовый первый список с уникальными элементами:", first_numbers)

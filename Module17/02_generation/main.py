# TODO здесь писать код

numbers = [
    (i % 5 if i % 2 else 1)
    for i in range(int(input("Введите длину списка: ")))
]

print("Результат:", numbers)

# TODO здесь писать код

numbers = [
   int(input("Число: ")) for _ in range(int(input("Кол-во чисел: ")))
]


def func(list_):
    new_numbers = []
    # защита от спика длиной менее 1 элемента
    # в таком случае будет возвращаться просто список
    if len(list_) > 1:

        if list_[-1] == list_[-2]:
            new_numbers = list_[-3::-1]
        else:
            new_numbers = list_[-2::-1]

    return new_numbers, len(new_numbers)


print("Последовательность:", numbers)
new_numbers, num = func(numbers)
print("Нужно приписать чисел:", num)
print("Сами числа:", new_numbers)

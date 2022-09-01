# TODO здесь писать код

from random import randint

# вариант 1
numbers = [randint(0, 9) for _ in range(10)]
new_numbers = []

temp_nums = []
for num in numbers:
    temp_nums.append(num)

    if len(temp_nums) == 2:
        new_numbers.append(tuple(temp_nums))
        temp_nums.clear()

print("Оригинальный список:", numbers)
print("Новый список:", new_numbers)


# вариант 2 - здесь код покомпактнее получился
numbers = [randint(0, 9) for _ in range(10)]
new_numbers = [
    (i, j) for i, j in zip(
        [numbers[k] for k in range(0, 10, 2)],
        [numbers[n] for n in range(1, 10, 2)]
    )
]

print("Оригинальный список:", numbers)
print("Новый список:", new_numbers)

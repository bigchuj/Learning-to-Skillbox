# TODO здесь писать код
from random import randint

numbers = [
    randint(0, 2) for _ in range(int(input("Количество чисел в списке: ")))
]
print("Список до сжатия:", numbers)

while 0 in numbers:
    numbers.remove(0)

print("Список после сжатия:", numbers)

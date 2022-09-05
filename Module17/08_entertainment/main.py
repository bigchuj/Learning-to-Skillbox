# TODO здесь писать код

from random import randint


sticks = "I" * int(input("Количество палок: "))
throws = int(input("Количество бросков: "))

for i in range(throws):

    left_i = randint(1, len(sticks))
    right_i = randint(left_i, len(sticks))
    print(f"Бросок {i + 1}. Сбиты палки с номера {left_i}\nпо номер {right_i}.")

    sticks = sticks[:left_i - 1] + '.' * \
        (right_i - left_i + 1) + sticks[right_i:]

print("\nРезультат:", sticks)

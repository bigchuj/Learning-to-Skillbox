# TODO здесь писать код

def summ_numbers(num):
    summ = 0
    while num:
        summ += num % 10
        num //= 10

    return summ


def count_numbers(num):
    count = 0
    while num:
        count += 1
        num //= 10

    return count


num = int(input("Введите число: "))
print("Сумма чисел:", summ_numbers(num))
print("Количество цифр в числе:", count_numbers(num))
print(
    "Разность суммы и количества цифр:",
    summ_numbers(num) - count_numbers(num)
)

# TODO здесь писать код

def reverse_number(num):
    num = int(num)
    new_num = 0

    while num:
        new_num = new_num * 10 + num % 10
        num //= 10

    return new_num


def reverse_number_remains(num):
    new_num = reverse_number(
        round(num - int(num), 2) * 100
    )
    new_num /= 100

    return new_num


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num1 = reverse_number(num1) + reverse_number_remains(num1)
num2 = reverse_number(num2) + reverse_number_remains(num2)

print("Первое число наоборот:", num1)
print("Второе число наоборот:", num2)
print("Сумма:", num1 + num2)

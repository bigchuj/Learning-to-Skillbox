# TODO здесь писать код


def operations(operation: str, f_num: int, s_num: int):

    if operation == "+":
        return f_num + s_num

    elif operation == "-":
        return f_num - s_num

    elif operation == "*":
        return f_num * s_num

    elif operation == "/":
        return f_num / s_num


def error_corrected(line):

    option = input(
        f"Обнаружена ошибка в строке: {line}   Хотите исправить? "
    ).lower()

    return True if option == "да" else False


with open("calc.txt", "r") as calc:

    total = 0

    for line in calc:

        temp_values = line.split()
        first_num = int(temp_values[0])
        second_num = int(temp_values[2])
        operation = temp_values[1]

        try:

            if len(operation) > 1:
                raise BaseException

        except BaseException:

            if error_corrected(line.rstrip("\n")):
                operation = input("Введите исправленную строку: ").split()[1]

            else:
                continue

        total += operations(operation, first_num, second_num)

    print("Сумма результатов:", total)

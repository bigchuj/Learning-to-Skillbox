# TODO здесь писать код

from random import randint


total_num = 0

try:
    while total_num < 777:
        temp_num = int(input("Введите число: "))

        random_num = randint(1, 13)

        with open("out_file.txt", "a") as out_file:
            out_file.write("{}".format(str(temp_num)))
            out_file.write("\n")
        
        if random_num == 1:
            raise BaseException

        total_num += temp_num

    else:
        print("Вы успешно выполнили условие для выхода из порочного цикла!\n")

except BaseException:
    print("Вас постигла неудача!")

finally:

    print("Содержимое файла out_file.txt:")
    try:
        with open("out_file.txt", "r") as out_file_print:
            print(out_file_print.read())

    except FileNotFoundError:
        print("В файл не записано никаких значений.")

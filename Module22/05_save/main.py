# TODO здесь писать код


import os


def verify_dirrectory(dir_way):

    if os.path.exists(os.path.join("C:\\", *dir_way)):
        return dir_way

    else:
        print("Такой путь на диске не существует. Введите верный путь.\n")
        return way_input()


def way_input(dir_way=None):

    dir_way = input(
        "Куда хотите сохранить документ?\
 Введите последовательность папок (через пробел):\n"
    ).split()

    return verify_dirrectory(dir_way)


def save_file():

    text = input("Введите строку: ")
    dir_way = way_input()
    name_file = input("Введите имя файла: ") + ".txt"
    dir_way.append(name_file)
    way_file = os.path.join("C:\\", *dir_way)


    if os.path.exists(way_file):
        option = input("Вы действительно хотите перезаписать файл? ").lower()

        if option == "да":
            file_rewrite = open(way_file, "w")
            file_rewrite.write(text)
            file_rewrite.close()
            print("Файл успешно перезаписан!")

        else:  # option == "нет"
            file_add = open(way_file, "a")
            file_add.write("\n" + text)
            file_add.close()
            print("Текст успешно добавлен в файл.")

    else:  # если файл в директории отсутствует
        file_write = open(way_file, "w")
        file_write.write(text)
        file_write.close()
        print("Файл успешно сохранён!")

    file_open = open(way_file, "r")
    print(f"\nСожержимое файла {name_file}:\n{file_open.read()}")
    file_open.close()


save_file()

# вопрос - было бы целесообразнее чтобы пользователь вводил абсолютный путь?
# после преобразования в список, брать первый элемент - 
# наименование диска, добавлять два слеша \\ и в конструкциях os.path.join()
# первым элементом передавать наименование диска?
# просто я указал по умолчанию диск С:\\, только он же не у всех задан по умолчанию
# и по идее программа должна определять самостоятельно где находится 
# вводимый путь. Конструкция os.path.abspath(path), у меня не стработала? а может 
# я неправильно использовал ее, направьте на пусть истинный
# путь: "Users sergei.chuev Desktop Обучение Python_SkillBox Python_Basic-1 Module22 05_save_25"

# у меня получается следующее:
# >>> os.path.abspath("Users\\sergei.chuev\\Desktop\\Обучение\\Python_SkillBox\\Python_Basic-1\\Module22\\05_save")
#'C:\\windows\\system32\\Users\\sergei.chuev\\Desktop\\Обучение\\Python_SkillBox\\Python_Basic-1\\Module22\\05_save'

# а если я делаю следующим образом, то путь получается верный:
# >>> os.path.abspath(os.path.join("..", "..", "Users\\sergei.chuev\\Desktop\\Обучение\\Python_SkillBox\\Python_Basic-1\\Module22\\05_save"))
# 'C:\\Users\\sergei.chuev\\Desktop\\Обучение\\Python_SkillBox\\Python_Basic-1\\Module22\\05_save'

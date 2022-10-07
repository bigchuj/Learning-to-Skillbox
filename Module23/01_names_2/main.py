# TODO здесь писать код

with open("people.txt", "r", encoding="utf-8") as peoples_line:

    line_num = 0
    count_symb = 0

    for word in peoples_line:

        line_num += 1
        lenght = len(word)

        if word.endswith("\n"):
            lenght -= 1

        count_symb += lenght

        try:
            if lenght < 3:
                raise BaseException
        except BaseException:

            option = input(
                "Желаете сохранить ошибки в отдельном файле? ").lower()
            if option == "да":
                with open("errors.log", "w", encoding="utf-8") as loggs:
                    loggs.write(
                        "Ошибка: менее трёх символов в строке {}\n".format(
                            line_num)
                    )

            print("Ошибка: менее трёх символов в строке", line_num)

    print("Общее количество символов:", count_symb)

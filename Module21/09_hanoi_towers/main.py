# TODO здесь писать код


def move(hight, begin_point, final_point):

    if hight == 1:
        print(
            f"Переложить диск {hight} со стержня номер {begin_point} на стержень номер {final_point}"
        )

    else:
        middle_point = 6 - begin_point - final_point  # промежуточный колышек
        move(hight - 1, begin_point, middle_point)
        print(
            f"Переложить диск {hight} со стержня номер {begin_point} на стержень номер {final_point}"
        )
        move(hight - 1, middle_point, final_point)


quantity_discs = int(input("Введите количество дисков: "))
move(quantity_discs, 1, 3)

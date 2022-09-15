# TODO здесь писать код

def fibonachi(position, count=1):

    return fibonachi(position - 1) + fibonachi(position - 2) if position > 2\
        else 1


num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
num_fibonachi = fibonachi(num_pos)
print("Число:", num_fibonachi)

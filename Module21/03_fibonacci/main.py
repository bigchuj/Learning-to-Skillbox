# TODO здесь писать код

def fibonachi(num_pos, num_fib_before=0, num_fib=1):

    if num_pos == 1:
        return num_fib

    else:
        num_pos -= 1
        return fibonachi(
            num_pos, num_fib, num_fib + num_fib_before
        )


num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
num_fibonachi = fibonachi(num_pos)
print("Число:", num_fibonachi)

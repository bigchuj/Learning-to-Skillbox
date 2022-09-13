# TODO здесь писать код

def out_all_num(num, temp_num=0):

    temp_num += 1
    print(temp_num)

    if temp_num != num:
        out_all_num(num, temp_num)


num = int(input("Введите num: "))
out_all_num(num)

# TODO здесь писать код

def min_divider(num):

    for i in range(2, num + 1):

        if not num % i:
            print("Наименьший делитель, отличный от единицы:", i)
            break



num = int(input("Введите число: "))
min_divider(num)

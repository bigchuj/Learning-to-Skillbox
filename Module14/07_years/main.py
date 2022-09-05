# TODO здесь писать код


def special_years(year_start, year_end):

    print("\nГоды от 1900 до 2100 с тремя одинаковыми цифрами:")
    for i in range(year_start, year_end + 1):

        for j in range(10):

            print(i) if str(i).count(str(j)) == 3 else None


    # посчитал что так будет проще через строковый метод
    # если для вывода функции потребуется вывод int, то
    # можно выполнить обратное преобразование


year_first = int(input("Введите первый год: "))
year_second = int(input("Введите второй год: "))
special_years(year_first, year_second)

# TODO здесь писать код


def shift_line(line):  # -> line, shift_number

    letters = list(line)
    letters[:0] += [letters.pop()]

    return ''.join(letters)


line_1 = input("Первая строка: ")
line_2 = input("Вторая строка: ")

for shift in range(len(line_1)):

    line_1 = shift_line(line_1)
    if line_2 == line_1:
        print(f"Первая строка получается из второй со сдвигом {shift + 1}.")
        break

else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

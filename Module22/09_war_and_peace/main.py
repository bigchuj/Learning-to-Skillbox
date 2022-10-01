# TODO здесь писать код

import zipfile
import os


def reverse():

    return input(
        "Сортировать по возрастанию (В) или по убыванию (У)? ").lower() == "у"


def analisis(letters_count):

    result_finish = []
    summ_letter = sum(letters_count.values())

    # формируем словарь результат-буквы
    results = dict()

    for letter in letters_count:
        result = round(letters_count[letter] / summ_letter, 6)

        if result in results:
            results[result].append(letter)
        else:
            results[result] = [letter]

    # сортируем буквы и формируем итоговый результат
    result_list = list(results.keys())
    # запрос по возрастанию или по убыванию
    result_list.sort(reverse=reverse())

    for result in result_list:
        results[result].sort()

        for let in results[result]:
            result_finish.append(let + " " + str(result))

    return result_finish


def count_letters(text):

    # подсчитываем каждую букву в предложении
    # сумма всех букв - это сумма значений ключей

    letters_count = dict()

    for letter in text:

        n_let = ord(letter)

        if (65 <= n_let <= 90 or
            97 <= n_let <= 122 or
            1040 <= n_let <= 1071 or
            1072 <= n_let <= 1103 or
            n_let == 1105
            ):

            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1

    return letters_count


file_1 = zipfile.ZipFile("voyna-i-mir.zip")

line = file_1.open("voyna-i-mir.txt")

text = line.read().decode()
result_analisis = analisis(count_letters(text))
line.close()

action_with_file = input(
    'Нажмите "Ф" чтобы записать статистику в файл и \
"Э" чтобы вывести статистику на экран: '
).lower()

if action_with_file == "ф":
    file_2 = open("analisis.txt", "w", encoding="utf-8")
    [file_2.write(result + "\n") for result in result_analisis]
    file_2.close()

else:
    [print(result) for result in result_analisis]

# сейчас записан файл с возрастающей сортировкой,
# можно его переписать с убывающей

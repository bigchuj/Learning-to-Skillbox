# TODO здесь писать код


def analisis(letters_count):

    result_finish = []
    summ_letter = sum(letters_count.values())

    # формируем словарь результат-буквы
    results = dict()

    for letter in letters_count:
        result = round(letters_count[letter] / summ_letter, 3)

        if result in results:
            results[result].append(letter)
        else:
            results[result] = [letter]

    # сортируем буквы и формируем итоговый результат
    result_list = list(results.keys())
    result_list.sort(reverse=True)

    for result in result_list:
        results[result].sort()

        for let in results[result]:
            result_finish.append(let + " " + str(result))

    return result_finish


def count_letters(text):

    # подсчитываем каждую букву в предложении
    # сумма всех букв - это сумма значений ключей

    letters_count = dict()

    for letter in text.lower():

        if 97 <= ord(letter) <= 122:

            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1

    return letters_count


# open origin file
line_1 = open("text.txt", "r")
text = line_1.read()
print("Содержимое файла text.txt:", text, sep="\n")
result_analisis = analisis(count_letters(text))
line_1.close()

# write result analisis
line_2 = open("analysis.txt", "w")
[line_2.write(result + "\n") for result in result_analisis]
line_2.close()

# print analis
line_3 = open("analysis.txt", "r")
print("\nСодержимое файла analysis.txt:", line_3.read(), sep="\n")
line_3.close()

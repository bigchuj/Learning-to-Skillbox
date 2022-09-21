# TODO здесь писать код

import os


letters = "abcdefghijklmnopqrstuvwxyz"


def quantity_lines(txt):

    lines = txt.split("\n")
    count_lines = len(lines)

    return count_lines


def rare_letter(txt):

    rare_letter = ""
    quantity_rare_letter = len(txt)

    for letter in letters:

        if 0 < txt.count(letter) < quantity_rare_letter:
            rare_letter = letter

    return rare_letter


def quantity_letters_and_words(txt):

    count_letters = 0
    count_words = 0
    lines = txt.split("\n")
    words = [word for line in lines for word in line.split(" ")]

    for word_i in words:

        for letter in word_i:

            if letter in letters:
                count_letters += 1

        for letter in letters:

            if letter in word_i:
                count_words += 1
                break

    return count_letters, count_words


way_file = os.path.abspath(os.path.join(
    "Module22", "02_zen_of_python", "zen.txt"))

text = open(way_file, "r")
txt = text.read().lower()
c_letter, c_word = quantity_letters_and_words(txt)
c_line = quantity_lines(txt)
rare_letter = rare_letter(txt)
text.close()

print("Количество букв в файле:", c_letter)
print("Количество слов в файле:", c_word)
print("Количество строк в файле:", c_line)
print("Наиболее редкая буква:", rare_letter)

# TODO здесь писать код

word_letters = list(input("Введите текст: "))
vowel_letters = "уеёэоаыяию"
result_vowel_letters = [
    letter for letter in word_letters if letter.lower() in vowel_letters
]

print("Список гласных букв:", result_vowel_letters)
print("Длина списка:", len(result_vowel_letters))

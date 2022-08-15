# TODO здесь писать код

line = input("Введите строку: ").split()
max_word = ''
len_max_word = 0

for i in line:
    temp_len = len(i)

    if temp_len > len_max_word:
        max_word = i
        len_max_word = temp_len

print("Самое длинное слово:", max_word)
print("Длина этого слова:", len_max_word)

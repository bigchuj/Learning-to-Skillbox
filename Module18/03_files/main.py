# TODO здесь писать код

name_file = input("Название файла: ")
symbols = '@№$%^&\*()'
expansions = ['.txt', '.docx']

for symb in symbols:

    if name_file.startswith(symb):
        print("\nОшибка: название начинается на один из специальных символов.")
        break

else:

    for exp in expansions:

        if name_file.endswith(exp):
            print("\nФайл назван верно.")
            break

    else:
        print("\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.")

# TODO здесь писать код

def line_to_list(line):
    # текст в список

    return list(line)


def new_symb_(new_symb, min_symb_ord, max_symb_ord):
    # формируем новый символ

    if new_symb > max_symb_ord:
        new_symb = min_symb_ord - 1 + (new_symb - max_symb_ord)
        return chr(new_symb)

    elif new_symb < min_symb_ord:
        new_symb = max_symb_ord + 1 - (min_symb_ord - new_symb)
        return chr(new_symb)

    else:
        return chr(new_symb)


def code_text(all_symbols, shift):
    # кодирование текста
    # на вход подается список всех символов в строке и смещение

    new_symbols = []

    for symb in all_symbols:

        if symb.isupper():

            if 1040 <= ord(symb) <= 1071:  # RU
                new_symbols.append(new_symb_(ord(symb) + shift, 1040, 1071))

            elif 65 <= ord(symb) <= 90:  # EN
                new_symbols.append(new_symb_(ord(symb) + shift, 65, 90))

        elif symb.islower():

            if 1072 <= ord(symb) <= 1103:  # RU
                new_symbols.append(new_symb_(ord(symb) + shift, 1072, 1103))

            elif 97 <= ord(symb) <= 122:  # EN
                new_symbols.append(new_symb_(ord(symb) + shift, 97, 122))

        else:
            new_symbols.append(symb)
            # иные символы

    return ''.join(new_symbols)


original_file = open("text.txt", "r")
line_lst_orig = original_file.read().split("\n")
line_lst_encoded = []

for i, text in enumerate(line_lst_orig):
    line_lst_encoded.append(code_text(line_to_list(text), i + 1))

print("Содержимое файла text.txt:", *line_lst_orig, sep="\n")
original_file.close()


encoded_file = open("cipher_text.txt", "a")

for text in line_lst_encoded:
    encoded_file.write(text + "\n")

encoded_file.close()


encoded_file_out = open("cipher_text.txt", "r")
line = encoded_file_out.read()
print("\nСодержимое файла cipher_text.txt:", line, sep="\n")
encoded_file_out.close()

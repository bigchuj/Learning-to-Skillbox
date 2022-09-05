# TODO здесь писать код
# я уже писал код по шифру https://stepik.org/lesson/352860/step/10?unit=336821
# только он у меня вышел очень громоздким, если доступа нет, то могу выслать текст кода отдельно
# текущий код я оптимизировал, выглядит лучше без потери функционала
# его так же можно оптимизировать, перечитывая приходят разные идеи


def line_to_list(line):

    all_symbols = [sym for sym in line]

    return all_symbols


def new_symb_(new_symb, min_symb_ord, max_symb_ord):  # формируем новый символ

    if new_symb > max_symb_ord:
        new_symb = min_symb_ord - 1 + (new_symb - max_symb_ord)
        return chr(new_symb)

    elif new_symb < min_symb_ord:
        new_symb = max_symb_ord + 1 - (min_symb_ord - new_symb)
        return chr(new_symb)

    else:
        return chr(new_symb)


def code_text(all_symbols, shift):  # на вход подается список всех символов в строке и смещение

    new_symbols = []

    for symb in all_symbols:

        if symb.isupper() and 1040 <= ord(symb) <= 1071:

            new_symbols.append(new_symb_(ord(symb) + shift, 1040, 1071))

        elif symb.islower() and (1072 <= ord(symb) <= 1103):

            new_symbols.append(new_symb_(ord(symb) + shift, 1072, 1103))

        else:
            new_symbols.append(symb)
            # если символы не в русском алфавите
            # а вообще можно реализовать через доп функцию переключение на другой язык
            # или вообще с автоматическим определением языка

    return ''.join(new_symbols)


line_text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

print("Зашифрованное сообщение:", code_text(line_to_list(line_text), shift))

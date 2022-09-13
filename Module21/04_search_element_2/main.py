# TODO здесь писать код

def value_search(dict_, key_search, depth=None):

    if not depth:
        value_s = dict_.get(key_search)

        if value_s:
            return value_s

        else:
            for key in dict_.keys():

                if isinstance(dict_[key], dict):
                    value_s = value_search(dict_[key], key_search)

                if value_s:
                    return value_s

    else:
        if depth == 1:
            return dict_.get(key_search)

        else:
            for key in dict_.keys():

                if isinstance(dict_[key], dict):
                    value_s = value_search(
                        dict_[key], key_search, depth - 1
                    )
                else:
                    return None

                if value_s:
                    return value_s


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input("Введите искомый ключ: ")
depth = input("Хотите ввести максимальную глубину? Y/N: ").lower()

max_depth = None if depth == "n"\
    else int(input("Введите максимальную глубину: "))

value = value_search(site, key, max_depth)
print("Значение ключа:", value)

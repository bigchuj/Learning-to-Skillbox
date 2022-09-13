nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код


def conversion_list(list_):

    conv_list = list()

    for elem in list_:

        if isinstance(elem, list):
            conv_list.extend(conversion_list(elem))
        else:
            conv_list.append(elem)

    return conv_list


print("Ответ:", conversion_list(nice_list))

# TODO здесь писать код

def tpl_sort(*args):

    for num in args:
        if type(num) == float:
            return args

    else:
        return tuple(sorted(args))

    # на сколько код ниже может быть целесообразнее и лучше чем тот 
    # что представлен выше? Оба случая выполняют требуемый функционал

    # return args if False in [type(num) != float for num in args]\
    #     else tuple(sorted(args))


# print(tpl_sort(6, 3, -1, 8, 4, 10, -5))

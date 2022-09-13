# TODO здесь писать код


def elems(obj):

    return tuple(elem for elem in obj)


def my_zip(*args):

    elements = tuple(elems(obj) for obj in args)
    len_iter = min(
        tuple(len(elem) for elem in elements)
    )

    results = list(
        tuple(obj[i] for obj in elements) for i in range(len_iter)
    )

    return results


# a = [{"x": 4}, "b", "z", "d"]

# b = (10, {20, }, [30], "z")

# print(my_zip(a, b))

# a = [1, 2, 3, 4, 5]

# b = {1: "s", 2: "q", 3: 4}

# x = (1, 2, 3, 4, 5)

# print(my_zip(a, b, x))

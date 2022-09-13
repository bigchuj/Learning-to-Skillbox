# TODO здесь писать код

def sum(*args):
    total = 0

    for elem in args:

        if isinstance(elem, list):
            total += sum(*elem)
            
        else:
            total += elem

    return total


# print(sum([[1, 2, [3]], [1], 3]))
# print(sum(1, 2, 3, 4, 5))

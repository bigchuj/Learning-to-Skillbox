# TODO здесь писать код


def is_prime(index):

    if index in (0, 1):
        return False

    count = 0
    for i in range(2, index + 1):

        count += 1 if not index % i else 0
        if count == 2:
            return False

    return True


def crypto(args):

    return [args[i] for i in range(len(args)) if is_prime(i)]

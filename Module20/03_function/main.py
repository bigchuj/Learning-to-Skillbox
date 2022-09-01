# TODO здесь писать код

from ast import arg


def slicer(args, elem):

    if elem in args:

        args = args[args.index(elem):]

        if args.count(elem) > 1:
            args = (args[0],) + args[1:args[1:].index(elem) + 2]

        return args

    else:
        return tuple()

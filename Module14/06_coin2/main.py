# TODO здесь писать код


def search_coin(
    first_coordinate, second_coordinate, radius
):

    if (
        pow(first_coordinate, 2) + pow(second_coordinate, 2) <= pow(radius, 2)
    ):
        print('\nМонетка где-то рядом')

    else:
        print('\nМонетки в области нет')


print("Введите координаты монетки:")
first_coordinate = float(input('X: '))
second_coordinate = float(input('Y: '))
radius = float(input('Введите радиус: '))

search_coin(first_coordinate, second_coordinate, radius)

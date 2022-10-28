# TODO здесь писать код

from math import pi, sqrt


class Circle:

    def __init__(
        self,
        coordinate_x=0,
        coordinate_y=0,
        radius=1
    ) -> None:

        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius


    def square(self):

        square_ = pi * pow(self.radius, 2)
        return round(square_, 4)


    def perimeter(self):

        perimeter_ = 2 * pi * self.radius
        return round(perimeter_, 4)


    def expantion(self, coef):

        radius_new = self.radius * coef
        square_new = Circle(radius=radius_new).square()
        perimeter_new = Circle(radius=radius_new).perimeter()

        return "Новый радиус = {}, новая площадь = {}, новый периметр = {}".format(
            radius_new, square_new, perimeter_new
        )


    def intersection(
        self,
        coordinate_second_circle_x,
        coordinate_second_circle_y,
        radius_second_circle
    ):

        distance = sqrt(
            sum(
                (
                    pow(self.coordinate_x - coordinate_second_circle_x, 2),
                    pow(self.coordinate_y - coordinate_second_circle_y, 2)
                )
            )
        )

        if distance > sum((self.radius, radius_second_circle)):
            return "Окружности не пересекаются"

        elif distance < abs(self.radius - radius_second_circle):

            if self.radius > radius_second_circle:
                return "Вторая окружность лежит внутри первой"

            elif self.radius < radius_second_circle:
                return "Первая окружность лежит внутри второй"
        
        elif distance == abs(self.radius - radius_second_circle) == 0:
            return "Окружности равны"

        elif distance == sum((self.radius, radius_second_circle)):
            return "Окружности соприкасаются"

        else:
            return "Окружности пересекаются"


crl = Circle(5, 5, 5)
print(crl.square())  # площадь
print(crl.perimeter())  # периметр
print(crl.expantion(3))  # изменение всех параметров согласно коэффициента
print(crl.intersection(-5, 5, 4))  # Окружности не пересекаются
print(crl.intersection(4, 4, 1))  # Вторая окружность лежит внутри первой
print(crl.intersection(10, 10, 15))  # Первая окружность лежит внутри второй
print(crl.intersection(5, 5, 5))  # Окружности равны
print(crl.intersection(-5, 5, 5))  # Окружности соприкасаются
print(crl.intersection(10, 10, 10))  # Окружности пересекаются

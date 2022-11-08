# TODO здесь писать код

class Answer:
    storm = "Шторм"
    vapeor = "Пар"
    dirt = "Грязь"
    lightning = "Молния"
    dust = "Пыль"
    lava = "Лава"
    wave= "Волны"
    hurricane= "Ураган"
    fire = "Пожар"
    drought = "Засуха"


class Water:
    air = Answer().storm
    fire = Answer().vapeor
    land = Answer().dirt
    wind = Answer().wave
    
    def __add__(self, other):
        try:
            return other.water
        except AttributeError:
            return None


class Air:
    water = Answer().storm
    land = Answer().dust
    fire = Answer().lightning
    wind = Answer().hurricane

    def __add__(self, other):
        try:
            return other.air
        except AttributeError:
            return None


class Fire:
    water = Answer().vapeor
    air = Answer().lightning
    land = Answer().lava
    wind = Answer().fire
    
    def __add__(self, other):
        try:
             return other.fire
        except AttributeError:
            return None


class Land:
    water = Answer().dirt
    air = Answer().dust
    fire = Answer().lava
    wind = Answer().drought

    def __add__(self, other):
        try:
            return other.land
        except AttributeError:
            return None


class Wind:
    water = Answer().wave
    air = Answer().hurricane
    fire = Answer().fire
    land = Answer().drought

    def __add__(self, other):
        try:
            return other.wind
        except AttributeError:
            return None


water = Water()
air = Air()
fire = Fire()
land = Land()
wind = Wind()
print(water + air)
print(water + fire)
print(water + land)
print(air + fire)
print(air + land)
print(fire + land)
print(fire + fire)  # -> None
print(wind + water)
print(wind + air)
print(wind + fire)
print(wind + land)
print(wind + wind)  # -> None

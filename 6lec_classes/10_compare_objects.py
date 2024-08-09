class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon if isinstance(otro, Coordenadas) else False

    # It's not necessary to override this method,
    # since python is smart enough to infer this method from method __eq__
    # def __ne__(self, otro):
        # return self.lat != otro.lat or self.lon != otro.lon if isinstance(otro, Coordenadas) else True

    # Likewise, It is also not necessary to override __gt__ and __ge__ method,
    # since It is able to infer it from __lt__ and _e__ method respectively
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon if isinstance(otro, Coordenadas) else False

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon if isinstance(otro, Coordenadas) else False


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
coords3 = Coordenadas(44, 27)

person1 = Person("sue", 15)
print(coords, coords2)

# __eq__
print(coords == coords2)  # True
print(coords2 == person1)  # False

# __ne__
print(coords != coords2)  # False
print(coords != coords3)  # True
print(coords2 != person1)  # True

# __lt__
print(coords2 < coords)  # False
print(coords3 < coords)  # True
print(coords < person1)  # False

# __gt__
print(coords2 > coords)  # False
print(coords > coords3)  # True

# __le__
print(coords <= coords2)  # True
print(coords3 <= coords)  # True
print(coords <= person1)  # False

# __ge__
print(coords >= coords2)  # True
print(coords >= coords3)  # True

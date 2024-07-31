class Perro:
    def __init__(self, nombre, edad):
        # __nombre is a private property
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    # this is a private method
    def __private_method(self):
        print("soy un metodo privado")

    def habla(self):
        self.__private_method()
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 5)


perro1 = Perro.factory()
perro1.habla()  # Chanchito dive: Guau!

# You can not access to private property directly
# print(perro1.__nombre)  # It throws an Error
# However, You can accces it trought public methods like this
print(perro1.get_nombre())  # Chanchito

# Also, you can modify the private property value thought a public method
perro1.set_nombre("Feliz")
print(perro1.get_nombre())  # Feliz

# _dict_ : It contains all properties that instance has
print(perro1.__dict__)  # {'_Perro__nombre': 'Feliz', 'edad': 5}

# Thus you could access to private property, although it's a bad practice.
print(perro1._Perro__nombre)  # Feliz

# Thus you could access to private method, although it's a bad practice.
perro1._Perro__private_method()

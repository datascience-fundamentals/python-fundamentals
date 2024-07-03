class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    # You can use @property to decorate a getter method and simulate
    # that It is being a class property, but behind scenes
    # it is executing a method
    @property
    def nombre(self):
        print("pasando por getter")
        return self.__nombre

    # You can also decorate the setter methods by @<getter-method-name>.setter
    # in order to invoke it when you want to set a value to name property
    @nombre.setter
    def nombre(self, nombre):
        print("pasando por setter")
        self.__nombre = nombre if isinstance(
            nombre, str) and nombre.strip() else "Chanchito"


perro = Perro(True)
perro2 = Perro("Choclo")
print(perro.nombre)  # Chanchito
print(perro2.nombre)  # Choclo

perro2.nombre = "Feliz"
print(perro2.nombre)  # Feliz

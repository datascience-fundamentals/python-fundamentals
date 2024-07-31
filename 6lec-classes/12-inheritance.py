class Animal:
    patas = 2

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def __str__(self):
        return f"Nombre: {self.nombre} Patas: {self.patas}"


# Inheriting instance members (methods, properties) from Animal
# Inheriting class members (Ejem: property patas)
class Perro(Animal):

    # super().__init__ calls parent constructor
    def __init__(self, nombre):
        super().__init__(nombre)

    def pasear(self):
        print(f"{self.nombre} esta paseando")

# Inheriting instance members (methods, properties) from Perro who also inherits
# from Animal. It means there is a multi level inheritance.
# It's recommmend not to inherit more than two levels.


class Serpiente(Perro):
    patas = 0

    def programar(self):
        print(f"{self.nombre} esta programando")


perro = Perro("Dogy")
print(perro)
perro.comer()
perro.pasear()
print(Perro.patas)  # 2

serpiente = Serpiente("Feliz")
print(serpiente)
serpiente.comer()
serpiente.pasear()
serpiente.programar()
print(Serpiente.patas)  # 0

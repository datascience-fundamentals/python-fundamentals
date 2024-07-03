# self: It references to the instance class
# __init__ : It is the constructor of the class
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)
mi_perro.habla()  # Chanchito dice: Guau!
print(mi_perro.edad)  # 1

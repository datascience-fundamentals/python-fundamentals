class Perro:
    # This property is a class member
    patas = 4

    def __init__(self, nombre, edad):
        # Those properties are instance members
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)
mi_perro2 = Perro("Felipe", 1)

# to access the value of the class property
print(Perro.patas)  # 4
# you can also access the value of class property by the object
print(mi_perro.patas)  # 4

# to change the value of the class property
Perro.patas = 3
# you could access to the changed value
# from the class declaration (Perro.patas)  the object (mi_perro.patas)
print(Perro.patas)  # 3
print(mi_perro.patas)  # 3

# you can also change the value by the object, but
# You only will see the new value in this object
mi_perro.patas = 2
print(Perro.patas)  # 3
print(mi_perro.patas)  # 2
print(mi_perro2.patas)  # 3

# to acccess the value of the instance property
print(mi_perro.nombre)  # Chanchito
print(mi_perro2.nombre)  # Felipe

# to change the value of the instance property
mi_perro.nombre = "Rufus"
print(mi_perro.nombre)  # Rufus
print(mi_perro2.nombre)  # Felipe

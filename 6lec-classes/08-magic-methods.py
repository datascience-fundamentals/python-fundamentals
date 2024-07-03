# method magics -> these are executed behind scences.
# In a nutshell, you don't call them directly.
# For example: the constructor __init__ is a magic method
# So, the magic methods start with __ and end with __
# By default there are magic methods inherited which you can use, for example:
# __str__ : provide string representations

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        print("se llama str")
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Chanchito", 7)
print(perro)  # Clase Perro: Chacnhito

texto = str(perro)
print(texto)  # Clase Perro: Chanchito

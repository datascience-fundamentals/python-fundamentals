# desctructor -> It is a method which is execute when you delete an object

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Chanchito", 7)
del perro  # Chao perro :( Chanchito

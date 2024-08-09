class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # This method is an instance member where self references to the instance (perro1) for example
    def instance_method(self):
        print("Soy un metodo de instancia")

    # This methos is a class member where cls references to the class (Perro)
    @classmethod
    def class_method(cls):
        print("Soy un metodo de clase")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro("Chanchito", 2)

# to invoke a instance method
perro1.instance_method()  # Soy un metodo de instancia

# to invoke a class method
Perro.class_method()  # Soy un metodo de clase
# you can also invoke a class method by the object
perro1.class_method()  # Soy un metodo de clase

# Example of factory design pattern using class methods
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)  # 4 Chanchito Feliz

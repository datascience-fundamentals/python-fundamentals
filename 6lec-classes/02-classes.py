class Perro:
    def habla(self):
        print("Guau!")


mi_perro = Perro()
mi_perro.habla()  # Guau!

# to identify the object class (data type)
print(type(mi_perro))  # <class '_main_.Perro'>

# to valid if the object is an instance of the class
print(isinstance(mi_perro, Perro))  # True
print(isinstance(mi_perro, str))  # False

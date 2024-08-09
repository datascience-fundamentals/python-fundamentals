# apellido recieves a default value if you dont send this argument's value
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Nicolas", "Schurman")
hola("Chanchito")

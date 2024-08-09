def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


# using named arguments where you must especify the name of argument
# whose value you need to pass
hola(apellido="Schurman", nombre="Wolfgang")

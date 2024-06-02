nombre = "Nicolas"
apellido = "Schurmann"

# concat strings
nombre_completo = nombre + " " + apellido  # Nicolas Schurmann
nombre_completo2 = f"{nombre} {apellido}"  # Nicolas Schurmann

# thanks to f"", you can implement logic within {}
nombre_completo3 = f"{nombre[0]} {2 + 5}"  # N 7

print(nombre_completo)
print(nombre_completo2)
print(nombre_completo3)

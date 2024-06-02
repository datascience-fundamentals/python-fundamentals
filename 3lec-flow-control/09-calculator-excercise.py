msg = """
Bievenidos a la calculadora
Para salir escribe "salir"
Las operaciones son suma, multi, div y resta
"""
print(msg)

n1 = None
while True:
    if n1 is None:
        n1 = int(input("Ingresa un número: "))

    ope = input("Ingresa una operación: ").strip().lower()
    if ope == "salir":
        break

    n2 = int(input("Ingresa siguiente número: "))

    if ope == "suma":
        n1 += n2
    elif ope == "multi":
        n1 *= n2
    elif ope == "div":
        n1 /= n2
    elif ope == "resta":
        n1 -= n2

    print(f"El resultado es: {n1}")


print("Fin del programa")

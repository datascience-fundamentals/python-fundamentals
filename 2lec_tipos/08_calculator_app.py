# input() -> read a value from the console
readNum1 = input("Ingresa primer numero: ")
readNum2 = input("Ingresa segundo numero: ")

# int() -> parse string to int
n1 = int(readNum1)
n2 = int(readNum2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es: {suma}
el resultado de la resta es: {resta}
el resultado de la multiplicacion es: {multi}
el resultado de la division es: {div}
"""

print(mensaje)

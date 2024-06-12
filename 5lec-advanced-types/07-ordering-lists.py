numeros = [2, 4, 1, 45, 75, 22]

# sort() -> It modifies the order of list's elements
# to order numbers ascending
numeros.sort()
print(numeros)

# to order numbers descending
numeros.sort(reverse=True)
print(numeros)

edades = [2, 4, 1, 45, 75, 22]

# sorted() -> It returns a new list with the elements ordererd.

# to order ages ascending
edadesOrdered = sorted(edades)
print(edades)
print(edadesOrdered)

# to order ages descending
edadesOrdered = sorted(edades, reverse=True)
print(edades)
print(edadesOrdered)

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)

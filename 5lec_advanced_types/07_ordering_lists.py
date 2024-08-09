
def ordena(elemento):
    return elemento[1]


numeros = [2, 4, 1, 45, 75, 22]
edades = [2, 4, 1, 45, 75, 22]
usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# sort() -> It modifies the order of list's elements
# to order numbers ascending
numeros.sort()
print(numeros)

# to order numbers descending
numeros.sort(reverse=True)
print(numeros)

# using a method to custom the ordering
usuarios.sort(key=ordena, reverse=True)
print(usuarios)  # [['Pulga', 5], ['Chanchito', 4], ['Felipe', 1]]

# using lambda to custom the ordering
usuarios.sort(key=lambda item: item[1])
print(usuarios)  # [['Felipe', 1], ['Chanchito', 4], ['Pulga', 5]]


# sorted() -> It returns a new list with the elements ordererd.

# to order ages ascending
edadesOrdered = sorted(edades)
print(edades)
print(edadesOrdered)

# to order ages descending
edadesOrdered = sorted(edades, reverse=True)
print(edades)
print(edadesOrdered)

# using a method to custom the ordering
usuariosOrdered = sorted(usuarios, key=ordena, reverse=True)
print(usuariosOrdered)  # [['Pulga', 5], ['Chanchito', 4], ['Felipe', 1]]

# using lambda to custom the ordering
usuariosOrdered = sorted(usuarios, key=lambda item: item[1])
print(usuariosOrdered)  # [['Felipe', 1], ['Chanchito', 4], ['Pulga', 5]]

# You can not modify, delete and add new elements in a Tuple.
# However You can create another tuple based on an existing tuple or list

# if you join both tuples, It returs another tuple
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)  # (1, 2, 3, 4, 5, 6)

# creating a tuple based on a list
punto = [1, 2]
puntoTuple = tuple(punto)
print(puntoTuple)  # (1, 2)

# It returns another tuple
menosNumeros = numeros[:3]
print(menosNumeros)  # (1, 2, 3)

# you can also unpack the tuple.
# *otros is a list, but not a tuple
primero, segundo, *otros = numeros
print(primero, segundo, otros)  # 1 2 [3, 4, 5, 6]

for n in numeros:
    print(n)

# numeros[0] = 4 -> You can not modify an tuple element
# But you can convert it to list and then modifying it
listaNumeros = list(numeros)

listaNumeros[0] = 30
print(listaNumeros)

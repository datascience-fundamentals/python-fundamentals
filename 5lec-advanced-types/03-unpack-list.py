numeros = [1, 2, 3]

# It's a bad practice
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# unpacking the elements of a list
primero, segundo, tercero = numeros
print(primero, segundo, tercero)  # 1, 2, 3

# unpacking the elements of a list using a xargs
primero, *otros = numeros
print(primero, otros)  # 1, [2, 3]

numeros = list(range(1, 10))
primero, segundo, *otros = numeros
print(primero, segundo, otros)  # 1, 2, [3,4,5,6,7,8,9]

primero, *otros, ultimo = numeros
print(primero, ultimo)  # 1, 9

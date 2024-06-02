# for -> It allow you to iterate a range o elements a range o elements
buscar = 10

for numero in range(5):  # range(5) -> 0 to 4
    print(numero, numero * "hola mundo")

for numero in range(2, 5):  # range(2, 5) -> 2 to 4
    print(numero, numero * "hola mundo")

for numero in range(1, 10, 2):  # range(1, 10, 2) -> 1 to 9 with an increase of 2 in 2
    print(numero, numero * "hola mundo")

# for - else
for numero in range(1, 6):  # range(1,6) -> 1 to 5
    if buscar == numero:
        print("numero encontrado:", buscar)
        break  # It allow to end the loop
    else:
        print(numero)
else:  # this part of code will be executed only if 'break' is not called on the loop
    print("numero buscado no encontrado :(")

# iterating a string
for char in "Ultimate python":
    print(char)

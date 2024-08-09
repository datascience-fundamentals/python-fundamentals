numero = 1
# while
while numero < 100:
    print(numero)
    numero *= 2
numero = 1
# while - else
while numero < 100:
    print(numero)
    if numero == 128:
        break  # it allows you to end the loop
    numero *= 2
else:  # This part of code will be executed only if 'break' is not called in the while
    print("128 no encontrado")

comando = ""
while comando.lower() != "exit":
    comando = input("$ ")
    print(comando)
print("fin del programa")

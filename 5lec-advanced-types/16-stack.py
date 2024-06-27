# STACK is LIFO (Last In First Out)

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# To delete the last element from the stack
ultimoElemento = pila.pop()
print(ultimoElemento)  # 3
print(pila)  # [1,2]

# getting the last element from the stack
print(pila[-1])  # 2

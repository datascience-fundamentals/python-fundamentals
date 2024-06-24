lista = [1, 2, 3, 4]
print(*lista)  # 1 2 3 4

tupla = (1, 2, 3, 4)
print(*tupla)  # 1 2 3 4


def suma3(n1, n2, n3):
    return n1 + n2 + n3


sumandos = [1, 2, 3]
suma = suma3(*sumandos)
print(suma)  # 6

# you can add elements from list to another one by unpackage operator
lista1 = [1, 2, 3, 4]
lista2 = [5, 6]
combinada = ["Hola", *lista1, "mundo", *lista2]  # ['Hola',1,2,3,4,'mundo,5,6]
print(combinada)

# you cand add elements from map to another one by unpackage operator
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}
print(nuevoPunto)  # {'x': 19, 'y': 15, 'z': 'mundo'}

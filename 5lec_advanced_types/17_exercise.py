from pprint import pprint

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


sin_espacios = quita_espacios(string)
print(sin_espacios)

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


contados = cuenta_caracteres(sin_espacios)
pprint(contados, width=1)
# 3. Ordenar las llaves de un diccionario por el valor que tiene y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


ordenados = ordena(contados)
print(ordenados)
# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4), ("d", 4)] => [("c", 4), ("d", 4)]


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


mayores = mayores_tuplas(ordenados)
print(mayores)

# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con n repeticiones son:
# -C
# -D


def crea_mensaje(dict):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in dict.items():
        mensaje += f"- {key.upper()} con {valor} repeticiones \n"
    return mensaje


mensaje = crea_mensaje(mayores)
print(mensaje)

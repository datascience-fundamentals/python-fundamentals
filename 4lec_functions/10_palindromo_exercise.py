def voltear_cadena(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto_sin_espacio = texto.replace(" ", "")
    texto_al_reves = voltear_cadena(texto_sin_espacio)
    return texto_al_reves.lower() == texto_sin_espacio.lower()


def es_palindromov2(texto):
    texto_sin_espacio = texto.replace(" ", "")
    # reversed() -> it returns an iterator where each element of the array
    # is the character of the string reversed
    texto_al_reves = ''.join(reversed(texto_sin_espacio))
    return texto_al_reves.lower() == texto_sin_espacio.lower()


print("hola mundo", es_palindromo("hola mundo"))  # False
print("ReconocEr", es_palindromo("ReconocEr"))  # True
print("Amo la paloma", es_palindromo("Amo la paloma"))  # True

print("hola mundo", es_palindromov2("hola mundo"))  # False
print("ReconocEr", es_palindromov2("ReconocEr"))  # True
print("Amo la paloma", es_palindromov2("Amo la paloma"))  # True

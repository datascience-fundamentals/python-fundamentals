punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto["z"])

# you can not ask for key which doesn't exist in the dictionary
# print(punto["lala"]) -> It throws an error

# you can ask if the key exists in the dictionary
print("z" in punto)  # True

# get() -> safe way to ask for value
print(punto.get("x"))  # 25
# get() -> It retuns None in case the key doesn't exist in the dictionary
# unless It have set up a default value
print(punto.get("lala"))  # None
print(punto.get("lala", 97))  # 97

# to delete a key with its value from the dictionary
del punto["x"]
print(punto)

punto["x"] = 25

# to iterate all values from the dictionary
for key in punto:
    print(key, punto[key])

for llave, valor in punto.items():
    print(f"{llave} - {valor}")

#
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]
usuarioConId3 = next(filter(lambda usuario: usuario["id"] == 3, usuarios))
print(f"{usuarioConId3["id"]} - {usuarioConId3["nombre"]}")  # 3 - Nicolas

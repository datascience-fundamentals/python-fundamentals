mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for mascota in mascotas:
    print(mascota)

# enumerate() -> it returns a tupla
for mascota in enumerate(mascotas):
    print(f"{mascota} -> {mascota[0]} - {mascota[1]}")

# you can unpack a tuple
for indice, nombre in enumerate(mascotas):
    print(indice, nombre)

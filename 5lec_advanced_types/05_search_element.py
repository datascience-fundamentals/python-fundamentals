mascotas = ["Pelusa", "Pulga", "Pulga", "Felipe", "Chanchito Feliz"]

# To know if the element is the element exist in the array
print("Pulga" in mascotas)  # True

# index() -> It returns the position of the searched element.
#            Otherwise, It will throw an error
if "Pulga" in mascotas:
    print(mascotas.index("Pulga"))  # 1

# count() -> counts how many times a value is repeated
print(mascotas.count("Pulga"))  # 2
print(len(mascotas))

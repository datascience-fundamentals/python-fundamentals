mascotas = ["Wolfgang", "Pelusa", "Pulga",
            "Pulga", "Felipe", "Chanchito feliz"]

# insert() -> to add an element in a specific position of the list
mascotas.insert(1, "Melvin")
print(mascotas)

# append() -> to add an element at the end of the list
mascotas.append("Chanchito triste")
print(mascotas)

# remove() -> It removes the first ocurrence of the element
mascotas.remove("Pulga")
print(mascotas)

# pop() -> It removes the last element of the list
# and returns the element removed
removed = mascotas.pop()
print(removed)  # Chanchito triste
print(mascotas)

# pop(ind) -> It removes an element of the list depending of the position
removed = mascotas.pop(1)
print(removed)  # Melvin
print(mascotas)

# another way to delete an element of the list.
del mascotas[0]
print(mascotas)

# You also can use this to delete elements in range in the same way
# you were able to select elements of a list.
# For example: removing elements from the beginning to end each two elements
del mascotas[::2]
print(mascotas)

# clear() -> Ifa allows you to remove all elements
mascotas.clear()
print(mascotas)

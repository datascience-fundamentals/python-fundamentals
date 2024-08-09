usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# [expression for item in items]
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filter
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

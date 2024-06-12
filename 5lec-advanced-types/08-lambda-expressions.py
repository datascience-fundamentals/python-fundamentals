usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# lambda parametors: valorRetorno
usuarios.sort(key=lambda elem: elem[1])
print(usuarios)

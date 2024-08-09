usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# filter
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)

# example using filter and map together
personas = [["Sue", 30], ["Ana", 20], ["Luis", 50]]

personasMayorIgual30 = filter(lambda persona: persona[1] >= 30, personas)
nombres = list(map(lambda persona: persona[0], personasMayorIgual30))
print(nombres)  # ['Sue', 'Luis']

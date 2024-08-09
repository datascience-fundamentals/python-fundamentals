mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]

# length of mascotas
print(len(mascotas))  # 4

print(mascotas[0])  # Wolfgang
mascotas[0] = "Bicho"

# get the first position of list
print(mascotas[0])  # Bicho

# get from the second position until third element of list
print(mascotas[1:3])  # ['Pelusa', 'Pulga']

# get from the first position until second element of list
print(mascotas[:2])  # ['Bicho','Pelusa']

# get from the third position until the last element of list
print(mascotas[2:])  # ['Pulga', 'Copito']

# get from the first position until the last element of list
print(mascotas[:])  # ['Bicho','Pelusa','Pulga','Copito']

nums = list(range(1, 8))

# Get elements from the initial position until last element of the list
# each 2 elements
print(nums[::2])  # [1,3,5,7]

# Get elements from the second position until last element of the list
# each 3 elements
print(nums[1::3])  # [2, 5]

# Get elements from the second position until fith element
# each two elements
print(nums[1:5:2])  # [2, 4]

numeros_21 = list(range(1, 21))
print(numeros_21[::2])  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(numeros_21[1::2])  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

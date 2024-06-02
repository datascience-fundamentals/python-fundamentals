animal = "chanCHito feliz"
animal2 = "  perrito feliz  "

# trasnform string to uppercase
print(animal.upper())  # CHANCHITO FELIZ

# trasnform string to lowercase
print(animal.lower())  # chanchito feliz

# transform the first letter to uppercase
# It always try to transform the first letter, whether It is a space o not.
print(animal.capitalize())  # Chanchito feliz

# transform the first letter of each word to uppercase
print(animal.title())  # Chanchito Feliz

# remove spaces on the sides
print(animal2.strip())  # perrito feliz
print(animal2.strip().capitalize())  # Perrito feliz

# remove spaces on the left side
print(animal2.lstrip())

# remove spaces on the right side
print(animal2.rstrip())

# return the nearest string position where It has found a match.
# Otherwise, It would return -1
print(animal.find("CH"))  # 4
print(animal.find("Ch"))  # -1

# replace some part of the string where It matches
print(animal.replace("nCH", "j"))  # chajito feliz

# Valid if the string contains the substring
print("nCH" in animal)  # True

# Valid if the string not contains the substring
print("nH" not in animal)  # True

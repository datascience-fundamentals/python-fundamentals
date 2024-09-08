import random
import string

lista = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
# It messes up the list randomly and assign the new value to the list
random.shuffle(lista)
print(
    random.random(),  # It returns a random decimal number between 0 and 1
    random.randint(1, 5),  # It returns a random int number between 1 and 5
    lista,
    random.choice(lista2),  # It takes a value from the list ramdonly
    # It takes a group of elements from the list ramdonly
    random.choices(lista2, k=3),
    # It takes a group of characters from the string ramdonly
    random.choices("holamundo", k=3),
)

# It returns a string which contains all characters in lowercase and uppercase
chars = string.ascii_letters
digits = string.digits  # It returns a string which contains all digits
seleccion = random.choices(chars + digits, k=16)
print(seleccion)

password = "".join(seleccion)
print(password)

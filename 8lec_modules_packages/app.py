# __pycache__ -> It's a mechanism to store compile bytecode files,
#   because Python compile the module when you execute it.
# in bytcode in order to accelerate execution every time program to be executed.

# module -> It's a single file containing variables, functions and classes.
#   Also, It can be imported in to another module.
# package -> It's a collection of modules with an _init_.py file,
#   Each Python package must contain an empty file named _init_.py

# It's bad practice use '*', since It import all functions.
#   Ejem: from users.actions import *
#
# If you have a function with the same name you can change it by using 'as'
#   Ejem: from users.actions import guardar as guardar_impuesto

# First way to import
from users.actions import guardar as guardar_impuesto, pagar_impuestos

# Second way to import
import users.hobbies

# Third way to import
from users import jobs


def guardar():
    print("soy app.py")


guardar()  # soy app.py

guardar_impuesto()  # guardando
pagar_impuestos()  # pagando impuestos

users.hobbies.cantar()  # cantando
users.hobbies.tocar("guitarra")  # tocando guitarra

jobs.profesor()  # enseniando
jobs.programador()  # codificando

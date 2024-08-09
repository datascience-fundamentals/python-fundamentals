# module -> It is a single Python file that can be imported into another module.
# __pycache__ is a mechanism to store compile bytecode files. When Python executes a module, compile it
# in bytcode in order to accelerate execution every time program to be executed.

# You can import functions from module like this.
# It's bad paractice to import all functions using '*'
# If you have a module with the same name you have to change its name using 'as'
from usuario_impuesto import guardar as guardar2, pagar_impuestos


def guardar():
    print("soy app.py")


guardar()  # soy app.py
guardar2()  # guardando
pagar_impuestos()  # pagando impuestos

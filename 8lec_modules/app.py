# module -> It is a single Python file that can be imported into another module.

# You can import functions from module like this.
# It's bad paractice to import all functions using '*'
# If you have a module with the same name you have to change its name using 'as'
from usuario_impuesto import guardar as guardar2, pagar_impuestos


def guardar():
    print("soy app.py")


guardar()  # soy app.py
guardar2()  # guardando
pagar_impuestos()  # pagando impuestos

# __name__ -> It's a dynamic variable whose value depends on where the module is being run from
# For example, If this script is being run directly then the __name__ 's value is gonna be "__main__"
# If helps you to control what code is beign executed if the program starts from this module.
from users.taxes.utils import pagar_impuestos

print(__name__)  # __main__


if __name__ == "__main__":
    print("La ejecucion inicio desde app3")

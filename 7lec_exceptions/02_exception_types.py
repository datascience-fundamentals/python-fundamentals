# except -> It allows you to catch an specific exception by its type
try:
    n1 = int(input("Ingresa un numero: "))
    asd
except ValueError as ex:  # catching ValueError type
    print("Ingrese un valor que corresponda")
except NameError as ex:  # catching NameError type
    print("Ocurrio un error de nombrado de variable")
except Exception as ex:  # catching an general exception
    print(type(ex))  # type allows you to know the error type

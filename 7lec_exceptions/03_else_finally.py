# else -> It executes whereas program ends with success
# finally -> It executes whether programs ends with sucess or throws an exception
try:
    n1 = int(input("Ingresa primer número: "))
except Exception as ex:
    print("Ocurrio un error!")
else:  # It executes whereas ends with success
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre")

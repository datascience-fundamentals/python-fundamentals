def division(n=0):
    if n == 0:
        # raise -> It allows you to throw an error
        raise ZeroDivisionError(
            "No se puede dividir por 0", f"divisor es: {n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as ex:
    print(ex)

# You can inherit from Exception to customize your own exception.
# If you want you could inherit from another specific Exception like ZeroDivisionError
class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

    def __str__(self):
        return f"{self.args[0]} - codigo: {self.code}"


def division(divisor=0):
    if divisor == 0:
        raise MiError("No se puede dividir por cero", 805)
    return 5 / divisor


try:
    division()
except MiError as ex:
    print(ex)

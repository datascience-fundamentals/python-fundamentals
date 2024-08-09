# There can be objects into another ones which helps you to declare
# a class instance (object) as a member from the another one.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 750)
bibicleta = Producto("Bicicleta", 1000)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deportes", [kayak, bibicleta])

deportes.agregar(surfboard)
deportes.imprimir()

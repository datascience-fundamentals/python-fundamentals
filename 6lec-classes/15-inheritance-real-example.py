class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando {self.tabla} por id {_id}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)

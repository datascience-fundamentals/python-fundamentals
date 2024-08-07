from abc import ABC, abstractmethod


# You can no instance a class which inheritance from ABC (Abstract class)
class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    # You aways have to override abstract method since It is required
    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        print(f"buscando {cls.tabla} por id {_id} en la tabla {cls.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(1)

# You can not instance an absctract class
# model = Model()

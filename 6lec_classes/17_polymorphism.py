# polymorphism: same method has diferent behaivors depending of instace object
# It allows objects of different classes to be used interchangeably if they are
# subclasses of the same parent class

from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Session(Model):

    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    entidadesModel = filter(
        lambda entidad: isinstance(entidad, Model), entidades)
    for entidad in entidadesModel:
        entidad.guardar()


usuario = Usuario()
session = Session()

guardar([usuario, session])

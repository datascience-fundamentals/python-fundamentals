class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


# This is an example of multiple inheritance
class Pato(Volador, Nadador, Caminador):
    def comer(self):
        print("comiendo")


pato = Pato()
pato.caminar()
pato.nadar()
pato.volar()
pato.comer()

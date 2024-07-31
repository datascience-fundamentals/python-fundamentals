class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        # It calls parent constructor in order to initilize volador property
        super().__init__()
        self.nadador = True

    # this method overrides parent method from Ave
    def vuela(self):
        print("vuela pato")
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)

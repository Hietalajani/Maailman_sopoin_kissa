class Esine:
    def __init__(self, nimi):
        self.nimi = nimi

    def metodi(self):
        pass


class Herkkutikku(Esine):
    def __init__(self):
        super().__init__("Herkkutikku")
        self.pisteet = 500


class Kissanminttu(Esine):
    def __init__(self):
        super().__init__("Kissanminttu")
        self.pisteet = 1000


class Tonnikala(Esine):
    def __init__(self):
        super().__init__("Tonnikala")
        self.pisteet = 750

class Kissa(Esine):
    def __init__(self, loydetty):
        self.loydetty = loydetty
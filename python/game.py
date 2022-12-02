class Kentta:
    def __init__(self, kentta, sijainti, esine, icao):
        self.kentta = kentta

    def metodi(self):

class Peli:
    def __init__(self, pelaajanimi, peliid, sijainti, karsivallisyyskulunut, tila, aiempisijainti):
        self.pelaajanimi = pelaajanimi
        self.peliid = peliid
        self.sijainti = sijainti
        self.karsivallisyyskulunut = karsivallisyyskulunut
        self.tila = tila
        self.aiempisijainti = aiempisijainti
    def metodi(self):

class Tavoite:
    def __init__(self):
    def metodi(self):

class Ilma:
    def __init__(self, kentta):
        self.kentta = Kentta.get(kentta)
        def metodi(self):

class Esine:
    def __init__(self, nimi, karsivallisyys):
        self.nimi = nimi
        self.karsivallisyys = karsivallisyys
        def metodi(self):
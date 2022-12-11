import random
import string


class Peli:
    def __init__(self, pelaajanimi, peliid, sijainti, karsivallisyyskulunut, tila, aiempisijainti):
        self.pelaajanimi = pelaajanimi
        self.peliid = peliid
        self.sijainti = sijainti
        self.karsivallisyyskulunut = karsivallisyyskulunut
        self.tila = tila
        self.aiempisijainti = aiempisijainti

        if peliid == 0:
            usable = string.ascii_lowercase + string.ascii_uppercase + string.digits

            self.status = {
                "peliid": ''.join(random.choice(usable) for i in range(20)),
                "pelaajanimi": pelaajanimi,
                "karsivallisyys": {
                    "karsivallisyyskulunut": karsivallisyyskulunut,
                    "karsivallisyysmax": karsivallisyysmax
                }

            }

    def metodi(self):
        pass

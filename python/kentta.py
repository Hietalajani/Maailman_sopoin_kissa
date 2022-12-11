import game

class Kentta:
    def __init__(self, kentta, data = None):
        self.kentta = kentta

        if data is None:
            sql = f"select icao, nimi, leveyspiiri, pituuspiiri, maa from lentokentta where icao = '{icao}'"
            kursori = game.yhteys.cursor()
            kursori.execute(sql)

            vastaus = kursori.fetchall()
            if len(vastaus) == 1:
                self.icao = vastaus[0][0]
                self.nimi = vastaus[0][1]
                self.leveyspiiri = float(vastaus[0][2])
                self.pituuspiiri = float(vastaus[0][3])

        else:
            self.nimi = data['nimi']
            self.leveyspiiri = float(data['leveyspiiri'])
            self.pituuspiiri = float(data['pituuspiiri'])

    def haeIlma(self):
        pass

    def haekentat(self):
        lista = []

        sql = "select icao, nimi, leveyspiiri, pituuspiiri, maa from lentokentta "
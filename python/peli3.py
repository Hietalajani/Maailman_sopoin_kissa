import config
import mysql.connector
from random import randint

config.yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kisupeli2',
    user='root',
    password=config.pw,
    autocommit=True
)


class Pelaaja:
    def __init__(self, nimi):

        self.kursori = config.yhteys.cursor()
        self.sijainti = config.aloituspaikka
        self.nimi = nimi
        self.käydyt = []
        self.esineet = {}   # sanakirja, johon arvotaan esineet löydettäväksi

    def to_json(self):
        skirja = {
            "ID": self.tunnus,
            "Nimi": self.nimi,
            "Kisun kärsivällisyys": self.kisun_kärsivällisyys,
            "Käytetty kärsivällisyys": self.käytetty_kärsivällisyys,
            "Sijainti": self.sijainti
        }
        return skirja

    def hae_tiedot(self, tunnus):
        sql = f"SELECT * from peli where id = {tunnus};"
        self.kursori.execute(sql)
        muut_tiedot = self.kursori.fetchone()

        if muut_tiedot:
            self.tunnus = muut_tiedot[0]
            self.nimi = muut_tiedot[1]
            self.kisun_kärsivällisyys = muut_tiedot[2]
            self.käytetty_kärsivällisyys = muut_tiedot[3]
            self.sijainti = muut_tiedot[4]

    def matkusta(self, icao, peli_id):
        # jos yritettiin kutsua oikealla ID-arvolla
        if int(peli_id) == self.tunnus:
            self.kursori.execute("UPDATE peli SET sijainti = %s WHERE id = %s", (icao, self.tunnus))

        self.hae_tiedot(self.tunnus)

        return self

    def muuta_nimi(self, nimi):
        # config-tiedostosta arvot, nimestä ensimmäiset 16 merkkiä, koska pelaaja_nimi tietokannassa varchar(16)
        self.kursori.execute(
            "INSERT INTO peli(pelaaja_nimi, kissa_karsivallisyys, kaytetty_karsivallisyys, sijainti) "
            "values(%s, %s, 0, %s);",
            (nimi[:16], config.kissan_kärsivällisyys, config.aloituspaikka))

        # haetaan uusin tunnus (auto increment) tietokannasta
        sql = "SELECT max(id) FROM peli;"
        self.kursori.execute(sql)
        tunnus = self.kursori.fetchone()

        if not tunnus:
            raise Exception("Pelaajan luominen epäonnistui.")

        self.tunnus = tunnus[0]
        self.hae_tiedot(self.tunnus)

        self.tuo_kentät()
        self.arvo_esineet()

        return self

    def tuo_kentät(self):
        # haetaan lentokentät tietokannasta
        self.kentät = {}

        sql = "SELECT * FROM lentokentta;"
        self.kursori.execute(sql)
        kentät = self.kursori.fetchall()

        if not kentät:
            raise Exception("Kenttien haku tietokannansta epäonnistui.")

        numero = 0
        for kenttä in kentät:
            self.kentät[numero] = {
                "icao": kenttä[0],
                "nimi": kenttä[1],
                "leveyspiiri": kenttä[2],
                "pituuspiiri": kenttä[3],
                "maa": kenttä[4]
            }
            numero += 1

    def arvo_esineet(self):
        for esine in config.esineiden_arvot.values():
            for n in range(esine[1]):
                num = randint(0, len(self.kentät) - 1)
                while num in self.esineet:
                    num = randint(0, len(self.kentät) - 1)
                self.esineet[num] = {
                    "esine": esine[0],
                    "pisteet": esine[2],
                    "sijainti": self.kentät[num]
                }


def pistetaulukko():
    kursori = config.yhteys.cursor()
    kursori.execute("SELECT id, pelaaja_nimi, (kissa_karsivallisyys - kaytetty_karsivallisyys) as pojot "
                    "from peli ORDER BY pojot DESC LIMIT 10;")
    pisteet = kursori.fetchall()
    ret_json = {}
    laskuri = 0
    if pisteet:
        for tulos in pisteet:
            ret_json[laskuri] = {
                "spot": laskuri,
                "ID": tulos[0],
                "name": tulos[1],
                "score": tulos[2]
            }
            laskuri += 1
    return ret_json


sessioukko = Pelaaja("Placeholder")


if __name__ == "__main__":
    testi = sessioukko.muuta_nimi("Sessiotesti")
    print(len(testi.kentät))
    print(type(testi.kentät))
    for kenttä_n in testi.kentät.values():
        print(kenttä_n["maa"])
    for testine in testi.esineet.values():
        print(testine)

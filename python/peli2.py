import config


class Pelaaja:
    def __init__(self, aloita, kohde, nimi, peli_id):

        self.kursori = config.yhteys.cursor()

        if aloita:  # jos aloita on True, halutaan uusi peli
            # config-tiedostosta arvot, nimestä ensimmäiset 16 merkkiä, koska pelaaja_nimi tietokannassa varchar(16)
            self.kursori.execute(
                "INSERT INTO peli(pelaaja_nimi, kissa_karsivallisyys, kaytetty_karsivallisyys, sijainti) "
                "values(%s, %s, 0, %s);",
                (nimi[:16], config.kissan_kärsivällisyys, config.aloituspaikka))

            sql = "SELECT max(id) FROM peli;"
            self.kursori.execute(sql)
            tunnus = self.kursori.fetchone()

            if not tunnus:
                raise Exception("Pelaajan luominen epäonnistui.")

            self.tunnus = tunnus[0]

            self.hae_tiedot(self.tunnus)

        else:  # jos aloita on False, niin halutaan siirtää olemassaolevaa Pelaajaa
            self.kursori.execute("UPDATE peli SET sijainti = %s WHERE id = %s", (kohde, peli_id))

            self.hae_tiedot(peli_id)

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

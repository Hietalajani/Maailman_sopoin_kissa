import mysql.connector
import random

lentokentät = {}

# Tällä funktiolla haetaan lentokenttien ICAO-koodit ja asetetaan niille arvoksi kyseisellä kentällä oleva
# asia: herkkutikku, tonnikala, kissanminttu tai kissa. Tallennetaan ICAOt ja niiden arvot sanakirjaan lentokentät.
# Funktio palauttaa sanakirjan.
def kenttienarvot():
    # Mielekkyyden vuoksi otetaan vain yksi lentokenttä per maa, siksi group by iso_country
    sql = '''select ident from airport 
    where continent = "EU" and type = "balloonport" and not iso_country = "RU" 
    group by iso_country;'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    icaot = kursori.fetchall()
    kissaluku = random.randint(0, 35)

    # Kissa sujahtaa lentokentälle
    lentokentät[icaot[kissaluku][0]] = 'Kissa'

    # Määritetään 6 lentokenttää joihin tulee herkkutikku
    for kierros in range(6):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in lentokentät:
                lentokentät[icaot[kentänarvo][0]] = 'Herkkutikku'
                successful = True

    # 5 lentokenttää joihin tulee tonnikala
    for kierros in range(5):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in lentokentät:
                lentokentät[icaot[kentänarvo][0]] = 'Tonnikala'
                successful = True

    # ja 4 lentokenttää joihin tulee kissanminttu
    for kierros in range(4):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in lentokentät:
                lentokentät[icaot[kentänarvo][0]] = 'Kissanminttu'
                successful = True


    return lentokentät

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='0232',
    autocommit=True
)

kenttienarvot()



import mysql.connector
import random

lentokentät = {}

def kenttienarvot():
    sql = '''select ident from airport 
    where continent = "EU" and type = "balloonport" and not iso_country = "RU" 
    group by iso_country;'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    icaot = kursori.fetchall()
    kissaluku = random.randint(0, 35)
    lentokentät[icaot[kissaluku][0]] = 'Kissa'
    for tuplet in icaot:
        h = 6
        t = 5
        k = 4

        for kierros in range(h):
            kentänarvo = random.randint(0,35)
            if kentänarvo == kissaluku:
                h += 1
                continue
            if icaot[kentänarvo][0] not in lentokentät:
                lentokentät[icaot[kentänarvo][0]] = 'Herkkutikku'









yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='0232',
    autocommit=True
)

kenttienarvot()



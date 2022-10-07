# Voisko importit tehdä jotenki tehokkaammin?
import mysql.connector
import random
from geopy import distance

# Muodostetaan yhteys tietokantaan
salasana = input("Anna salasana tietokantaan.")
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password=salasana,
    autocommit=True
)

# Tyhjä sanakirja lentokentille
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
    #   print(len(icaot))
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

# Läheiset_lentokentät tuottaa kaikki lentokentät alle 500km päässä nykyisestä (nimet, ei ICAO:t)
def läheiset_lentokentät(location):
    läheiset = []
    nykyisetkoordinaatit = f'''select latitude_deg, longitude_deg
    from airport where ident = "{location}";'''
    kaikkikoordinaatit = f'''select latitude_deg, longitude_deg, name
    from airport where continent = "EU" and type = "balloonport" and not iso_country = "RU";'''
    kursori = yhteys.cursor()
    kursori.execute(nykyisetkoordinaatit)
    nykyiset = kursori.fetchall()
    kursori.execute(kaikkikoordinaatit)
    kaikki = kursori.fetchall()
    for koordinaatit in kaikki:
        if 0 < distance.distance(nykyiset, koordinaatit[0:2]).km <= 500:
            läheiset.append(koordinaatit[2])
        else:
            pass
    return läheiset

# Uuden kentän nimi takaisin ICAO:ksi, tän ongelman voi varmaan jotenkin välttää lol
def icaoksi(nimi):
    sql = f'select ident from airport where name = "{nimi}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    icao = kursori.fetchone()
    return icao[0]

# Herkuntarkistus tarkistaa, onko uudella lentokentällä herkkua tai kissa, palauttaa herkun nimen
def herkuntarkistus(nimi):
    if nimi in lentokentät:
        print(f'Löytyi {lentokentät[nimi]}')
        return lentokentät[nimi]
    else:
        print('Ei löytynyt mitään :(')
        return "none"


# Määritellään kissan kärsivällisyys ja sen hiipuminen/nouseminen, annetaan herkulle muuttuja rekursioiden välttämiseksi

kisun_kärsivällisyys = 20000
def kärsivällisyyshiipuu(vanhalocation, uusilocation):
    kenttä1 = f'''select latitude_deg, longitude_deg from airport
    where ident = "{vanhalocation}";'''
    kenttä2 = f'''select latitude_deg, longitude_deg from airport
    where ident = "{uusilocation}";'''
    kursori = yhteys.cursor()
    kursori.execute(kenttä1)
    k1 = kursori.fetchall()
    kursori.execute(kenttä2)
    k2 = kursori.fetchall()
    matka = int(distance.distance(k1, k2).km)
    global kisun_kärsivällisyys
    global herkku
    if herkku != "none":
        if herkku == 'Herkkutikku':
            kisun_kärsivällisyys += 500
            print('Kissan kärsivällisyys kasvoi 500!')
        elif herkku == 'Tonnikala':
            kisun_kärsivällisyys += 750
            print('Kissan kärsivällisyys kasvoi 750!')
        elif herkku == 'Kissanminttu':
            kisun_kärsivällisyys += 1000
            print('Kissan kärsivällisyys kasvoi 1000!')
    kisun_kärsivällisyys -= matka
    print(f'Matkan keston takia kissan kärsivällisyys laski {matka}!')
    return

# Gameplay loop

# Peli arpoo kenttien arvot
kenttienarvot()

# Peli aloitetaan aina samasta paikasta? Vaikka Helsinki?
icao1 = 'EFHK'

# Peli tarjoaa käyttäjälle läheisiä lentokenttiä joihin voi lentää
print(f'Tässä läheisimmät kentät: {läheiset_lentokentät(icao1)}')

# Käyttäjä valitsee mille lentokentälle lentää
minne = int(input('Valitse mille lentokentälle haluat lentää seuraavaksi indeksiluvulla: '))
lentokenttä2 = läheiset_lentokentät(icao1)[minne]
icao2 = icaoksi(lentokenttä2)
herkku = herkuntarkistus(icao2)

# Kärsivällisyys hiipuu/nousee
kärsivällisyyshiipuu(icao1, icao2)
print(f'Kissan kärsivällisyyttä jäljellä: {kisun_kärsivällisyys}')
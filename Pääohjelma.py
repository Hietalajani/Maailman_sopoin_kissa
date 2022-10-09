# Voisko importit tehdä jotenki tehokkaammin?
import mysql.connector
import random
from geopy import distance


# Muodostetaan yhteys tietokantaan
# Funktio palauttaa luomansa yhteyden
def luo_yhteys():
    salasana = input("Anna salasana tietokantaan.")
    uusi_yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password=salasana,
        autocommit=True)
    return uusi_yhteys


# Tällä funktiolla haetaan lentokenttien ICAO-koodit ja asetetaan niille arvoksi kyseisellä kentällä oleva
# asia: herkkutikku, tonnikala, kissanminttu tai kissa.
# Tallennetaan ICAOt ja niiden arvot parametrina annettuun sanakirjaan.
# Funktio palauttaa sanakirjan.
def kenttienarvot(kentät, yhteys):
    # Mielekkyyden vuoksi otetaan vain yksi lentokenttä per maa, siksi group by iso_country
    sql = '''select ident from airport 
    where continent = "EU" and type = "balloonport" and not iso_country = "RU" 
    group by iso_country;'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    icaot = kursori.fetchall()
    #   print(len(icaot))   # testiprintti
    kissaluku = random.randint(0, len(icaot) - 1)

    # Kissa sujahtaa lentokentälle
    kentät[icaot[kissaluku][0]] = 'Kissa'

    # Määritetään 6 lentokenttää joihin tulee herkkutikku
    for kierros in range(6):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in kentät:
                kentät[icaot[kentänarvo][0]] = 'Herkkutikku'
                successful = True

    # 5 lentokenttää joihin tulee tonnikala
    for kierros in range(5):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in kentät:
                kentät[icaot[kentänarvo][0]] = 'Tonnikala'
                successful = True

    # ja 4 lentokenttää joihin tulee kissanminttu
    for kierros in range(4):
        successful = False
        while not successful:
            kentänarvo = random.randint(0, 35)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in kentät:
                kentät[icaot[kentänarvo][0]] = 'Kissanminttu'
                successful = True

    return kentät


# Läheiset_lentokentät tuottaa kaikki lentokentät alle 500km päässä nykyisestä (nimet, ei ICAO:t)
def läheiset_lentokentät(location, yhteys):
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
def icaoksi(nimi, yhteys):
    sql = f'select ident from airport where name = "{nimi}";'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    icao = kursori.fetchone()
    return icao[0]


# Herkuntarkistus tarkistaa, onko uudella lentokentällä herkkua tai kissa, palauttaa herkun nimen
def herkuntarkistus(nimi, kentät):
    if nimi in kentät:
        print(f'Löytyi {kentät[nimi]}')
        return kentät[nimi]
    else:
        print('Ei löytynyt mitään :(')
        return "none"


# Määritellään kissan kärsivällisyyden hiipuminen/nouseminen,
# annetaan herkulle muuttuja rekursioiden välttämiseksi
def kärsivällisyyshiipuu(vanhalocation, uusilocation, yhteys, kärsivällisyys):
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
    global herkku
    if herkku != "none":
        if herkku == 'Herkkutikku':
            kärsivällisyys += 500
            print('Kissan kärsivällisyys kasvoi 500!')
        elif herkku == 'Tonnikala':
            kärsivällisyys += 750
            print('Kissan kärsivällisyys kasvoi 750!')
        elif herkku == 'Kissanminttu':
            kärsivällisyys += 1000
            print('Kissan kärsivällisyys kasvoi 1000!')
    kärsivällisyys -= matka
    print(f'Matkan keston takia kissan kärsivällisyys laski {matka}!')
    return kärsivällisyys


if __name__ == '__main__':
    # luodaan yhteys
    peliyhteys = luo_yhteys()    # huomaa vastata salasanakyselyyn konsolissa

    # Tyhjä sanakirja lentokentille
    lentokentät = {}
    # määritellään kisulle kärsivällisyysarvo
    kisun_kärsivällisyys = 20000

    # Peli arpoo kenttien arvot
    kenttienarvot(lentokentät, peliyhteys)

    # Peli aloitetaan aina samasta paikasta? Vaikka Helsinki?
    icao1 = 'EFHK'

    # Gameplay loop
    while kisun_kärsivällisyys > 0:
        # Peli tarjoaa käyttäjälle läheisiä lentokenttiä joihin voi lentää
        print(f'Tässä läheisimmät kentät: {läheiset_lentokentät(icao1, peliyhteys)}')

        # Käyttäjä valitsee mille lentokentälle lentää
        minne = int(input('Valitse mille lentokentälle haluat lentää seuraavaksi indeksiluvulla: '))
        lentokenttä2 = läheiset_lentokentät(icao1, peliyhteys)[minne]
        icao2 = icaoksi(lentokenttä2, peliyhteys)
        herkku = herkuntarkistus(icao2, lentokentät)

        # Kärsivällisyys hiipuu/nousee
        kisun_kärsivällisyys = kärsivällisyyshiipuu(icao1, icao2, peliyhteys, kisun_kärsivällisyys)
        print(f'Kissan kärsivällisyyttä jäljellä: {kisun_kärsivällisyys}\n')

        # muutetaan uusi sijainti nykyiseksi sijainniksi
        icao1 = icao2

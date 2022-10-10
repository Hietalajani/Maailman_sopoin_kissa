"""
TODO:
- funktiot muuttamaan tietokantaa
- oma funktio juttujen (kissa, herkut) lisäämiseksi kentille
"""

# Voisko importit tehdä jotenki tehokkaammin?
import mysql.connector
from random import randint
from geopy import distance


# Muodostetaan yhteys tietokantaan
# Funktio palauttaa luomansa yhteyden
def luo_yhteys():
    salasana = input("Anna salasana tietokantaan: ")
    uusi_yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='kisupeli',
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
    and not iso_country = "ES" and not iso_country = "FR" and not iso_country = "PT" 
    and not iso_country = "IS" group by iso_country;'''
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    icaot = kursori.fetchall()
    #   print(len(icaot))   # testiprintti
    kissaluku = randint(0, len(icaot) - 1)

    # Kissa sujahtaa lentokentälle
    kentät[icaot[kissaluku][0]] = 'Kissa'

    # Määritetään 6 lentokenttää joihin tulee herkkutikku
    for kierros in range(6):
        successful = False
        while not successful:
            kentänarvo = randint(0, len(icaot) - 1)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in kentät:
                kentät[icaot[kentänarvo][0]] = 'Herkkutikku'
                successful = True

    # 5 lentokenttää joihin tulee tonnikala
    for kierros in range(5):
        successful = False
        while not successful:
            kentänarvo = randint(0, len(icaot) - 1)
            if kentänarvo == kissaluku:
                continue
            elif icaot[kentänarvo][0] not in kentät:
                kentät[icaot[kentänarvo][0]] = 'Tonnikala'
                successful = True

    # ja 4 lentokenttää joihin tulee kissanminttu
    for kierros in range(4):
        successful = False
        while not successful:
            kentänarvo = randint(0, len(icaot) - 1)
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
    from airport where continent = "EU" and type = "balloonport" and not iso_country = "RU" 
    and not iso_country = "ES" and not iso_country = "FR" and not iso_country = "PT" 
    and not iso_country = "IS" group by iso_country;'''
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(nykyisetkoordinaatit)
    nykyiset = kursori.fetchall()
    kursori.execute(kaikkikoordinaatit)
    kaikki = kursori.fetchall()
    kopio = []
    kopio.extend(kaikki)
    n = 1
    while n <= 5:
        minimi = 1000000
        for koordinaatit in kopio:
            if 0 < distance.distance(nykyiset, koordinaatit[0:2]) < minimi:
                minimi = distance.distance(nykyiset, koordinaatit[0:2])
        for koordinaatit in kopio:
            if distance.distance(nykyiset, koordinaatit[0:2]) == minimi:
                läheiset.append(koordinaatit[2])
                kopio.remove(koordinaatit)
                break
        n += 1

    return läheiset


# Uuden kentän nimi takaisin ICAO:ksi, tän ongelman voi varmaan jotenkin välttää lol
def icaoksi(nimi, yhteys):
    sql = f'select ident from airport where name = "{nimi}";'
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql)
    icao = kursori.fetchone()
    return icao[0]


# Herkuntarkistus tarkistaa, onko uudella lentokentällä herkkua tai kissa, palauttaa herkun nimen
def herkuntarkistus(icao, kentät):
    if icao in kentät:
        print(f'\nLöytyi {kentät[icao]}')
        nimi = kentät.pop(icao)
        return nimi
    else:
        print('\nEi löytynyt mitään :(')
        return "none"


# Määritellään kissan kärsivällisyyden hiipuminen/nouseminen,
# annetaan herkulle muuttuja rekursioiden välttämiseksi
def kärsivällisyyshiipuu(vanhalocation, uusilocation, yhteys, kärsivällisyys):
    kenttä1 = f'''select latitude_deg, longitude_deg from airport
    where ident = "{vanhalocation}";'''
    kenttä2 = f'''select latitude_deg, longitude_deg from airport
    where ident = "{uusilocation}";'''
    kursori = yhteys.cursor(buffered=True)
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


# Lisää uuden pelaajan tietokantaan.
# tietokannassa auto_increment, joten id:tä ei tarvita
def luo_pelaaja(nimi, yhteys):
    # Lisätään uusi pelaaja annetulla nimi-parametrilla tietokantaan
    # screen_name=%s ja execute(sql2, nimi),
    # jotta käyttäjä ei voi syöttää omaa koodiaan. (Bobby Tables)
    sql1 = '''insert into game(co2_consumed, co2_budget, cat_patience_used, 
    cat_patience, screen_name, location) 
    values(0, 10000, 0, 2500, %s, "EFHK");'''
    kursori = yhteys.cursor(buffered=True)
    kursori.execute(sql1, (nimi,))
    sql2 = '''select id from game where screen_name = %s;'''
    kursori.execute(sql2, (nimi,))
    uusi_id = kursori.fetchone()
    if uusi_id:
        print(f'Pelaajanumerosi on: {uusi_id[0]}')
        return uusi_id[0]   # palautetaan id, jolla voi viitata uuteen pelaajaan tietokannassa
    else:
        print("False")
        return False


if __name__ == '__main__':
    # luodaan yhteys
    peliyhteys = luo_yhteys()    # huomaa vastata salasanakyselyyn konsolissa

    # Tyhjä sanakirja lentokentille
    lentokentät = {}
    # määritellään kisulle kärsivällisyysarvo
    kisun_kärsivällisyys = 2500

    # kysytään pelaajalle nimi
    syötetty_nimi = input("Kirjoita valitsemasi pelaajanimi ja paina enter:  ")
    pelaajan_nro = luo_pelaaja(f"{syötetty_nimi}", peliyhteys)

    # Peli arpoo kenttien arvot
    kenttienarvot(lentokentät, peliyhteys)

    # Peli aloitetaan aina samasta paikasta? Vaikka Helsinki?
    icao1 = 'EFHK'

    # Gameplay loop
    käydyt = []
    Kissa = False
    voitto = None
    # Oton push test3
    # Ohjeet käyttäjälle
    print('''
            Yhdellä Euroopan kuumailmapallokentistä piileskelee kissa, tehtäväsi on löytää tämä kissa ja palata takaisin lähtökentälle.
            Lähtökenttänä toimii Helsinki-Vantaa. 
            Ohjelma kertoo sinulle viisi lähintä kuumailmapallokenttää, voit lentää mille tahansa näistä kentistä. 
            Kentiltä voit löytää kissanminttua, tonnikalaa, herkkutikun tai et mitään.
            Kissan kärsivällisyydellä on rajansa ja mikäli kärsivällisyys pääsee loppumaan häviät pelin.
            Mitä pidempi lentomatka, sitä enemmän se kuluttaa kärsivällisyyttä.
            Kärsivällisyys kasvaa jos onnistut löytämään tonnikalaa, kissanminttua tai herkkutikkuja.
            Jos kissan kärsivällisyys loppuu häviät pelin, jos löydät kissan ja onnistut palaamaan lähtökentälle voitat pelin.
            ''')
    while kisun_kärsivällisyys > 0:
        input('Jatka painamalla enter\n')

        # Peli tarjoaa käyttäjälle läheisiä lentokenttiä joihin voi lentää
        print('Tässä lähimmät kentät:\n')

        # Tulostus for-loopin sisään ja tulostus selkenä numeroituna listana
        for indeksi, lentokenttä in enumerate(läheiset_lentokentät(icao1, peliyhteys), start=1):
            if lentokenttä not in käydyt:
                print('{0}. {1}'.format(indeksi, lentokenttä))
            else:
                print('{0}. {1}'.format(indeksi, lentokenttä), '(käyty)')

        # Käyttäjä valitsee mille lentokentälle lentää
        try:
            minne = int(input('\nValitse mille lentokentälle haluat lentää '
                              'seuraavaksi indeksiluvulla (negatiivinen lopettaa pelin): '))
            if minne < 0:
                kisun_kärsivällisyys = 0
            elif 0 < minne < 6:
                lentokenttä2 = läheiset_lentokentät(icao1, peliyhteys)[minne-1]
                icao2 = icaoksi(lentokenttä2, peliyhteys)
                herkku = herkuntarkistus(icao2, lentokentät)
                käydyt.append(lentokenttä2)
                if herkku == "Kissa":
                    Kissa = True

                # Kärsivällisyys hiipuu/nousee
                kisun_kärsivällisyys = kärsivällisyyshiipuu(icao1, icao2, peliyhteys, kisun_kärsivällisyys)
                print(f'Kissan kärsivällisyyttä jäljellä: {kisun_kärsivällisyys}\n')

                # muutetaan uusi sijainti nykyiseksi sijainniksi
                icao1 = icao2
                if icao1 == 'EFHK' and Kissa:
                    voitto = True
                    break
            else:
                print("Valitse arvo annettujen kenttien mukaisesti.")

        except ValueError:
            print("Syötä parempi arvo!")

    if kisun_kärsivällisyys <= 0:
        voitto = False
    if voitto:
        print('Mahtavaa! Voitit pelin!')
    else:
        print('Kisun kärsivällisyys loppui. Hävisit pelin.')


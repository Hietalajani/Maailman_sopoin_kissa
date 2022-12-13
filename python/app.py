from flask import Flask, request
import mysql.connector
import config
import peli2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


config.yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='kisupeli2',
            user='root',
            password=config.pw,
            autocommit=True
        )


def muuta_sijainti(aloita, kohde, nimi="", tunnus=0):
    pelaaja = peli2.Pelaaja(aloita, kohde, nimi, tunnus)
    return pelaaja.to_json()


# http://127.0.0.1:3000/uusi_peli?nimi=Puliukko
@app.route('/uusi_peli')
def uusi_peli():
    args = request.args
    nimi = args.get("nimi")
    json_data = muuta_sijainti(True, config.aloituspaikka, nimi)
    return json_data


# http://127.0.0.1:3000/matkusta?id=28&kohde=EETN
@app.route('/matkusta')
def matkusta():
    args = request.args
    peli_id = args.get("id")
    kohde = args.get("kohde")
    json_data = muuta_sijainti(False, kohde, tunnus=int(peli_id))
    return json_data


# http://127.0.0.1:3000/pistetaulukko
@app.route('/pistetaulukko')
def pistetaulukko():
    json_data = peli2.pistetaulukko()
    return json_data


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

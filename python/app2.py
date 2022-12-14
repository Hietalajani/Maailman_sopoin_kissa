from flask import Flask, request
import peli3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def muuta_sijainti(kohde, peli_id):
    pelaaja = peli3.sessioukko.matkusta(kohde, peli_id)
    return pelaaja.to_json()


# http://127.0.0.1:3000/uusi_peli?nimi=Puliukko
@app.route('/uusi_peli')
def uusi_peli():
    args = request.args
    nimi = args.get("nimi")
    pelaaja = peli3.sessioukko.muuta_nimi(nimi)
    json_data = pelaaja.to_json()
    return json_data


# http://127.0.0.1:3000/matkusta?id=28&kohde=EETN
@app.route('/matkusta')
def matkusta():
    args = request.args
    peli_id = args.get("id")
    kohde = args.get("kohde")
    json_data = muuta_sijainti(kohde, peli_id)
    return json_data


# http://127.0.0.1:3000/pistetaulukko
@app.route('/pistetaulukko')
def pistetaulukko():
    json_data = peli3.pistetaulukko()
    return json_data


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

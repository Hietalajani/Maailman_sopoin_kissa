from esine import Esine
from tavoite import Tavoite
from peli import Peli
from kentta import Kentta
import mysql.connector
from flask import Flask

app = Flask(__name__)


@app.route("/testipisteet")
def testipisteet():
    ret = []
    # select id, pelaaja_nimi, (kissa_karsivallisyys - kaytetty_karsivallisyys) as pojot
    # from peli
    # order by pojot desc limit 10
    for i in range(10):
        uusi = {"spot": i, "name": f"Pelaaja {i}", "score": i * 500}
        ret.append(uusi)
    return ret


# pw = input("Anna tietokannan salasana:")
# yhteys = mysql.connector.connect(
#     host='127.0.0.1',
#     port=3306,
#     database='kisupeli2',
#     user='root',
#     password=pw,
#     autocommit=True
# )

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

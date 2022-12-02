from esine import Esine
from tavoite import Tavoite
from peli import Peli
from kentta import Kentta
import mysql.connector
from flask import Flask

app = Flask(__name__)
pw = input("Anna tietokannan salasana:")
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kisupeli2',
    user='root',
    password=pw,
    autocommit=True
)

def hae_tietokannasta():
    pass

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

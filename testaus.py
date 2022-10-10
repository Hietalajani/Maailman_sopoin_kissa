import unittest
import Pääohjelma


class Testit(unittest.TestCase):
    def testaa_pariton(self):   # esimerkin vuoksi tässä
        luku = int(input("Anna pariton luku."))
        tulos = (luku % 2 == 1)
        print(tulos)
        self.assertEqual(tulos, True)  # add assertion here

    """
    def yhteystesti(self):
        uusi_yhteys = Pääohjelma.luo_yhteys()
        self.assertIsInstance(uusi_yhteys, mysql.connector.connection_cext.CMySQLConnection)
    """

    def kenttätesti(self):
        kentät = {}  #
        Pääohjelma.kenttienarvot(kentät, testiyhteys)
        # pitää olla 16 pitkä lista, koska on lisätty
        # kissa, 6 herkkutikkua, 5 tonnikalaa ja 4 kissanminttua
        pituus = len(kentät)
        self.assertEqual(pituus, 16)


if __name__ == '__main__':
    testiyhteys = Pääohjelma.luo_yhteys()
    unittest.main()

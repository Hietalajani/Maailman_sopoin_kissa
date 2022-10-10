import unittest


class Testit(unittest.TestCase):
    def testaa_pariton(self):
        luku = int(input("Anna pariton luku."))
        tulos = (luku % 2 == 1)
        print(tulos)
        self.assertEqual(tulos, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

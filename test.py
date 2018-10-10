from fileS import devuelveTrue
import unittest

class SoloTest(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(devuelveTrue(), "devuelveTrue devuelve True")

if __name__ == '__main__':
    unittest.main()

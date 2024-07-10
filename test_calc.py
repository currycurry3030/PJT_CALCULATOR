from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_get_zegop(self):
        self.calc = Calc()
        self.assertEqual(81, self.calc.getZegop(9))
        
    def test_getGop(self):
        self.calc = Calc()
        self.assertEqual(12, self.calc.getGop(3, 4))

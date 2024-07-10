from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_getGop(self):
        self.calc = Calc()
        self.assertEqual(12, self.calc.getGop(3, 4))

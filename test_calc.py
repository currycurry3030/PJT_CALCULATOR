from unittest import TestCase
from calc import Calc

class TestCalc(TestCase):

    def setUp(self):
        super().setUp()
        self.calc = Calc()

    def test_getMinus_1_2(self):
        self.assertEqual(-1, self.calc.getMinus(1, 2))

    def test_getMinus_2_1(self):
        self.assertEqual(1, self.calc.getMinus(2, 1))

    def test_getDivide_6_3(self):
        self.assertEqual(2.0, self.calc.getDivide(6, 3))

    def test_getMinus_2_4(self):
        self.assertEqual(0.5, self.calc.getDivide(2, 4))



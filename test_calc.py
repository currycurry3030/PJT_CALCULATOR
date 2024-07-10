from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):

    def setUp(self):
        super().setUp()
        self.calc = Calc()

    def test_get_sum_sum(self):
        self.assertEqual(self.calc.get_sum_sum(1, 2, 3), 6)
        self.assertEqual(self.calc.get_sum_sum(2, 3, 4), 9)
        self.assertEqual(self.calc.get_sum_sum(-3, 3, 8), 8)
        self.assertEqual(self.calc.get_sum_sum(1, -13, -20), -32)
        self.assertEqual(self.calc.get_sum_sum(73, 13, -103), -17)

    def test_get_zegop(self):
        self.calc = Calc()
        self.assertEqual(81, self.calc.getZegop(9))
        
    def test_getGop(self):
        self.calc = Calc()
        self.assertEqual(12, self.calc.getGop(3, 4))


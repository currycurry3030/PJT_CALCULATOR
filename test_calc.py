from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):

    def setUp(self):
        super().setUp()
        self.calc = Calc()

    def test_get_sum_sum(self):
        self.assertEqual(self.calc.get_sum_sum(1, 2, 3), 6)



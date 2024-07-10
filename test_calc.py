from unittest import TestCase
from calc import Calc


class TestCalc(TestCase):
    pass

    def test_get_sum_sum(self):
        calc = Calc()

        result = calc.get_sum_sum(1, 2, 3)

        self.assertEqual(result, 6)


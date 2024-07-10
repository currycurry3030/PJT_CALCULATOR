from unittest import TestCase
from calc import Calc

class TestCalc(TestCase):
    def setUp(self):
        super().setUp()
        self.calc = Calc()

    def test_get_sum(self):
        lst_pair_number = [(1, 2, 3),
                           (300, 8, 308),
                           (1.3, 8, 9.3),
                           (1.2, 2.3, 3.5)]
        for (number_1, number_2, ans) in lst_pair_number:
            ret = self.calc.getSum(number_1,number_2)
            self.assertEqual(ans, ret)
import unittest
from algorithms import *


class TestAlgorithms(unittest.TestCase):

    def test_sum_list_answer(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([2, 4, 6]), 12)

    def test_sum_list_input(self):
        self.assertRaises(TypeError, sum_list, True)

    def test_int_to_str(self):
        self.assertEqual(int_to_str(1), '1')

    def test_int_to_str_value(self):
        self.assertRaises(TypeError, int_to_str, True)

import unittest

from day04.day04 import solve


class TestDay04(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day04/input.txt')[0], 569)

    def test_task2_input_01(self):
        self.assertEqual(solve('day04/input.txt')[1], 936)

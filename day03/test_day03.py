import unittest

from day03.day03 import solve


class TestDay03(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day03/input.txt')[0], 8105)

    def test_task2_input_01(self):
        self.assertEqual(solve('day03/input.txt')[1], 2363)

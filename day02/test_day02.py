import unittest

from day02.day02 import solve


class TestDay02(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day02/input.txt')[0], 11603)

    def test_task2_input_01(self):
        self.assertEqual(solve('day02/input.txt')[1], 12725)

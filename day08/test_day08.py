import unittest

from day08.day08 import solve


class TestDay00(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day08/input.txt')[0], 1763)

    def test_task2_input_01(self):
        self.assertEqual(solve('day08/input.txt')[1], 671160)

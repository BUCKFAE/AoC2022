import unittest

from day01.day01 import solve


class TestDay01(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day01/input.txt')[0], 69501)

    def test_task2_input_01(self):
        self.assertEqual(solve('day01/input.txt')[1], 202346)

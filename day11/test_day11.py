import unittest

from day11.day11 import solve


class TestDay11(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day11/sample_input.txt', 1), 10605)


    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day11/sample_input.txt', 2), 2713310158)

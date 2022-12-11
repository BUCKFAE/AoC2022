import unittest

from day11.day11 import solve


class TestDay09(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day10/sample_input.txt')[0], 0)


    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day10/sample_input.txt')[1], 0)

import unittest

from day12.day12 import solve


class TestDay12(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day12/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day12/sample_input.txt')[1], 0)

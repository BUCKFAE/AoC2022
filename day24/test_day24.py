import unittest

from day24.day24 import solve


class TestDay24(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day24/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day24/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day24/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day24/input.txt')[1], 0)
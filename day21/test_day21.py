import unittest

from day21.day21 import solve


class TestDay21(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day21/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day21/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day21/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day21/input.txt')[1], 0)
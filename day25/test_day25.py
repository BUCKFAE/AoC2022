import unittest

from day25.day25 import solve


class TestDay25(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day25/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day25/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day25/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day25/input.txt')[1], 0)
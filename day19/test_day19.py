import unittest

from day19.day19 import solve


class TestDay19(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day19/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day19/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day19/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day19/input.txt')[1], 0)
import unittest

from day14.day14 import solve


class TestDay14(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day14/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day14/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day14/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day14/input.txt')[1], 0)
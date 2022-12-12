import unittest

from day00.day00 import solve


class TestDay00(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day00/sample_input.txt')[0], 0)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day00/sample_input.txt')[1], 0)

    def test_task1_input_01(self):
        self.assertEqual(solve('day00/input.txt')[0], 0)

    def test_task2_input_01(self):
        self.assertEqual(solve('day00/input.txt')[1], 0)

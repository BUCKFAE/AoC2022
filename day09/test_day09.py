import unittest

from day09.day09 import solve, are_adjacent


class TestDay09(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day09/sample_input.txt', 2), 13)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day09/sample_input.txt', 10), 1)

    def test_task2_sample_input_02(self):
        self.assertEqual(solve('day09/sample_input_2.txt', 10), 36)

    def test_are_adjacent(self):
        self.assertTrue(are_adjacent((0, 0), (0, 0)))
        self.assertTrue(are_adjacent((0, 0), (1, 0)))
        self.assertTrue(are_adjacent((2, 2), (1, 2)))
        self.assertTrue(are_adjacent((0, 0), (1, 1)))

        self.assertFalse(are_adjacent((0, 0), (2, 0)))

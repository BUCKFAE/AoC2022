import unittest

from day06.day06 import solve


class TestDay06(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day06/input.txt')[0], 1953)

    def test_task2_input_01(self):
        self.assertEqual(solve('day06/input.txt')[1], 2301)

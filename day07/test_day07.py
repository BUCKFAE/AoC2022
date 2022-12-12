import unittest

from day07.day07 import solve


class TestDay00(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day07/input.txt')[0], 1477771)

    def test_task2_input_01(self):
        self.assertEqual(solve('day07/input.txt')[1], 3579501)

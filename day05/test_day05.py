import unittest

from day05.day05 import solve


class TestDay05(unittest.TestCase):

    def test_task1_input_01(self):
        self.assertEqual(solve('day05/input.txt')[0], 'MQSHJMWNH')

    def test_task2_input_01(self):
        self.assertEqual(solve('day05/input.txt')[1], 'LLWJRBHVZ')

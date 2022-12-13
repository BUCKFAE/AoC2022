import unittest

from day13.day13 import solve, compare


class TestDay13(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day13/sample_input.txt')[0], 13)

    def test_task2_sample_input_01(self):
        self.assertEqual(solve('day13/sample_input.txt')[1], 140)

    def test_compare(self):
        self.assertTrue(compare([1,1,3,1,1], [1,1,5,1,1]))
        self.assertTrue(compare([[1],[2,3,4]], [[1],4]))
        self.assertFalse(compare([9], [[8,7,6]]))
        self.assertTrue(compare([[4,4],4,4], [[4,4],4,4,4]))
        self.assertFalse(compare([7,7,7,7], [7,7,7]))
        self.assertTrue(compare([], [3]))
        self.assertFalse(compare([[[]]], [[]]))
        self.assertFalse(compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))


    def test_task1_input_01(self):
        self.assertEqual(solve('day13/input.txt')[0], 5196)

    def test_task2_input_01(self):
        self.assertEqual(solve('day13/input.txt')[1], 22134)

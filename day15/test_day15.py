import unittest

from day15.day15 import solve


class TestDay15(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day15/sample_input.txt', 10)[0], 26)

    def test_task1_sample_input_02(self):
        self.assertEqual(solve('day15/sample_input.txt', 11)[0], 27)
        pass

    def test_task1_sample_input_03(self):
        self.assertEqual(solve('day15/sample_input.txt', 9)[0], 25)

    def test_task2_sample_input_01(self):
        #self.assertEqual(solve('day15/sample_input.txt', 0)[1], 0)
        pass

    def test_task1_input_01(self):
        # self.assertEqual(solve('day15/input.txt', 2000000)[0], 0)
        pass

    def test_task2_input_01(self):
        # self.assertEqual(solve('day15/input.txt', 0)[1], 0)
        pass

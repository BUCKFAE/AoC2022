import unittest

from day10.day10 import solve, simulate_cycles


class TestDay10(unittest.TestCase):

    def test_task1_sample_input_01(self):
        self.assertEqual(solve('day10/sample_input.txt')[0], 13140)

    def test_simulate_cycles(self):
        cycle_values = simulate_cycles('day10/sample_input.txt')

        self.assertEqual(cycle_values[20], 420)
        self.assertEqual(cycle_values[60], 1140)
        self.assertEqual(cycle_values[100], 1800)
        self.assertEqual(cycle_values[140], 2940)
        self.assertEqual(cycle_values[180], 2880)
        self.assertEqual(cycle_values[220], 3960)


    def test_task2_sample_input_01(self):

        img = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

        print (f'Solution:\n{img}')

        res = solve('day10/sample_input.txt')[1]
        print(f'Actual:\n{res}')

        self.assertEqual(res, img)

    def test_task1_input_01(self):
        self.assertEqual(solve('day10/input.txt')[0], 13680)

    def test_task2_input_01(self):
        res = """###..####..##..###..#..#.###..####.###..
#..#....#.#..#.#..#.#.#..#..#.#....#..#.
#..#...#..#....#..#.##...#..#.###..###..
###...#...#.##.###..#.#..###..#....#..#.
#....#....#..#.#....#.#..#....#....#..#.
#....####..###.#....#..#.#....####.###.."""
        self.assertEqual(solve('day10/input.txt')[1], res)

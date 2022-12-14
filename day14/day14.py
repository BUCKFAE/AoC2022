from __future__ import annotations

import os
import numpy as np

def simulate_sand(grid: np.ndarray, start: int, is_task2: bool = False):

    sand_placed = 0

    while True:

        sand: tuple[int, int] = (start, 0)
        sand_placed += 1

        # Moving sand until it stops
        while True:

            if not(0 <= sand[1] < grid.shape[0] - 1 and 0 <= sand[0] < grid.shape[1] - 1):
                if not is_task2:
                    break
                else:
                    grid[sand[1]][sand[0]] = 3
                    break

            # Moving one down
            if grid[sand[1] + 1][sand[0]] == 0:
                grid[sand[1] + 1][sand[0]] = 2
                grid[sand[1]][sand[0]] = 0
                sand = (sand[0], sand[1] + 1)
            # Moving left down
            elif grid[sand[1] + 1][sand[0] - 1] == 0:
                grid[sand[1] + 1][sand[0] - 1] = 2
                grid[sand[1]][sand[0]] = 0
                sand = (sand[0] - 1, sand[1] + 1)
            # Moving right down
            elif grid[sand[1] + 1][sand[0] + 1] == 0:
                grid[sand[1] + 1][sand[0] + 1] = 2
                grid[sand[1]][sand[0]] = 0
                sand = (sand[0] + 1, sand[1] + 1)
            # Stopping
            else:
                grid[sand[1]][sand[0]] = 3
                break



        if not is_task2:
            if not(0 <= sand[1] < grid.shape[0] - 1 and 0 <= sand[0] < grid.shape[1] - 1):
                break
        else:
            if grid[0][start] == 3:
                break

    _print_grid(grid)
    return sand_placed - 1

def _print_grid(g: np.ndarray):
    print(str(g).replace('.', '').replace('0', '.').replace('1', '#').replace('3', 'o'))

def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

        start_x = min([min([int(p.split(',')[0]) for p in line.split(' -> ')]) for line in lines])
        end_x = max([max([int(p.split(',')[0]) for p in line.split(' -> ')]) for line in lines])
        start_y = min([min([int(p.split(',')[1]) for p in line.split(' -> ')]) for line in lines])
        end_y = max([max([int(p.split(',')[1]) for p in line.split(' -> ')]) for line in lines])

        size_x = end_x - start_x

        add_x = (end_y) * 2


        grid = np.zeros((end_y + 1, size_x + 1))
        grid2 = np.zeros((end_y + 2, size_x + add_x))

        for line in lines:
            points = [(int(x) - start_x, int(y)) for x, y in [coord.split(',') for coord in line.split(' -> ')]]
            print(points)

            last_point = points[0]
            for current_point in points[1:]:
                assert last_point[0] == current_point[0] or last_point[1] == current_point[1]

                # Horizontal line
                if last_point[0] == current_point[0]:
                    start = min(current_point[1], last_point[1])
                    end = max(current_point[1], last_point[1])
                    for y in range(start, end + 1):
                        grid[y, last_point[0]] = 1
                        grid2[y, last_point[0] + (add_x // 2)] = 1
                # Vertical line
                if last_point[1] == current_point[1]:
                    start = min(current_point[0], last_point[0])
                    end = max(current_point[0], last_point[0])
                    for x in range(start, end + 1):
                        grid[last_point[1], x] = 1
                        grid2[last_point[1], x + (add_x // 2)] = 1

                last_point = current_point

        sand_pos = 500 - start_x

    res1 = simulate_sand(grid, sand_pos)
    res2 = simulate_sand(grid2, sand_pos + (add_x // 2), is_task2=True) + 1

    return res1, res2


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day14/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')

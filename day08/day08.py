from __future__ import annotations

import os

import numpy as np


class Grid:
    def __init__(self, data: np.ndarray):
        self.data: np.ndarray = data

    def get_neighbors(self, x: int, y:int) -> list[int]:
        # Get all tiles up / left / right / down
        neighbors = []
        if x < self.data[0].size - 1:
            neighbors.append(self.data[y, x + 1])
        if x > 0:
            neighbors.append(self.data[y, x - 1])
        if y < self.data[1].size - 1:
            neighbors.append(self.data[y + 1, x])
        if y > 0:
            neighbors.append(self.data[y - 1, x])
        return neighbors

    def get_height(self, x: int, y: int) -> int:
        return self.data[y, x]

    def is_visible(self, x: int, y: int) -> bool:

        own_height = self.get_height(x, y)
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dir in directions:
            current = (x, y)

            visible = True
            while len(self.get_neighbors(current[0], current[1])) > 3:
                current = (current[0] + dir[0], current[1] + dir[1])

                if self.get_height(current[0], current[1]) >= own_height:
                    visible = False
                    break
            if visible:
                return True
        return False

    def get_tree_score(self, x: int, y: int) -> int:
        own_height = self.get_height(x, y)
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        score = 1

        for dir in directions:
            current = (x, y)

            dir_score = 0
            while len(self.get_neighbors(current[0], current[1])) > 3:
                current = (current[0] + dir[0], current[1] + dir[1])
                dir_score += 1

                if own_height <= self.get_height(current[0], current[1]):
                    break
            score *= max(1, dir_score)
        return score

    def get_all_coordinates(self) -> list[tuple[int, int]]:
        return [(x, y) for x in range(self.data[0].size) for y in range(self.data[1].size)]



def create_grid(input_file: str) -> Grid:
    assert os.path.exists(input_file), f'File {input_file} does not exist'
    with open(input_file, 'r') as f:
        arr = np.array([[int(n) for n in line.strip()] for line in f.read().splitlines() if line.strip()])
    return Grid(arr)

def solve(input_file: str)-> tuple[int, int]:

    grid = create_grid(input_file)


    res1 = sum([1 if grid.is_visible(x, y) else 0 for x, y in grid.get_all_coordinates()])

    best_tree = max(grid.get_all_coordinates(), key=lambda x: grid.get_tree_score(x[0], x[1]))
    res2 = grid.get_tree_score(best_tree[0], best_tree[1])


    return res1, res2


if __name__ == '__main__':

    sample_grid = create_grid('day08/sample_input.txt')

    # Getting neighbors
    assert sorted(sample_grid.get_neighbors(0, 0)) == [0, 2]
    assert sorted(sample_grid.get_neighbors(0, 1)) == [3, 5, 6]
    assert sorted(sample_grid.get_neighbors(4, 4)) == [9, 9]

    # Visibility
    assert sample_grid.is_visible(1, 1)
    assert not sample_grid.is_visible(2, 2)
    assert not sample_grid.is_visible(1, 3)
    assert sample_grid.is_visible(2, 3)
    assert not sample_grid.is_visible(3, 3)

    # Tree score
    assert sample_grid.get_tree_score(2, 1) == 4, f'Expected 4, got {sample_grid.get_tree_score(2, 1)}'
    assert sample_grid.get_tree_score(2, 3) == 8, f'Expected 8, got {sample_grid.get_tree_score(2, 1)}'

    # Solving sample inputs
    res_sample = solve('day08/sample_input.txt')
    assert res_sample[0] == 21, f'Expected 21, got {res_sample[0]}'
    assert res_sample[1] == 8, f'Expected 8, got {res_sample[1]}'

    # Solving real input
    res = solve('day08/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

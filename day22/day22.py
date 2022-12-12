from __future__ import annotations

import os

def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

    res1 = 0
    res2 = 0

    return res1, res2


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day22/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')
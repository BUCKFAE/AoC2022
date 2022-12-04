from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    with open(input_file, 'r') as f:
        for line in [line.strip() for line in f.read().splitlines() if line.strip()]:

            pass

    res1 = 0
    res2 = 0

    return res1, res2


if __name__ == '__main__':
    res_sample = solve('day04/sample_input.txt')
    #assert res_sample[0] == 2, f'Expected 2, got {res_sample[0]}'
    #assert res_sample[1] == 4, f'Expected 4, got {res_sample[1]}'

    res = solve('day04/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

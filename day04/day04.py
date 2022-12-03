from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    return 0, 0


if __name__ == '__main__':
    res_sample = solve('day04/sample_input.txt')
    #assert res_sample[0] == 157, f'Expected 157, got {res_sample[0]}'
    #assert res_sample[1] == 70, f'Expected 70, got {res_sample[1]}'

    res = solve('day04/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

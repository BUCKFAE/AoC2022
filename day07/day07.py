from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    with open(input_file, 'r') as f:
        file_text = f.read().splitlines()

    res1 = 0
    res2 = 0

    return res1, res2


if __name__ == '__main__':

    # Solving sample inputs
    res_sample_1 = solve('day07/sample_inputs/sample_input_1.txt')
    #assert res_sample_1[0] == 7, f'Expected 7, got {res_sample_1[0]}'
    #assert res_sample_1[1] == 19, f'Expected 19, got {res_sample_1[1]}'

    # Solving real input
    res = solve('day07/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    data = []

    with open(input_file, 'r') as f:
        tmp = [line.strip() for line in f.read().splitlines() if line.strip()]
        assert len(tmp) == 1, f'Expected 1 line, got {len(tmp)}'
        data = tmp[0]

    print(f'Data: {data}')

    res1 = 0
    res2 = 0

    # Part 1 - Sequence of 4 without repetition
    for idx in range(4, len(data)):
        if len(set(data[idx - 4:idx])) == 4:
            res1 = idx
            break

    # Part 2 - Sequence of 14 without repetition
    for idx in range(14, len(data)):
        if len(set(data[idx - 14:idx])) == 14:
            res2 = idx
            break

    return res1, res2


if __name__ == '__main__':

    # Solving sample inputs
    res_sample_1 = solve('day06/sample_inputs/sample_input_1.txt')
    assert res_sample_1[0] == 7, f'Expected 7, got {res_sample_1[0]}'
    assert res_sample_1[1] == 19, f'Expected 19, got {res_sample_1[1]}'
    res_sample_2 = solve('day06/sample_inputs/sample_input_2.txt')
    assert res_sample_2[0] == 5, f'Expected 5, got {res_sample_2[0]}'
    assert res_sample_2[1] == 23, f'Expected 23, got {res_sample_2[1]}'
    res_sample_3 = solve('day06/sample_inputs/sample_input_3.txt')
    assert res_sample_3[0] == 6, f'Expected 6, got {res_sample_3[0]}'
    assert res_sample_3[1] == 23, f'Expected 23, got {res_sample_3[1]}'
    res_sample_4 = solve('day06/sample_inputs/sample_input_4.txt')
    assert res_sample_4[0] == 10, f'Expected 10, got {res_sample_4[0]}'
    assert res_sample_4[1] == 29, f'Expected 29, got {res_sample_4[1]}'
    res_sample_5 = solve('day06/sample_inputs/sample_input_5.txt')
    assert res_sample_5[0] == 11, f'Expected 11, got {res_sample_5[0]}'
    assert res_sample_5[1] == 26, f'Expected 26, got {res_sample_5[1]}'

    # Solving real input
    res = solve('day06/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

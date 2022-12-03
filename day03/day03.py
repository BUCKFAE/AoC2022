from __future__ import annotations

import os
import string


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    backpacks: list[tuple[str, str]] = []

    with open(input_file, 'r') as f:
        for line in [line.strip() for line in f.read().splitlines()]:
            if not line: continue
            split_index = len(line) // 2

            backpacks.append((line[:split_index], line[split_index:]))

    assert all([len(c1) == len(c2) for (c1, c2) in backpacks]), 'Backpacks are not of equal length'

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    print(f'Alphabet: {alphabet}')

    res1 = 0
    for (c1, c2) in backpacks:
        matches = set([m for m in c1 if m in c2])
        print(f'{c1} {c2} {matches}')
        res1 += sum([alphabet.index(m) + 1 for m in matches])

    res2 = 0

    for group_id in range(0, len(backpacks), 3):
        print(f'Group {group_id}')
        b1 = set(backpacks[group_id][0] + backpacks[group_id][1])
        b2 = set(backpacks[group_id + 1][0] + backpacks[group_id + 1][1])
        b3 = set(backpacks[group_id + 2][0] + backpacks[group_id + 2][1])

        for c in b1:
            if c in b2 and c in b3:
                print(f'{c} in {b1} {b2} {b3}')
                res2 += alphabet.index(c) + 1
                continue

    return res1, res2


if __name__ == '__main__':
    res_sample = solve('day03/sample_input.txt')
    assert res_sample[0] == 157, f'Expected 157, got {res_sample[0]}'
    assert res_sample[1] == 70, f'Expected 70, got {res_sample[1]}'

    res = solve('day03/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

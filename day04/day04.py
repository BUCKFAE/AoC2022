from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'
    assignments: list[tuple[list[int], list[int]]] = []
    with open(input_file, 'r') as f:
        for line in [line.strip() for line in f.read().splitlines() if line.strip()]:
            p1, p2 = line.split(',')
            s1, e1 = [int(p) for p in p1.split('-')]
            s2, e2 = [int(p) for p in p2.split('-')]

            assignments.append((list(range(s1, e1 + 1)), list(range(s2, e2 + 1))))

            print(p1, p2)
    print(assignments)

    res1 = 0
    res2 = 0

    # Searching for overlap
    for (p1, p2) in assignments:

        # Task1: Full overlap
        if all([s in p2 for s in p1]) or all([s in p1 for s in p2]):
            print(f'{p1} {p2} overlap')
            res1 += 1

        # Task2: Partial overlap
        if any([s in p2 for s in p1]) or any([s in p1 for s in p2]):
            print(f'{p1} {p2} partial overlap')
            res2 += 1


    return res1, res2


if __name__ == '__main__':
    res_sample = solve('day04/sample_input.txt')
    assert res_sample[0] == 2, f'Expected 2, got {res_sample[0]}'
    assert res_sample[1] == 4, f'Expected 4, got {res_sample[1]}'

    res = solve('day04/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

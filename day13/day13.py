from __future__ import annotations

import os
from enum import Enum
from functools import cmp_to_key


class ComparisonResult(Enum):
    VALID = 1
    INVALID = 2
    UNKNOWN = 3

def compare(left, right):
    res = _compare(left, right)
    assert res != ComparisonResult.UNKNOWN, f'Unknown result for {left} and {right}'
    return res == ComparisonResult.VALID

def _compare(left, right) -> ComparisonResult:

    print(f'Compare {left} and {right}')

    # Two integers
    if type(left) == int and type(right) == int:
        if left == right:
            return ComparisonResult.UNKNOWN
        elif left < right:
            return ComparisonResult.VALID
        else:
            return ComparisonResult.INVALID

    # Exactly one value is an int
    if (type(left) == int) ^ (type(right) == int):
        print(f'Exactly one is an int')
        if type(left) == int:
            return _compare([left], right)
        else:
            return _compare(left, [right])

    assert type(left) == list and type(right) == list


    print(f'Comparing lists {left} and {right}')

    for idx in range(min(len(left), len(right))):

        print(f'Comparing {left[idx]} and {right[idx]}')
        res = _compare(left[idx], right[idx])

        # One invalid -> all invalid
        if res == ComparisonResult.INVALID:
            print(f'List comparison invalid (at {idx})')
            return ComparisonResult.INVALID

        if res == ComparisonResult.VALID:
            print(f'List comparison valid (at {idx})')
            return ComparisonResult.VALID

    print(f'Comparing lengths {len(left)} and {len(right)}')

    # Same length -> unknown
    if len(left) == len(right):
        return ComparisonResult.UNKNOWN

    return ComparisonResult.VALID if len(left) <= len(right) else ComparisonResult.INVALID


def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    res1: int = 0

    all_packets = []

    with open(input_file, 'r') as f:

        for idx, (p1, p2) in enumerate([comb.split('\n') for comb in f.read().strip().split('\n\n')]):

            l1 = eval(p1)
            l2 = eval(p2)

            all_packets += [l1, l2]

            print(f'\n\n== Pair {idx + 1} ==')
            res = compare(l1, l2)
            print(f'Valid: {res}')

            if res:
                res1 += idx + 1

    # Adding divider packets for task 2
    div_packets = [[[2]], [[6]]]
    all_packets += div_packets

    all_packets.sort(key=cmp_to_key(_cmp_packet))


    print('\n'.join([str(l) for l in all_packets]))
    res2 = (all_packets.index(div_packets[0]) + 1) * (all_packets.index(div_packets[1]) + 1)

    return res1, res2

def _cmp_packet(p1, p2) -> int:

    if p1 == p2:
        return 0

    res = compare(p1, p2)
    return -1 if res else 1


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day13/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')

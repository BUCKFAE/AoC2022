from __future__ import annotations

import os
import re
from dataclasses import dataclass


@dataclass
class Instruction:
    amount: int
    start: int
    end: int

@dataclass
class Stack:
    elements: list[str]

def solve(input_file: str)-> tuple[str, str]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    instructions: list[Instruction] = []
    stacks: list[Stack] = []

    with open(input_file, 'r') as f:

        file_text = f.read().splitlines()

        # Splitting document into stacks / instructions
        assert sum([1 if not line.strip() else 0 for line in file_text]) == 1
        divider = file_text.index('')
        print(f'Divider at {divider}')
        stack_lines = file_text[:divider - 1]
        instruction_lines = file_text[divider + 1:]

        # Getting number of stacks
        num_stacks = len(re.sub(r'\s+', '', file_text[divider - 1]))
        print(f'Number of stacks: {num_stacks}')

        stacks: list[Stack] = [Stack([]) for _ in range(num_stacks)]

        # Parsing stacks
        for stack_line in stack_lines:
            # Padding line to use step 4
            stack_line_pad = stack_line.ljust(num_stacks * 4)
            for idx in range(1, num_stacks * 4, 4):
                e = stack_line_pad[idx]
                if e.strip():
                    stacks[idx // 4].elements = [e] + stacks[idx // 4].elements

        # Parsing instructions
        for instruction_line in instruction_lines:
            line = re.sub(r'[^0-9]+', ' ' , instruction_line)
            line = re.sub(r'\s+', ' ', line).strip()
            amount, start, end = line.split(' ')
            instructions.append(Instruction(int(amount), int(start) - 1, int(end) - 1))

    stacks_2 = [Stack([e for e in s.elements]) for s in stacks]

    # Applying instructions
    for instruction in instructions:
        # Task 1
        s1 = stacks[instruction.start]
        crates1 = [s1.elements.pop() for _ in range(instruction.amount)]
        stacks[instruction.end].elements.extend(crates1)

        # Task 2
        s2 = stacks_2[instruction.start]
        crates2 = s2.elements[-instruction.amount:]
        del s2.elements[-instruction.amount:]
        stacks_2[instruction.end].elements.extend(crates2)

    res1 = ''.join([s.elements[-1] for s in stacks])
    res2 = ''.join([s.elements[-1] for s in stacks_2])

    return res1, res2


if __name__ == '__main__':
    res_sample = solve('day05/sample_input.txt')
    assert res_sample[0] == 'CMZ', f'Expected CMZ, got {res_sample[0]}'
    assert res_sample[1] == 'MCD', f'Expected MCD, got {res_sample[1]}'

    res = solve('day05/input.txt')
    print(f'Part 1: {res[0]} - Part 2: {res[1]}')

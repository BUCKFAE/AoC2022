from __future__ import annotations

import os


def solve(input_file: str)-> tuple[int, str]:
    """

    Values at steps: 20th, 60th, 100th, 140th, 180th, and 220th
    """

    time_steps = [20, 60, 100, 140, 180, 220]
    cycle_values = simulate_cycles(input_file)

    res1 = sum([cycle_values[time_step] for time_step in time_steps])

    # Task 2 - Drawing
    res2: str = ''
    for cycle, value in cycle_values.items():

        crt_pos = (cycle - 1) % 40
        sprite_pos = value // cycle

        # Adding new line
        if crt_pos % 40 == 0 and cycle > 1:
            res2 += '\n'

        if abs(sprite_pos - crt_pos) <= 1:
            res2 += '#'
        else:
            res2 += '.'



    return res1, res2.strip()


def simulate_cycles(input_file: str)-> dict[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'


    x = 1
    cycle_id = 1
    cycle_values: dict[int, int] = {1: 1}

    with open(input_file, 'r') as f:

        commands = [line.strip() for line in f.read().splitlines() if line.strip()]

        for command_id in range(len(commands)):

            command = commands[command_id]

            if command == 'noop':
                cycle_values[cycle_id] = x
                cycle_id += 1
            elif command.startswith('addx'):
                cycle_values[cycle_id] = x
                cycle_values[cycle_id + 1] = x
                cycle_id += 2
                x += int(command.split(' ')[1])

    return {k: v * k for k, v in cycle_values.items()}


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day10/input.txt')
    print(f'Part 1: {res1} - Part 2:\n{res2}')

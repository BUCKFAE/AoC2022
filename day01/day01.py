from __future__ import annotations

def solve(input_file: str) -> tuple[int, int]:

    with open(input_file) as f:
        data = f.read().splitlines()

    elves: list[int] = []
    current_elv_calories = 0

    for idx, line in enumerate(data):
        if line:
            current_elv_calories += int(line)
        else:
            elves.append(current_elv_calories)
            current_elv_calories = 0

    res1 = max(elves)

    res2 = sum(sorted(elves, reverse=True)[:3])

    return res1, res2

if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day01/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')

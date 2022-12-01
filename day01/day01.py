from __future__ import annotations

with open('day01/input.txt') as f:
    data = f.read().splitlines()

elves: list[int] = []
current_elv_calories = 0

for idx, line in enumerate(data):
    if line:
        current_elv_calories += int(line)
    else:
        elves.append(current_elv_calories)
        current_elv_calories = 0

max_elv = max(elves)
print(f'Calories top elv: {max_elv}')

max_three = sum(sorted(elves, reverse=True)[:3])
print(f'Calories top three: {max_three}')

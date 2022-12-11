from __future__ import annotations

import os
import re
from dataclasses import dataclass

import numpy as np


@dataclass
class Monkey:
    monkey_id: int
    items: list[dict[int, int]]
    operation: str
    divider: int
    throw_true: int
    throw_false: int
    items_inspected: int = 0

    def __str__(self) -> str:
        return f'Monkey ({self.monkey_id}):\n\t' \
                f'Items: {self.items}\n\t' \
                f'Operation: {self.operation}\n\t' \
                f'Divider: {self.divider}\n\t' \
                f'Throw True: {self.throw_true}\n\t' \
                f'Throw False: {self.throw_false}'



def solve(input_file: str, task_id: int)-> int:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    monkeys: dict[int, Monkey] = {}

    with open(input_file, 'r') as f:

        for monkey_block in f.read().split('\n\n'):
            monkey_lines = [line.strip() for line in monkey_block.split('\n')]

            monkey_id = int(monkey_lines[0].split(' ')[1].removesuffix(':'))
            items = [int(item.strip()) for item in monkey_lines[1].split(':')[1].strip().split(',')]
            op = monkey_lines[2].split(':')[1].strip().split('=')[1].strip()
            divider = int(re.sub(r"[^0-9]", "", monkey_lines[3]).strip())
            throw_true = int(re.sub(r"[^0-9]", "", monkey_lines[4]).strip())
            throw_false = int(re.sub(r"[^0-9]", "", monkey_lines[5]).strip())
            items_mod = [{1: item} for item in items]

            new_monkey = Monkey(monkey_id, items_mod, op, divider, throw_true, throw_false)
            monkeys[monkey_id] = new_monkey

    return task_1(monkeys) if task_id == 1 else task_2(monkeys)

def task_1(monkeys: dict[int, Monkey]) -> int:

    for _ in range(20):

        for monkey_id in monkeys.keys():
            monkey = monkeys[monkey_id]

            for item_dict in monkey.items:
                item = item_dict[1]
                calc = monkey.operation.replace('old', str(item))
                new_worry_level = eval(calc) // 3

                monkey.items_inspected += 1

                if new_worry_level % monkey.divider == 0:
                    monkeys[monkey.throw_true].items.append({1: new_worry_level})
                else:
                    monkeys[monkey.throw_false].items.append({1: new_worry_level})

            monkey.items = []

    monkeys_active = sorted(monkeys.values(), key=lambda x: x.items_inspected, reverse=True)
    res1 = int(np.prod([monkey.items_inspected for monkey in monkeys_active[:2]]))

    return res1

def task_2(monkeys: dict[int, Monkey]) -> int:

    # Storing for each item the remainder in each div
    divs = [monkey.divider for monkey in monkeys.values()]
    for monkey in monkeys.values():
        item_list = []
        for item in monkey.items:
            item_dict = {}
            for div in divs:
                item_dict[div] = item[1] % div
            item_list.append(item_dict)
        monkey.items = item_list
        print(monkey)


    for _ in range(10000):

        for monkey_id in monkeys.keys():
            monkey = monkeys[monkey_id]

            for item_map in monkey.items:

                new_item_map = {}
                for key, value in item_map.items():
                    calc = monkey.operation.replace('old', str(value))

                    new_worry_level = eval(calc)
                    new_worry_level = new_worry_level % key
                    new_item_map[key] = new_worry_level

                monkey.items_inspected += 1

                if new_item_map[monkey.divider] == 0:
                    monkeys[monkey.throw_true].items.append(new_item_map)
                else:
                    monkeys[monkey.throw_false].items.append(new_item_map)

            monkey.items = []

    monkeys_active = sorted(monkeys.values(), key=lambda x: x.items_inspected, reverse=True)
    res = int(np.prod([monkey.items_inspected for monkey in monkeys_active[:2]]))

    return res


if __name__ == '__main__':

    # Solving real input
    res1 =  solve('day11/input.txt', 1)
    res2 =  solve('day11/input.txt', 2)
    print(f'Part 1: {res1} - Part 2: {res2}')

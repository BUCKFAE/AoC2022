from __future__ import annotations

import os


def are_adjacent(a: tuple[int, int], b: tuple[int, int])-> bool:
    """Checks if the two points are adjacent to each other
    - Left / Right
    - Diagonal
    - Overlap
    """
    if a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True
    elif a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True
    elif abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1:
        return True
    elif a[0] == b[0] and a[1] == b[1]:
        return True
    return False

def solve(input_file: str, rope_length: int)-> int:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    instructions: list[tuple[str, int]] = []

    with open(input_file, 'r') as f:
        for line in [line.strip() for line in f.read().splitlines() if line.strip()]:
            a, b = line.split(' ')
            instructions.append((a, int(b)))

    visited: list[tuple[int, int]] = []

    rope_elements : list[tuple[int, int]]= [(0, 0) for _ in range(rope_length)]
    print(f'Rope elements: {rope_elements}')

    for dir, steps in instructions:
        for _ in range(steps):

            pos_head = rope_elements[0]

            # Moving the head of the rope
            if dir == 'R':
                pos_head = (pos_head[0] + 1, pos_head[1])
            elif dir == 'L':
                pos_head = (pos_head[0] - 1, pos_head[1])
            elif dir == 'U':
                pos_head = (pos_head[0], pos_head[1] + 1)
            elif dir == 'D':
                pos_head = (pos_head[0], pos_head[1] - 1)

            rope_elements[0] = pos_head

            for current_rope_part in range(len(rope_elements) - 1):
                pos_head = rope_elements[current_rope_part]
                pos_tail = rope_elements[current_rope_part + 1]

                if not are_adjacent(pos_head, pos_tail):

                    # Moving closer if not diagonal
                    if pos_head[0] == pos_tail[0] or pos_head[1] == pos_tail[1]:
                        # Straight move
                        if pos_head[0] > pos_tail[0]:
                            pos_tail = (pos_tail[0] + 1, pos_tail[1])
                        elif pos_head[0] < pos_tail[0]:
                            pos_tail = (pos_tail[0] - 1, pos_tail[1])
                        elif pos_head[1] > pos_tail[1]:
                            pos_tail = (pos_tail[0], pos_tail[1] + 1)
                        elif pos_head[1] < pos_tail[1]:
                            pos_tail = (pos_tail[0], pos_tail[1] - 1)
                    else:
                        # Diagonal move
                        if pos_head[0] > pos_tail[0] and pos_head[1] > pos_tail[1]:
                            pos_tail = (pos_tail[0] + 1, pos_tail[1] + 1)
                        elif pos_head[0] < pos_tail[0] and pos_head[1] > pos_tail[1]:
                            pos_tail = (pos_tail[0] - 1, pos_tail[1] + 1)
                        elif pos_head[0] > pos_tail[0] and pos_head[1] < pos_tail[1]:
                            pos_tail = (pos_tail[0] + 1, pos_tail[1] - 1)
                        elif pos_head[0] < pos_tail[0] and pos_head[1] < pos_tail[1]:
                            pos_tail = (pos_tail[0] - 1, pos_tail[1] - 1)

                    rope_elements[current_rope_part + 1] = pos_tail

                    assert are_adjacent(pos_head, pos_tail), f'Head {pos_head} and Tail {pos_tail} are not adjacent'

                # Tail has visited the current position
                if current_rope_part == len(rope_elements) - 2:
                    if pos_tail not in visited:
                        visited.append(pos_tail)

    return len(visited)


if __name__ == '__main__':

    # Solving real input
    res1 = solve('day09/input.txt', rope_length=2)
    print(f'Part 1: {res1}')

    res2 = solve('day09/input.txt', rope_length=10)
    print(f'Part 2: {res2}')

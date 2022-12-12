from __future__ import annotations

import os
import dataclasses

@dataclasses.dataclass
class Node:
    pos: tuple[int, int]
    height: str
    neighbors: list[tuple[int, int]]
    distance: float = float('inf')
    prev: Node | None = None

def dijkstra(graph: dict[tuple[int, int], Node], pos_start: tuple[int, int], pos_tgt: tuple[int, int]):

    print(f'Executing Dijkstra from ({pos_start})')
    print(f'Target: ({pos_tgt})')

    q = [n for n in graph.keys()]

    graph[pos_start].distance = 0

    while q:
        q.sort(key=lambda n: graph[n].distance)

        pos_u = q.pop(0)
        u = graph[pos_u]

        # Found the correct node
        if u.pos == pos_tgt:
            break

        for n_pos in [n for n in u.neighbors if n in q]:
            v = graph[n_pos]

            alt = u.distance + 1
            if alt < v.distance:
                v.distance = alt
                v.prev = u

def solve(input_file: str)-> tuple[int, int]:

    assert os.path.exists(input_file), f'File {input_file} does not exist'

    graph: dict[tuple[int, int], Node] = {}

    start_pos = (-1, -1)
    tgt_pos = (-1, -1)

    with open(input_file, 'r') as f:

        lines = [line.strip() for line in f.read().splitlines() if line.strip()]

        size_x = len(lines[0])
        size_y = len(lines)

        print(f'Input size: {size_x}x{size_y}')


        for pos_y, line in enumerate(lines):

            for pos_x, height in enumerate(line):

                neighbors: list[tuple[int, int]] = []

                dirs: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                # Get all neighbors
                for dir in dirs:
                    new_pos = (pos_x + dir[0], pos_y + dir[1])
                    if 0 <= new_pos[0] < size_x and 0 <= new_pos[1] < size_y:
                        neighbors.append(new_pos)

                # Start
                if height == 'S':
                    height = 'a'
                    start_pos = (pos_x, pos_y)
                # Target
                if height == 'E':
                    height = 'z'
                    tgt_pos = (pos_x, pos_y)

                graph[(pos_x, pos_y)] = Node((pos_x, pos_y), height, neighbors)

    graph_copy = {pos: dataclasses.replace(n) for pos, n in graph.items()}

    # Remove all neighbors we can't reach
    for node_pos in graph.keys():

        node = graph[node_pos]

        own_height= ord(node.height)
        new_neighbors_t1 = []
        new_neighbors_t2= []

        for neighbor in node.neighbors:
            neighbor_height = ord(graph[neighbor].height)

            # Step from that node to neighbor (Task 1)
            if neighbor_height - own_height <= 1:
                new_neighbors_t1.append((neighbor[0], neighbor[1]))

            # Step to that node from neighbor (Task 2)
            if own_height - neighbor_height <= 1:
                new_neighbors_t2.append((neighbor[0], neighbor[1]))

        graph[node_pos].neighbors = new_neighbors_t1
        graph_copy[node_pos].neighbors = new_neighbors_t2


    # Find route from start to end
    dijkstra(graph, start_pos, tgt_pos)


    # Find route from end to all nodes (especially to all with height 'a')
    dijkstra(graph_copy, tgt_pos, (-1, -1))

    res1 = int(graph[tgt_pos].distance)
    res2 = int(min([n.distance for n in graph_copy.values() if n.height == 'a']))

    return res1, res2


if __name__ == '__main__':

    # Solving real input
    res1, res2 = solve('day12/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')

from __future__ import annotations


def solve(input_file: str)-> tuple[int, int]:

    with open(input_file, 'r') as f:
        data = f.read().splitlines()

    enemy_moves, own_moves = zip(*[d.split(' ') for d in data])

    score = 0

    rewards = {'loss': 0 , 'draw': 3 , 'win': 6 }

    for own_move, enemy_move in zip(own_moves, enemy_moves):

        if own_move == 'X': # Rock
            score += 1 # 1 for Rock
            if enemy_move == 'A': # Rock
                score += rewards['draw']
            elif enemy_move == 'B': # Paper
                score += rewards['loss']
            elif enemy_move == 'C': # Scissors
                score += rewards['win']
        elif own_move == 'Y': # Paper
            score += 2 # 2 for Paper
            if enemy_move == 'A': # Rock
                score += rewards['win']
            elif enemy_move == 'B': # Paper
                score += rewards['draw']
            elif enemy_move == 'C': # Scissors
                score += rewards['loss']
        elif own_move == 'Z': # Scissors
            score += 3 # 3 for Scissors
            if enemy_move == 'A': # Rock
                score += rewards['loss']
            elif enemy_move == 'B': # Paper
                score += rewards['win']
            elif enemy_move == 'C': # Scissors
                score += rewards['draw']

    res1 = score

    # Now second column is the desired result
    score = 0
    for result, enemy_move in zip(own_moves, enemy_moves):
        if enemy_move == 'A': # Rock
            if result == 'X': # Loose
                score += rewards['loss']
                score += 3 # 3 for Scissors
            elif result == 'Y': # Draw
                score += rewards['draw']
                score += 1 # 1 for Rock
            elif result == 'Z': # Win
                score += rewards['win']
                score += 2 # 2 for Paper
        elif enemy_move == 'B': # Paper
            if result == 'X': # Loose
                score += rewards['loss']
                score += 1 # 1 for Rock
            elif result == 'Y': # Draw
                score += rewards['draw']
                score += 2 # 2 for Paper
            elif result == 'Z': # Win
                score += rewards['win']
                score += 3 # 3 for Scissors
        elif enemy_move == 'C': # Scissors
            if result == 'X': # Loose
                score += rewards['loss']
                score += 2 # 2 for Paper
            elif result == 'Y': # Draw
                score += rewards['draw']
                score += 3 # 3 for Scissors
            elif result == 'Z': # Win
                score += rewards['win']
                score += 1 # 1 for Rock
    res2 = score
    return res1, res2

if __name__ == '__main__':
    # Solving real input
    res1, res2 = solve('day02/input.txt')
    print(f'Part 1: {res1} - Part 2: {res2}')

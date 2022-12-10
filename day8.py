# day 8

import numpy as np
from itertools import permutations

def compute_paths(n):
    pass

def load_grid():
    with open('data/day8.txt') as f:
        return np.array([list(map(int, list(line.rstrip())))
            for line in f.readlines()], dtype=int)

def east_west(n):
    for r in range(1, n-1):
        yield [[r, c] for c in range(0, n-1)]
        yield [[r, c] for c in range(n-1, 0, -1)]

def north_south(n):
    for c in range(1, n-1):
        yield [[r, c] for r in range(0, n-1)]
        yield [[r, c] for r in range(n-1, 0, -1)] 

def analyze_grid():
    grid = load_grid()
    n, _ = grid.shape
    seen = np.zeros((n, n), dtype=int)

    for direction in [east_west(n), north_south(n)]:
        for paths in direction:
            peak = -1
            for r, c in paths:
                if grid[r,c] > peak:
                    seen[r,c] = 1
                    peak = grid[r,c]

    # Add 4 corners
    seen[0,0] = seen[0, n-1] = seen[n-1, 0] = seen[n-1, n-1] = 1

    return dict(grid=grid, visible=seen)
    

def scenic_score(from_r: int, from_c: int, grid, n: int) -> int:
    height = grid[from_r, from_c]

    look_up = 0
    for r in range(from_r-1, -1, -1):
        look_up += 1
        if grid[r, from_c] >= height:
            break
   
    look_left = 0
    for c in range(from_c-1, -1, -1):
        look_left += 1
        if grid[from_r, c] >= height:
            break

    look_right = 0
    for c in range(from_c+1, n):
        look_right += 1
        if grid[from_r, c] >= height:
            break

    look_down = 0
    for r in range(from_r+1, n):
        look_down += 1
        if grid[r, from_c] >= height:
            break

    score = look_right * look_left * look_up * look_down
    # print(f"Scenic score for [{from_r},{from_c}] is {look_up} * {look_left} * {look_right} * {look_down} = {score}")
    return score

def most_scenic(results):
    grid, visible = results['grid'], results['visible']
    n, _ = grid.shape
    return max([scenic_score(*p, grid, n) for p in permutations(range(1, n), 2) if visible[*p]])

if __name__ == '__main__':
    results = analyze_grid()

    print(f"Part 1 is {np.sum(results['visible'])}")
    print(f"Part 2 is {most_scenic(results)}")
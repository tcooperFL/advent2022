# day 8

import numpy as np

def compute_paths(n):
    pass

def build_grid():
    with open('data/day8.txt') as f:
        return np.array([list(map(int, list(line.rstrip())))
            for line in f.readlines()], dtype=int)

def east(n):
    for r in range(1, n-1):
        yield [[r, c] for c in range(0, n-1)]

def west(n):
    for r in range(1, n-1):
        yield [[r, c] for c in range(n-1, 0, -1)]

def north(n):
    for c in range(1, n-1):
        yield [[r, c] for r in range(0, n-1)]

def south(n):
    for c in range(1, n-1):
        yield [[r, c] for r in range(n-1, 0, -1)] 

def solve():
    grid = build_grid()
    n, _ = grid.shape
    seen = np.zeros((n, n), dtype=int)

    for direction in [east(n), west(n), north(n), south(n)]:
        for paths in direction:
            peak = -1
            for r, c in paths:
                if grid[r,c] > peak:
                    seen[r,c] = 1
                    peak = grid[r,c]

    # Add 4 corners
    return(np.sum(seen) + 4)

if __name__ == '__main__':
    print(f"Part 1 is {solve()}")

# day 8

import numpy as np
from itertools import chain
from pprint import pprint

def compute_paths(n):
    pass

def build_grid():
    with open('data/sample.txt') as f:
        return np.array([list(map(int, list(line.rstrip())))
            for line in f.readlines()], dtype=int)

def build_visibles(n):
    v = np.zeros((n, n), dtype=int)
    for i in range(n):
        v[i, 0] = v[i, n-1] = v[0, i] = v[n-1, i] = 1
    return v

def taller(h, lst):
    print(f"Is {h} greater than all of {lst}?")
    result = all(map(lambda x: h > x, lst))
    print(result)
    return result

def visible(grid, r, c):
    height = grid[r,c]
    # east, west, north, south
    taller(height, grid[r,c+1:]) \
        or taller(height, grid[r,:c-1]) \
        or taller(height, grid[:r-1,c]) \
        or taller(height, grid[r+1:,c])

def solve():
    grid = build_grid()
    n, _ = grid.shape
    seen = build_visibles(n)
    peek_over = lambda p1, p2: grid[*p1] < grid[*p2]

    # Look in from every direction
    for r, c in [[r, c] for r in range(1, n-2) for c in range(1, n-2)]:
        if not seen[r, c] and visible(grid, r, c):
            seen[r, c] = 1

    pprint(grid)
    pprint(seen)
    print(np.sum(seen))

if __name__ == '__main__':
    print(f"Part 1 is {solve()}")

   #  pprint(list(south(5)))

    # 5219 is too high
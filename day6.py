# day 6
from collections import deque

def solve(n):
    with open('data/day6.txt', 'r') as f:
        data = f.read()

    buffer = deque(maxlen=n)
    for i in range(len(data)):
        buffer.append(data[i])
        if len(set(buffer)) == n:
            return i + 1


if __name__ == "__main__":
    print(f"Part 1: {solve(4)}")
    print(f"Part 2: {solve(14)}")

# day 5
from collections import defaultdict
from pprint import pprint

def add_layer(stacks, line):
    if '[' in line:
        for i in range(len(line)):
            if line[i] == '[':
                row = (i // 4) + 1
                stacks[row].append(line[i + 1])

def move(stacks, num, from_stack, to_stack, xf):
    stack = stacks[from_stack]
    to_move = xf(stack[:num])
    stacks[from_stack] = stack[num:]
    stacks[to_stack] = to_move + stacks[to_stack]

def get_message(stacks):
    return ''.join([stacks[i][0] for i in range(1, len(stacks) + 1)])

def solve(xf):
    stacks = defaultdict(list)

    with open('data/day5.txt', 'r') as f:
        # Build the stacks
        while line := f.readline().rstrip():
            add_layer(stacks, line)

        # Make the moves
        while line := f.readline():
            _, num, _, from_stack, _, to_stack = line.split()
            move(stacks, int(num), int(from_stack), int(to_stack), xf)

    return get_message(stacks)


if __name__ == "__main__":
    print(f"Part 1: {solve(lambda x: list(reversed(x)))}")
    print(f"Part 2: {solve(lambda x: x)}")

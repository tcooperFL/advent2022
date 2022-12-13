# day 11 part 1
from pprint import pprint
from collections import deque
import operator
import re
import math

number_pattern = re.compile(r'\d+')

def find_number(s):
    return int(number_pattern.search(s).group())

def parse_items(f):
    line = f.readline()
    return deque(map(int, number_pattern.findall(line)))

def parse_operation(f):
    line = f.readline().rstrip().split()
    match line:
        case ['Operation:', 'new', '=', _, op, arg2]:
            fn = operator.add if op == '+' else operator.mul
            if arg2 == 'old':
                return lambda item: fn(item, item)
            else:
                arg = int(arg2)
            return lambda item: fn(item, arg)
        case _:
            raise Exception(f"Unrecognized operation: {line}")

def parse_test(f):
    divisor = find_number(f.readline())
    m1 = find_number(f.readline())
    m2 = find_number(f.readline())
    return lambda item: m1 if (item % divisor) == 0 else m2

def load_monkeys(boredom=lambda x: x):
    monkeys = []
    with open('data/day11.txt', 'r') as f:
        count = 0
        while line := f.readline().strip():
            if line.startswith('Monkey'):
                monkey = dict(
                    number=count,
                    inspections=0,
                    items=parse_items(f),
                    boredom_fn=boredom,
                    adjust_fn=parse_operation(f),
                    throw_to_fn=parse_test(f))
                monkeys.append(monkey)
                f.readline()
            count += 1
    return monkeys

def boredom_adjust(inspected):
    return math.floor(inspected / 3)

def take_turn(m, monkeys):
    while m['items']:
        item = m['items'].popleft()
        inspected = m['adjust_fn'](item)
        m['inspections'] += 1
        worry = m['boredom_fn'](inspected)
        throw_to = m['throw_to_fn'](worry)
        next_monkey = monkeys[throw_to]
        next_monkey['items'].append(worry)
        # print(f"Monkey {m['number']}:")
        # print(f"  Monkey inspects an item with a worry level of {item}.")
        # print(f"  Worry level adjusted to {inspected}.")
        # print(f"  Monkey gets bored with item. Worry level is divided by 3 to {worry}.")
        # print(f"  Item is thrown to monkey {throw_to}.")

def round(monkeys):
    for m in monkeys:
        take_turn(m, monkeys)

def part1():
    monkeys = load_monkeys(boredom=lambda x: math.floor(x / 3))
    for _ in range(20):
        round(monkeys)

    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]


if __name__ == '__main__':

    print(f"Part 1: {part1()}")
    # 99840
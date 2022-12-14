# day 11 part 1
from pprint import pprint
import operator
import re
import math

number_pattern = re.compile(r'\d+')

def find_number(s):
    return int(number_pattern.search(s).group())

def parse_items(f):
    line = f.readline()
    return list(map(int, number_pattern.findall(line)))

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

def load_monkeys():
    monkeys = []
    with open('data/day11.txt', 'r') as f:
        count = 0
        while line := f.readline().strip():
            if line.startswith('Monkey'):
                monkey = dict(
                    number=count,
                    inspections=0,
                    items=parse_items(f),
                    adjust_fn=parse_operation(f),
                    throw_to_fn=parse_test(f))
                monkeys.append(monkey)
                f.readline()
            count += 1
    return monkeys

def take_turn(m, monkeys):
    m['inspections'] += len(m['items'])
    for item in m['items']:
        inspected = m['adjust_fn'](item)
        worry = math.floor(inspected / 3)
        throw_to = m['throw_to_fn'](worry)
        next_monkey = monkeys[throw_to]
        next_monkey['items'].append(worry)
    m['items'].clear()

def round(monkeys):
    for m in monkeys:
        take_turn(m, monkeys)

def part1():
    monkeys = load_monkeys()
    for _ in range(20):
        round(monkeys)

    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    # 99840
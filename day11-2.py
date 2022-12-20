# day 11 part 2
from pprint import pprint
import operator
import re
from functools import reduce

number_pattern = re.compile(r'\d+')
factors = set()
cap = 1

def find_number(s):
    return int(number_pattern.search(s).group())

def parse_items(f):
    line = f.readline()
    return list(map(int, number_pattern.findall(line)))

def parse_operation(f):
    line = f.readline().rstrip().split()
    match line:
        case ['Operation:', 'new', '=', 'old', op, arg2]:
            fn = operator.add if op == '+' else operator.mul
            if arg2 == 'old':
                return lambda item: fn(item, item)
            else:
                arg = int(arg2)

            return lambda item: fn(item, arg)

        case _:
            raise Exception(f"Unrecognized operation: {line}")

def parse_test(f):
    global factors
    divisor = find_number(f.readline())
    factors.add(divisor)
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
        inspected = m['adjust_fn'](item) % cap
        throw_to = m['throw_to_fn'](inspected)
        monkeys[throw_to]['items'].append(inspected)
    m['items'] = []

def round(monkeys):
    for m in monkeys:
        take_turn(m, monkeys)

def part2():
    global cap
    monkeys = load_monkeys()
    cap = reduce(operator.mul, factors)
    for _ in range(10000):
        round(monkeys)

    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]


if __name__ == '__main__':
    print(f"Part 2: {part2()}")
    # 20683044837 is my answer

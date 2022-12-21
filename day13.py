# day 13

from itertools import count, zip_longest
from first import first
from functools import cmp_to_key

INPUT = 'data/day13.txt'

class Ordered(Exception):
    def __init__(self, answer):
        self.answer = answer
        super().__init__()

def read_packet_pairs():
    with open(INPUT, 'r') as f:
        for i in count(1):
            yield (i, eval(f.readline()), eval(f.readline()))
            if not f.readline():
                break

def in_order(numbered_pair):
    # Assume ordered unless you find an explicit result
    is_ordered = True
    try:
        verify_order(numbered_pair[1], numbered_pair[2])
    except Ordered as r:
        is_ordered = r.answer
    return is_ordered

def verify_order(left_packet, right_packet):
    """Walk the pairs and throw the result if you find a definitive True/False"""
    for left, right in zip_longest(left_packet, right_packet):
        if isinstance(left, int) and isinstance(right, int):
            if left != right:
                raise Ordered(left < right)
        elif isinstance(left, list) and isinstance(right, list):
            verify_order(left, right)

        elif left is None:
            raise Ordered(True)
        elif right is None:
            raise Ordered(False)
         
        elif isinstance(left, int):
            verify_order([left,], right)
        else:
            verify_order(left, [right,])

def part1():
    return sum(map(first, filter(in_order, read_packet_pairs())))

####

def read_all_packets():
    with open(INPUT, 'r') as f:
        yield [[2]]
        yield [[6]]
        for line in f.readlines():
            if line.strip():
                yield eval(line)

def order_cmp(x, y):
    # Assume ordered unless you find an explicit result
    ordering = 0
    try:
        verify_order(x, y)
    except Ordered as r:
        ordering = -1 if r.answer else 1
    return ordering

def part2():
    ordered = sorted(read_all_packets(), key=cmp_to_key(order_cmp))
    decoder_key = (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)
    return decoder_key

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

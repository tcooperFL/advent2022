# day 15 part 1

import re
from collections import namedtuple
from codetiming import Timer

INPUT = 'data/day15.txt'
TARGET_ROW = 2000000

number_pattern = re.compile(r'-?\d+')
Point = namedtuple('Point', ['x', 'y'])

def parse_locations(line):
    sx, sy, bx, by = list(map(int, number_pattern.findall(line)))
    return Point(sx, sy), Point(bx, by)

def load_sensors():
    """Return a list of point pairs: (sensor_x, xsensor_y), (beacon_x, beacon_y)"""
    with open(INPUT, 'r') as f:
        return list(map(parse_locations, f.readlines()))

def part1():
    data = load_sensors()
    occupied = set([p for pair in data for p in pair])
    empty = set()

    with Timer(text="Search time: {:0.4f} seconds"):
        for s, b in data:
            mdist = abs(s.y - b.y) + abs(s.x - b.x)
            distance_to_line = abs(TARGET_ROW - s.y)
            span = mdist - distance_to_line
            if span >= 0:
                for x in range(s.x - span, s.x + span + 1):
                    p = Point(x, TARGET_ROW)
                    if p not in occupied:
                        empty.add(p)

    return len(empty)

if __name__ == '__main__':
    print(f"Part 1: {part1()}")

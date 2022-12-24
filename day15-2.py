# day 15 part 2
# NOT SOLVED YET.
# Works for sample data, but not for provided iput.

import re
from collections import namedtuple
from pprint import pprint

INPUT = 'data/day15.txt'    # sample.txt
MAX_COORD = 4000000         # 20

number_pattern = re.compile(r'\d+')
Point = namedtuple('Point', ['x', 'y'])

def parse_locations(line):
    sx, sy, bx, by = list(map(int, number_pattern.findall(line)))
    return Point(sx, sy), Point(bx, by)

def load_sensors():
    """Return a list of point pairs: (sensor_x, xsensor_y), (beacon_x, beacon_y)"""
    with open(INPUT, 'r') as f:
        return list(map(parse_locations, f.readlines()))

def mdist(p1, p2):
    return abs(p2.y - p1.y) + abs(p2.x - p1.x)

def create_span(x, dx):
    """Return the x span, inclusive"""
    return (x - dx, x + dx)

def find_spans(y, areas):
    # Create a list of intersected x-spans sorted by span start
    x_spans = []
    trimmed = set()
    for (p, dist) in areas:
        # print(f"Considering sensor {p} with radius {dist}")
        # If sensor is above this line
        if p.y <= y:
            # If the range extends down to this line, compute covered x-span
            if p.y + dist >= y:
                dx = (p.y + dist) - y
                x_spans.append(create_span(p.x, dx))
            else:
                # Else plan to trim this area from subsequent line scans
                trimmed.add((p, dist))

        # Else sensor is below.
        elif p.y - dist <= y:
            dx = y - (p.y - dist)
            x_spans.append(create_span(p.x, dx))
    
    # Remove areas that can no longer cover below
    for a in trimmed:
        # print(f"Can trim out sensor {a} since no longer covers row {y} or below")
        areas.remove(a)

    # Return spans sorted by start of span.
    return sorted(x_spans, key=lambda x: x[0])

def part2():
    data = sorted(load_sensors(), key=lambda x: x[0])
    occupied = set([p for pair in data for p in pair])
    areas = [(s, mdist(s, b)) for s, b in data]

    # print(f"Areas: {len(areas)}")
    # for p, d in sorted(areas, key=lambda x: x[0].x - x[1]):
    #     print(f"Sensor {p,d} extends up to {(p.x - d,p.y - d)}")

    for y in range(MAX_COORD):
        # print(f"\nSearching row {y}")
        x = 0
        for x1, x2 in find_spans(y, areas):
            # print(f"At {x,y} first x-span at {y} is {x1, x2}")
            if (x < x1) and Point(x, y) not in occupied:
                return Point(x, y)
            else:
                x = max(x, x2 + 1)
                # print(f"   x = {x}")

        if x < MAX_COORD and Point(x, y) not in occupied:
            return Point(x, y)


if __name__ == '__main__':
    p = part2()
    print(f"Part 2: at {p} tuning frequency is {(p.x * 4000000) + p.y}")

    # Point(x=1022932, y=57951), 4,091,728,057,951 is too low
    # Point(x=1022933, y=57951), 4,091,736,057,951 is also "not right"
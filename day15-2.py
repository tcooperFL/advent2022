# day 15 part 2

import re
from itertools import product

INPUT = 'data/day15.txt'    # sample.txt
MAX_COORD = 4_000_000         # 20

number_pattern = re.compile(r'-?\d+')


def parse_locations(line):
    """Return tuple: sensor location and mdistance to nearest beacon"""
    sx, sy, bx, by = list(map(int, number_pattern.findall(line)))
    return (sx, sy), mdist((sx, sy), (bx, by))


def load_sensors():
    """Return a list of point pairs: (sensor_x, xsensor_y), (beacon_x, beacon_y)"""
    with open(INPUT, 'r') as f:
        return list(map(parse_locations, f.readlines()))


def mdist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def outlines(s, d):
    dist = d + 1
    sx, sy = s

    top, bottom = (sx, sy-dist), (sx, sy+dist)
    left, right = (sx-dist, sy), (sx+dist, sy)

    return ((top, left), (right, bottom)), ((top, right), (left, bottom))


def collect_lines(data):
    left_lines = []
    right_lines = []
    for p, d in data:
        left, right = outlines(p, d)
        left_lines.extend(left)
        right_lines.extend(right)
    return left_lines, right_lines


def line_intersection(line1, line2):
    """From https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines"""
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) // div
    y = det(d, ydiff) // div
    return x, y


def part2():
    data = load_sensors()
    left_lines, right_lines = collect_lines(data)

    for left, right in product(left_lines, right_lines):
        x, y = line_intersection(left, right)

        if not ((0 < x < MAX_COORD) and (0 < y < MAX_COORD)):
            continue

        if all(mdist((x, y), p) > d for p, d in data):
            print(f"Found at {(x,y)}")
            return x*4_000_000 + y


if __name__ == '__main__':
    print(f"Part 2: {part2()}")

# day 14

from pprint import pprint
import numpy as np
from collections import namedtuple
import re

INPUT = 'data/sample.txt'

pour_point = (500, 0)
point_pattern = re.compile(f'\d+,\d+')

Rock = namedtuple('Rock', ['offset', 'size', 'data'])


def create_point(s):
    x, y = s.split(',')
    return (int(x), int(y))


def bounding_box(points):
    def first(x): return x[0]
    def second(x): return x[1]

    return ((min(map(first, points)), min(map(second, points))),
            (max(map(first, points)), max(map(second, points))))


def load_lines():
    """Read input file and return the rock structure"""
    all_points = set()
    all_lines = set()
    with open(INPUT, 'r') as f:
        for line in f.readlines():
            points = list(map(create_point, point_pattern.findall(line)))
            all_points.update(points)
            for start in range(len(points) - 1):
                all_lines.add((points[start], points[start+1]))

    all_points.add(pour_point)
    return bounding_box(all_points), all_lines


def normalize(rock, p):
    x,y = p
    result = (x - rock.offset[0], y - rock.offset[1])
    return result


def draw(rock, p1, p2):
    x1, y1 = normalize(rock, p1)
    x2, y2 = normalize(rock, p2)
    print(f"Draw from {(x1,y1)} to {(x2,y2)}")
    if x1 == x2:
        rock.data[min(y1,y2):max(y1,y2)+1, x1] = '#'
    else:
        rock.data[y1, min(x1,x2):max(x1,x2)+1] = '#'


def create_rock(box, lines):
    minx, miny = box[0]
    maxx, maxy = box[1]
    height = 1 + maxy-miny
    width = 1 + maxx-minx
    offset = (minx, miny)
    dims = (height, width)
    data = np.array(['.'] * (height * width), dtype=str).reshape(dims)
    rock = Rock(offset, dims, data)
    for p1, p2 in lines:
        draw(rock, p1, p2)
    return rock


if __name__ == '__main__':
    rock = create_rock(*load_lines())
    pprint(rock.data)

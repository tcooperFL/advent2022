# day 14

import numpy as np
from collections import namedtuple
import re

INPUT = 'data/day14.txt'

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
    x, y = p
    result = (x - rock.offset[0], y - rock.offset[1])
    return result

def occupy(rock, p, c):
    x, y = p
    rock.data[y, x] = c

def inspect(rock, p):
    x, y = p
    return rock.data[y, x]

def draw(rock, p1, p2):
    x1, y1 = normalize(rock, p1)
    x2, y2 = normalize(rock, p2)
    if x1 == x2:
        rock.data[min(y1, y2):max(y1, y2)+1, x1] = '#'
    else:
        rock.data[y1, min(x1, x2):max(x1, x2)+1] = '#'

def create_rock(box, lines):
    minx, miny = box[0]
    maxx, maxy = box[1]
    height = 1 + maxy-miny
    width = 1 + maxx-minx
    dims = (height, width)
    data = np.array(['.'] * (height * width), dtype=str).reshape(dims)
    rock = Rock(box[0], dims, data)
    for p1, p2 in lines: draw(rock, p1, p2)
    return rock

def pour(rock, p):
    next_p = p
    while next_p:
        x, y = p
        for next_p in ((x, y+1), (x-1, y+1), (x+1, y+1), None):
            if next_p and inspect(rock, next_p) == '.':
                p = next_p
                break
    return p

def fill(rock):
    current = start = normalize(rock, pour_point)
    count = 0
    try:
        while True:
            next_point = pour(rock, start)
            if next_point == current:
                break
            current = next_point
            occupy(rock, current, 'o')
            count += 1
    except:
        # We started spilling out
        print("Spilling!")
        pass
    return count

def part1():
    # Load model and solve
    rock = create_rock(*load_lines())
    return fill(rock) 

def part2():
    # Load the model
    box, lines = load_lines()

    # Extend the bounding box
    floor_y = box[1][1] + 2
    minx = min(box[0][0], pour_point[0] - (floor_y + 1))
    maxx = max(box[1][0], pour_point[0] + floor_y + 1)
    new_box = ((minx, box[0][1]), (maxx, floor_y))

    # Add a new floor below
    lines.add(((0, floor_y), (maxx-1, floor_y)))

    # Create model and solve
    rock = create_rock(new_box, lines)
    return fill(rock)

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

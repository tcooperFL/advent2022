# day 3 parts 1 and 2

def common_item(s1, *rest):
    base = set(s1.strip())
    for s in rest:
        base = base.intersection(s.strip())
    return base.pop()

def priority(c):
    if c.islower():
        return 1 + ord(c) - ord('a')
    return 27 + ord(c) - ord('A')

def run(collector):
    total = 0
    with open('data/day3.txt', 'r') as f:
        while True:
            if collections := collector(f):
                common = common_item(*collections)
                total = total + priority(common)
            else:
                break
    return total

## Part 1

def halfs(s):
    s = s.strip()
    midpoint = len(s) // 2
    return (s[0:midpoint], s[midpoint:])

def split_compartments(f):
    if line := f.readline():
        return halfs(line)
    else:
        return None

def part1():
    print(f"Total for part 1 is {run(split_compartments)}")

part1()

## Part 2

def collect_group(f):
    if first := f.readline():
        return (first, f.readline(), f.readline())
    else:
        return None

def part2():
    print(f"Total for part 2 is {run(collect_group)}")

part2()

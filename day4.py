# day 4 parts 1 and 2

class Assignment:
    def __init__(self, s: str):
        lower_string, upper_string = s.split('-')
        self.lower = int(lower_string)
        self.upper = int(upper_string)

    def contains(self, a) -> bool:
        return (self.lower <= a.lower) and (self.upper >= a.upper)
    
    def has_containment(self, a) -> bool:
        return self.contains(a) or a.contains(self)

    def overlaps(self, a) -> bool:
        if self.lower <= a.lower:
            return self.upper >= a.lower
        else:
            return self.lower <= a.upper

    def has_overlap(self, a) -> bool:
        return self.overlaps(a) or a.overlaps(self)

    def __str__(self):
        return f"Assignment({self.lower} - {self.upper})"

def solve(method):
    count = 0
    with open('data/day4.txt', 'r') as f:
        while line := f.readline():
            a1, a2 = map(Assignment, line.split(','))
            if method(a1, a2):
                count = count + 1
    return count

if __name__ == "__main__":
    print(f"Part 1: {solve(Assignment.has_containment)}")
    print(f"Part 2: {solve(Assignment.has_overlap)}")

# day 7
from collections import defaultdict

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = defaultdict(lambda: None)
        self.parent = parent

    def add_child(self, s):
        size, name = s.split()
        if size == 'dir':
            child = self.children[name] or Dir(name, self)
        else:
            child = self.children[name] or File(name, int(size))
        
        self.children[name] = child

    def get_size(self):
        return sum(map(lambda c: c.get_size(), self.children.values()))

    def get_parent(self):
        return self.parent

    def get_child(self, name):
        return self.children[name]

    def get_directories(self):
        for child in self.children.values():
            if type(child) == Dir:
                yield child
                for subdir in child.get_directories():
                    yield subdir

def build_tree():
    """Parse the input file to construct the root directory tree and return the root"""
    root = Dir('/')
    current = None

    with open('data/day7.txt', 'r') as f:
        while line := f.readline():
            match line.split():
                case ['$', 'cd', '/']:
                    current = root
                case ['$', 'cd', '..']:
                    current = current.get_parent() or root
                case ['$', 'cd', dir]:
                    current = current.get_child(dir)
                case ['$', 'ls']:
                    pass
                case _:
                    current.add_child(line)

    return root

def part1():
    """Sum of small directories"""
    root = build_tree()
    small_dirs = filter(lambda d: d.get_size() <= 100000, root.get_directories())
    return sum(map(lambda d: d.get_size(), small_dirs))

def part2():
    """Smallest dir to remove to get under size limit"""
    root = build_tree()
    sizes = sorted([d.get_size() for d in root.get_directories()])
    excess = root.get_size() - 40000000
    return next(n for n in sizes if n >= excess)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

# day 9

class Knot:
    def __init__(self, name):
        self.name = name
        self.x = self.y = 0
        self.followers = []
        self.history = set([str(self),])

    def move(self, dx, dy):
        if (dx, dy) != (0, 0):
            self.x += dx
            self.y += dy
            # print(f"Move {save} dx={dx}, dy={dy} to {self}")
            self.history.add(str(self))
            for follower in self.followers:
                self._pull(follower)

    def attach(self, tail):
        self.followers.append(tail)
    
    @staticmethod
    def _inch(d):
        if d == 0:
            return 0
        return d // abs(d)

    def _pull(self, follower):
        while not (abs(self.x - follower.x) <= 1 and abs(self.y - follower.y) <= 1):
            dx = self._inch(self.x - follower.x)
            dy = self._inch(self.y - follower.y)
            follower.move(dx, dy)

    def get_history(self):
        return self.history

    def __str__(self):
        return f"{self.name}({self.x},{self.y})"

def simulate(knot):
    with open('data/day9.txt', 'r') as f:
        while motion := f.readline():
            dir, s = motion.split()
            count = int(s)
            match dir:
                case 'U':
                    knot.move(-count, 0)
                case 'D':
                    knot.move(count, 0)
                case 'L':
                    knot.move(0, -count)
                case 'R':
                    knot.move(0, count)
                case _:
                    raise ValueError(f"Unknown direction: {dir}")

def stretch(head, n):
    knots = [head]
    for i in range(1, n + 1):
        k = Knot(f"T{i}")
        knots[i-1].attach(k)
        knots.append(k)
    return knots


if __name__ == '__main__':
    
    head = Knot('H')
    tail = Knot('T')
    head.attach(tail)
    simulate(head)

    print(f"Part 1: {len(tail.get_history())}")

    head = Knot('H')
    rope = stretch(head, 9)
    simulate(head)

    print(f"Part 2: {len(rope[9].get_history())}")

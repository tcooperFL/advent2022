# day 16 part 1

import re
from collections import deque
from typing import List, Dict

INPUT = 'data/day16.txt'
TIMER = 30

def load_graph() -> Dict[str, Dict[int, List[str]]]:
    """Parse the input file and return a graph in dicts"""
    g = {}
    with open(INPUT, 'r') as f:
        while line := f.readline():
            valve, *tunnels = re.findall(r'([A-Z][A-Z])', line)
            rate = int(re.findall(r'\d+', line)[0])
            g[valve] = dict(rate=rate, tunnels=tunnels)
    return g


def map_distances(g) -> None:
    """Store the distance to every other valve with each valve"""
    for valve in g.keys():
        distances = {valve: 0}
        d = 1
        queue = deque(g[valve]['tunnels'])
        while queue:
            for v in list(queue):
                queue.popleft()
                if v not in distances:
                    distances[v] = d
                    queue.extend(g[v]['tunnels'])
            d += 1
        g[valve]['distances'] = distances


def greatest_pressure(g, valve: str, minutes: int, remaining: List[str]) -> int:
    """Find the greatest weighted path from this valve to the others"""
    if minutes >= TIMER:
        return 0
    
    max_flow = 0
    distances = g[valve]['distances']

    for i in range(len(remaining)):
        v = remaining[i]
        dist = distances[v]
        time = minutes + dist + 1;
        del remaining[i]
        node_flow = ((30 - min(time, 30)) * g[v]['rate']);
        flow = node_flow + greatest_pressure(g, v, time, remaining);
        remaining.insert(i, v)
        if flow > max_flow:
            max_flow = flow

    return max_flow


def solve():
    # parse the input into a graph structure
    g = load_graph()
    
    # For each node, calculate distances to all non-zero pressure valves
    map_distances(g)

    # Starting from AA, find the greatest path within the time limit.
    valves_with_flows = list(filter(lambda v: g[v]['rate'] > 0, g.keys()))
    return greatest_pressure(g, 'AA', 0, valves_with_flows)


if __name__ == '__main__':
    print(f"Part 1 is {solve()}")

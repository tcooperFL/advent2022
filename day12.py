# day 12

import networkx as nx
import itertools

def accessible(g, height, neighbor) -> bool:
    try:
        neighbor_height = g.nodes[neighbor]['height']
        return neighbor_height <= height + 1
    except:
        return False

def build_graph():
    g = nx.DiGraph()

    # Create nodes
    with open('data/day12.txt', 'r') as f:
        r = 0
        while line := f.readline():
            for c, ch in zip(itertools.count(), list(line.strip())):
                node = (r, c)
                if ch == 'S':
                    source = node
                    ch = 'a'
                elif ch == 'E':
                    target = node
                    ch = 'z'
                g.add_node(node, height=(ord(ch) - ord('a')))
            r = r + 1
    
    # Create ediges
    rows = r; cols = c+1
    for r in range(rows):
        for c in range(cols):
            neighbors = ((r, c-1), (r-1, c), (r+1, c), (r, c+1))
            height = g.nodes[(r,c)]['height']
            for neighbor in filter(lambda n: accessible(g, height, n), neighbors):
                g.add_edge((r,c), neighbor)    

    print(f"Graph is {rows} x {cols} with {nx.number_of_nodes(g)} nodes and {nx.number_of_edges(g)} edges")
    return g, source, target

def part1():
    g, source, target = build_graph()
    return nx.shortest_path_length(g, source, target)

def part2():
    g, source, target = build_graph()
    for source, length in nx.single_target_shortest_path_length(g, target):
        if g.nodes[source]['height'] == 0:
            return length

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

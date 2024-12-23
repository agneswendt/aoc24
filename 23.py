import time
from aocd.models import Puzzle
from collections import defaultdict

day, year = 23, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(tuple(line.split("-")))
    return res


def p1(data):
    neighbors = defaultdict(set)
    for a, b in data:
        neighbors[a].add(b)
        neighbors[b].add(a)

    res = set()

    for n0 in neighbors:
        for n1 in neighbors[n0]:
            for n2 in neighbors[n1]:
                for n3 in neighbors[n2]:
                    if n3 == n0:
                        if any(item.startswith("t") for item in [n0, n1, n2]):
                            res.add(frozenset([n0, n1, n2]))
    return len(res)


def max_clique(graph, r, p, x):
    if not p and not x:
        return r
    u = max(p.union(x), key=lambda v: len(p.intersection(graph[v])))
    return max_clique(
        graph, r.union([u]), p.intersection(graph[u]), x.intersection(graph[u])
    )


def p2(data):
    nodes = set()
    for a, b in data:
        nodes.add(a)
        nodes.add(b)
    nodes = list(nodes)

    graph = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

    for a, b in data:
        graph[nodes.index(a)][nodes.index(b)] = 1
        graph[nodes.index(b)][nodes.index(a)] = 1

    graph = [set(i for i, v in enumerate(row) if v) for row in graph]
    return ",".join(
        sorted(
            [nodes[i] for i in max_clique(graph, set(), set(range(len(nodes))), set())]
        )
    )


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

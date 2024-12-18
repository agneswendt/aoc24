import time
from aocd.models import Puzzle
from heapq import heappush, heappop

day, year = 18, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(tuple(map(int, line.split(","))))
    return res


def dijkstra(start, end, corruptions):
    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Q = []
    heappush(Q, (0, start))

    while Q:
        cost, curr = heappop(Q)
        if curr in visited:
            continue
        visited.add(curr)
        if curr == end:
            return cost
        x, y = curr
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < end[0] + 1 and 0 <= ny < end[1] + 1:
                if (nx, ny) not in corruptions:
                    heappush(Q, (cost + 1, (nx, ny)))
    return None


def solve(data):
    r1, r2 = 0, 0
    r1 = dijkstra((0, 0), (70, 70), data[:1024])
    for i in range(2976, len(data)):
        res = dijkstra((0, 0), (70, 70), data[:i])
        if res is None:
            r2 = ",".join(map(str, data[i - 1]))
            break
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

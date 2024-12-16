import time
from aocd.models import Puzzle
from heapq import heappush, heappop
from collections import defaultdict

day, year = 16, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(list(line))
    return res


def dijkstra(grid, start, end):
    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Q = []
    heappush(Q, (0, (0, 0), (1, 0), start))
    parent = defaultdict(list)
    res = float("inf")

    while Q:
        cost, last, last_dir, curr = heappop(Q)
        lx, ly = last_dir
        if (last_dir, curr) in visited:
            continue
        visited.add((last_dir, curr))
        parent[curr].append((cost, last_dir, last))

        if curr == end:
            res = min(res, cost)
        x, y = curr
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if grid[ny][nx] != "#" and (nx, ny) not in visited:
                if (lx != 0 and dy != 0) or (ly != 0 and dx != 0):
                    heappush(Q, (cost + 1001, (x, y), (dx, dy), (nx, ny)))
                elif last_dir == (dx, dy):
                    heappush(Q, (cost + 1, (x, y), (dx, dy), (nx, ny)))
    return res, parent


def dfs(parent, end, cost):
    path = set()
    stack = []
    for p in parent[end]:
        n_cost, n_dir, n = p
        if cost - n_cost == 0:
            path.add(n)
            stack.append(p)

    while stack:
        cost, dir, curr = stack.pop()
        dx, dy = dir
        for p in parent[curr]:
            n_cost, n_dir, n = p
            nx, ny = n_dir
            diff_cost = 1001 if (nx != 0 and dy != 0) or (ny != 0 and dx != 0) else 1
            if cost - n_cost == diff_cost:
                if n not in path:
                    path.add(n)
                    stack.append(p)
    return path


def solve(data):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                start = (x, y)
            if data[y][x] == "E":
                end = (x, y)
    cost, parent = dijkstra(data, start, end)
    path = dfs(parent, end, cost)
    return cost, len(path)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

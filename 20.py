import time
from aocd.models import Puzzle
from heapq import heappush, heappop

day, year = 20, 2024


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
    heappush(Q, (0, start))
    dists = {}

    while Q:
        cost, curr = heappop(Q)
        if curr in visited:
            continue
        visited.add(curr)
        dists[curr] = cost

        x, y = curr
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if grid[ny][nx] != "#" and (nx, ny) not in visited:
                heappush(Q, (cost + 1, (nx, ny)))
    return dists


def skips(start, end, skip_len):
    solutions = []
    for sx, sy in start:
        for ex, ey in end:
            if abs(sx - ex) + abs(sy - ey) <= skip_len:
                solutions.append(
                    start[(sx, sy)] + end[(ex, ey)] + abs(sx - ex) + abs(sy - ey)
                )
    return solutions


def solve(data):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                start = (x, y)
            if data[y][x] == "E":
                end = (x, y)
    costs_from_start = dijkstra(data, start, end)
    costs_from_end = dijkstra(data, end, start)
    end_val = costs_from_start[end]
    p1 = skips(costs_from_start, costs_from_end, 2)
    r1 = sum(end_val - solution >= 100 for solution in p1)
    p2 = skips(costs_from_start, costs_from_end, 20)
    r2 = sum(end_val - solution >= 100 for solution in p2)
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

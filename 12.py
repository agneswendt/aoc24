import time
from aocd.models import Puzzle
import re

day, year = 12, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        l = line
        res.append(l)
    return res


def bfs(grid, x, y, target):
    visited = set()
    stack = [(x, y)]
    delimiters = set()
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and grid[ny][nx] == target
            ):
                stack.append((nx, ny))
            else:
                delimiters.add(((x, y), (nx, ny)))
    return visited, delimiters


def tuple_diff(a, b):
    return a[0] - b[0], a[1] - b[1]


def count_sides(delimiters):
    res = 0
    for a1, b1 in delimiters:
        for a2, b2 in delimiters:
            a_diff = tuple_diff(a1, a2)
            b_diff = tuple_diff(b1, b2)
            if a_diff == b_diff and ((a_diff == (0, 1)) or (a_diff == (1, 0))):
                res += 1
    return res


def solve(data):
    visited = set()
    r1, r2 = 0, 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (x, y) in visited:
                continue
            v, delimiters = bfs(data, x, y, data[y][x])
            sides = len(delimiters) - count_sides(delimiters)
            r1 += len(v) * len(delimiters)
            r2 += len(v) * sides
            visited.update(v)
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

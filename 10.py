import time
from aocd.models import Puzzle

day, year = 10, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        line = list(map(int, line))
        res.append(line)
    return res


def bfs(data, start, use_visited=True):
    stack = [start]
    visited = set()
    score = 0
    while stack:
        x, y = stack.pop()
        if use_visited and (x, y) in visited:
            continue
        visited.add((x, y))
        if data[y][x] == 9:
            score += 1
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(data[0])
                and 0 <= ny < len(data)
                and data[ny][nx] - data[y][x] == 1
            ):
                stack.append((nx, ny))
    return score


def solve(data):
    r1, r2 = 0, 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                start = (x, y)
                r1 += bfs(data, start)
                r2 += bfs(data, start, False)
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

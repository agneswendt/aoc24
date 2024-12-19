import time
from aocd.models import Puzzle
from functools import cache

day, year = 19, 2024


def get_input():
    data = Puzzle(year, day).input_data
    half = False
    towels, patterns = [], []
    for line in data.splitlines():
        if not line:
            half = True
            continue
        if half:
            patterns.append(line)
        else:
            towels = line.split(", ")
    return towels, patterns


@cache
def search(towels, pattern):
    if not pattern:
        return 1
    res = 0
    for towel in towels:
        if pattern.startswith(towel):
            res += search(towels, pattern[len(towel) :])
    return res


def solve(data):
    towels, patterns = data
    r1, r2 = 0, 0
    for pattern in patterns:
        res = search(tuple(towels), pattern)
        if res > 0:
            r1 += 1
        r2 += res
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

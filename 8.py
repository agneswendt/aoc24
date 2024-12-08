import time
from aocd.models import Puzzle
from collections import defaultdict

day, year = 8, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(line)
    return res


def solve(data):
    locations = defaultdict(list)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != ".":
                locations[c].append((x, y))
    a1, a2 = set(), set()
    for freq in locations:
        for (x1, y1) in locations[freq]:
            for (x2, y2) in locations[freq]:
                if (x1, y1) == (x2, y2):
                    continue
                d1, d2 = (x1 - x2, y1 - y2)
                i = 0
                while True:
                    r1, r2 = (i * d1 + x1, i * d2 + y1)
                    if 0 <= r1 < len(data[0]) and 0 <= r2 < len(data):
                        if i == 1:
                            a1.add((r1, r2))
                        a2.add((r1, r2))
                        i += 1
                    else:
                        break
    return len(a1), len(a2)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

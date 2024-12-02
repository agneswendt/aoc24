import time
from aocd.models import Puzzle
import re

day, year = 2, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        l = list(map(int, re.findall(r"[-\d]+", line)))
        res.append(l)
    return res


def check(l):
    diffs = []
    for i in range(1, len(l)):
        diffs.append(l[i - 1] - l[i])
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def p1(data):
    return sum(check(l) for l in data)


def p2(data):
    safe = 0
    for l in data:
        if check(l):
            safe += 1
        else:
            for i in range(len(l)):
                if check(l[:i] + l[i + 1 :]):
                    safe += 1
                    break
    return safe


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

import time
from aocd.models import Puzzle
import re

day, year = 7, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        val, l = line.split(': ')
        l = list(map(int, l.split(' ')))
        res.append((int(val), l))
    return res


def t1(target, val, l):
    if not l and target == val:
        return True
    elif val > target:
        return False
    elif not l:
        return False
    return  any((t1(target, val + l[0], l[1:]), t1(target, val * l[0], l[1:])))


def t2(target, val, l):
    if not l and target == val:
        return True
    elif val > target:
        return False
    elif not l:
        return False
    n_val = int(f"{val}{l[0]}")
    return  any((t2(target, val + l[0], l[1:]), t2(target, val * l[0], l[1:]), t2(target, n_val, l[1:])))


def solve(data):
    r1, r2 = 0, 0
    for item in data:
        val, l = item
        r1 += val if t1(val, 0, l) else 0
        r2 += val if t2(val, 0, l) else 0
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

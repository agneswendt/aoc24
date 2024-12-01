import time
from aocd.models import Puzzle
import re

day, year = 1, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(tuple(map(int, re.findall(r"\d+", line))))
    return res


def p1(data):
    data = list(zip(*data))
    p1, p2 = data
    p1, p2 = sorted(p1), sorted(p2)
    dist = 0
    for i1, i2 in zip(p1, p2):
        dist += abs(i1 - i2)
    return dist


def p2(data):
    data = list(zip(*data))
    p1, p2 = data
    res = 0
    for i1 in p1:
        temp = 0
        for i2 in p2:
            temp += i1 == i2
        res += temp * i1
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

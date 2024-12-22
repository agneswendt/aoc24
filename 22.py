import time
from aocd.models import Puzzle
from collections import defaultdict
import re

day, year = 22, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(int(line))
    return res


def p1(data):
    r3 = data
    r3_hist = [[num % 10 for num in r3]]

    for _ in range(2000):
        r1 = [num * 64 for num in r3]
        r2 = [n1 ^ n2 for n1, n2 in zip(r3, r1)]
        r3 = [num % 16777216 for num in r2]

        r1 = [num // 32 for num in r3]
        r2 = [n1 ^ n2 for n1, n2 in zip(r3, r1)]
        r3 = [num % 16777216 for num in r2]

        r1 = [num * 2048 for num in r3]
        r2 = [n1 ^ n2 for n1, n2 in zip(r3, r1)]
        r3 = [num % 16777216 for num in r2]

        r3_hist.append([num % 10 for num in r3])

    diffs = []
    for n1, n2 in zip(r3_hist[1:], r3_hist):
        diffs.append([a - b for a, b in zip(n1, n2)])
    diffs = list(zip(*diffs))

    r3_hist_t = list(zip(*r3_hist))

    seqs = defaultdict(int)
    for j, diff in enumerate(diffs):
        seen = set()
        for i, seq in enumerate(zip(diff, diff[1:], diff[2:], diff[3:]), start=4):
            if seq in seen:
                continue
            seen.add(seq)
            seqs[seq] += r3_hist_t[j][i]
    return sum(r3), max(seqs.values())


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = p1(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

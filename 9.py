import time
from aocd.models import Puzzle
import re

day, year = 9, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        line = line
        res.append(line)
    return res[0]


def p1(data):
    id = 0
    space = []
    for i, c in enumerate(data):
        if i % 2 == 0:
            for j in range(int(c)):
                space.append(id)
            id += 1
        else:
            for j in range(int(c)):
                space.append(-1)
    for i, id in enumerate(reversed(space)):
        if id == -1:
            continue
        i = len(space) - i - 1
        for j, val in enumerate(space):
            if val != -1:
                continue
            space[j] = space[i]
            space[i] = -1
            break
    res = 0
    for i, id in enumerate(space):
        if id == -1:
            continue
        res += (i - 1) * id
    return res


def p2(data):
    id = 0
    space = []
    for i, c in enumerate(data):
        if i % 2 == 0:
            space.append((id, int(c), 0))
            id += 1
        else:
            space[-1] = (space[-1][0], space[-1][1], int(c))
    for i in range(len(space)):
        i = len(space) - i - 1
        id1, size1, free1 = space[i]
        for k, (id2, size2, free2) in enumerate(space):
            if k >= i:
                break
            if free2 - size1 >= 0:
                space[i] = (id1, 0, free1 + size1)
                space.insert(k + 1, (id1, size1, free2 - size1))
                space[k] = (id2, size2, 0)
    k, res = 0, 0
    for id, size, free in space:
        for i in range(size):
            res += k * id
            k += 1
        k += free
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

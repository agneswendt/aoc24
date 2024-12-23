import time
from aocd.models import Puzzle
from itertools import permutations
from functools import cache
from frozendict import frozendict
import re

day, year = 21, 2024

numeric = frozendict({
        "7": (0, 0),
        "8": (1, 0),
        "9": (2, 0),
        "4": (0, 1),
        "5": (1, 1),
        "6": (2, 1),
        "1": (0, 2),
        "2": (1, 2),
        "3": (2, 2),
        "0": (1, 3),
        "A": (2, 3),
    })

directional = frozendict({
        "^": (1, 0),
        "A": (2, 0),
        "<": (0, 1),
        "v": (1, 1),
        ">": (2, 1),
    })


diff = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1),
}


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        res.append(list(line))
    return res


def sub_tuples(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])


def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


@cache
def search(map, seq, depth):
    if depth == 0:
        return len(seq)
    curr = map["A"]
    total = 0
    for input in seq:
        dx, dy = sub_tuples(map[input], curr)
        string = ""
        if dx > 0:
            string += ">"*dx
        elif dx < 0:
            string += "<"*abs(dx)
        if dy > 0:
            string += "v"*dy
        elif dy < 0:
            string += "^"*abs(dy)
        res = []
        for perm in permutations(string):
            temp = curr
            for char in perm:
                temp = add_tuples(temp, diff[char])
                if temp not in map.values():
                    break
            else:
                new_seq = "".join(perm) + "A"
                res.append(search(directional, new_seq, depth-1))
        total += min(res)
        curr = map[input]
    return total


def solve(data):
    r1, r2 = 0, 0
    for code in data:
        l1 = search(numeric, tuple(code), 3)
        l2 = search(numeric, tuple(code), 26)
        r1 += l1*int("".join(code[:-1]))
        r2 += l2*int("".join(code[:-1]))
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

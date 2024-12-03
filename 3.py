import time
from aocd.models import Puzzle


day, year = 3, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        l = line
        res.append(l)
    return res


def solve(data):
    res = 0
    for line in data:
        r1 = line.split("mul(")
        r2 = []
        for str in r1:
            r2.append(str.split(")"))
        for lst in r2:
            for str in lst:
                r3 = str.split(",")
                try:
                    assert len(r3) == 2
                    mul = int(r3[0]) * int(r3[1])
                except:
                    mul = 0
                res += mul
    return res


def split_seg(data):
    enabled = True
    res = []
    line = "".join(data)
    while line:
        if enabled:
            r1 = line.split("don't()")
            res.append(r1[0])
            enabled = False
            line = "don't()".join(r1[1:])
        else:
            r1 = line.split("do()")
            enabled = True
            line = "do()".join(r1[1:])
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = solve(data)
    p2 = solve(split_seg(data))
    print(p1, p2)
    print("Time: ", time.time() - start)

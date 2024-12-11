import time
from aocd.models import Puzzle
from functools import cache

day, year = 11, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        line = list(map(int, line.split(" ")))
        res.append(line)
    return res[0]


@cache
def traverse(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return traverse(1, n - 1)
    s_stone = str(stone)
    if len(s_stone) % 2 == 0:
        return traverse(int(s_stone[: len(s_stone) // 2]), n - 1) + traverse(
            int(s_stone[len(s_stone) // 2 :]), n - 1
        )
    else:
        return traverse(stone * 2024, n - 1)


def solve(data):
    p1 = sum(traverse(stone, 25) for stone in data)
    p2 = sum(traverse(stone, 75) for stone in data)
    return p1, p2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

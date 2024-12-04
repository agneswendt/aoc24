import time
from aocd.models import Puzzle


day, year = 4, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        l = line
        res.append(l)
    return res


def p1(data):
    res = 0
    target = "XMAS"
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for x in range(len(data)):
        for y in range(len(data[x])):
            for direction in directions:
                dx, dy = direction
                i = 0
                while (
                    0 <= x + i * dx < len(data)
                    and 0 <= y + i * dy < len(data[x])
                    and i < len(target)
                ):
                    if data[x + i * dx][y + i * dy] != target[i]:
                        break
                    i += 1
                if i == 4:
                    res += 1
    return res


def p2(data):
    res = 0
    targets = ["MAS", "SAM"]
    for x in range(len(data)):
        for y in range(len(data[x])):
            for s1 in targets:
                for s2 in targets:
                    valid = True
                    for (dx, dy, n_x, n_y, s) in [
                        (1, 1, x, y, s1),
                        (-1, 1, x + 2, y, s2),
                    ]:
                        i = 0
                        while (
                            0 <= n_x + i * dx < len(data)
                            and 0 <= n_y + i * dy < len(data[x])
                            and i < len(s)
                        ):
                            if data[n_x + i * dx][n_y + i * dy] != s[i]:
                                break
                            i += 1
                        if i != 3:
                            valid = False
                            break
                    if valid:
                        res += 1
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

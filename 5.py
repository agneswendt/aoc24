import time
from aocd.models import Puzzle


day, year = 5, 2024


def get_input():
    data = Puzzle(year, day).input_data
    rules = []
    updates = []
    passed = False
    for line in data.splitlines():
        if not passed:
            if line == "":
                passed = True
                continue
            rules.append(tuple(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))
    return (rules, updates)


def solve(data):
    rules, updates = data
    r1, r2 = 0, 0
    for update in updates:
        sorted, changed = False, False
        while not sorted:
            sorted = True
            for rule in rules:
                x, y = rule
                if x in update and y in update and update.index(x) > update.index(y):
                    update[update.index(x)], update[update.index(y)] = y, x
                    sorted = False
                    changed = True
        if not changed:
            r1 += update[len(update) // 2]
        else:
            r2 += update[len(update) // 2]

    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

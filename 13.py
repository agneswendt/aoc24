import time
from aocd.models import Puzzle
import numpy as np

day, year = 13, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    machine = []
    for line in data.splitlines():
        if "A" in line or "B" in line:
            x = int(line.split("X+")[1].split(",")[0])
            y = int(line.split("Y+")[1].split(",")[0])
            machine.append(x)
            machine.append(y)
        elif "Prize" in line:
            x = int(line.split("X=")[1].split(",")[0])
            y = int(line.split("Y=")[1].split(",")[0])
            machine.append(x)
            machine.append(y)
        else:
            res.append(machine)
            machine = []
    res.append(machine)
    return res


def solve(data):
    r1, r2 = 0, 0
    for elem in data:
        xa, ya, xb, yb, goal_x, goal_y = elem
        a = np.array([[xa, xb], [ya, yb]])
        b1 = np.array([goal_x, goal_y])
        b2 = np.array([10000000000000 + goal_x, 10000000000000 + goal_y])
        sol1 = np.linalg.solve(a, b1)
        sol2 = np.linalg.solve(a, b2)
        x1, y1 = sol1
        x2, y2 = sol2
        tol = 10 ** (-4)
        if (x1 % 1 <= tol or (1 - x1 % 1) <= tol) and (
            y1 % 1 <= tol or (1 - y1 % 1) <= tol
        ):
            r1 += round(x1) * 3 + round(y1)
        if (x2 % 1 <= tol or (1 - x2 % 1) <= tol) and (
            y2 % 1 <= tol or (1 - y2 % 1) <= tol
        ):
            r2 += round(x2) * 3 + round(y2)
    return r1, r2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

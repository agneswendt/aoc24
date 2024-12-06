import time
from aocd.models import Puzzle

day, year = 6, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for l in data.splitlines():
        line = l
        res.append(list(line))
    return res


def find_obstacles(data):
    obstacles = set()
    start = (0, 0)
    directions = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    dir = None
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == "#":
                obstacles.add((j, i))
            elif y in (">", "<", "^", "v"):
                start = (j, i)
                dir = directions[y]
    return obstacles, start, dir


def change_dir(dir):
    match dir:
        case (0, -1):
            return (1, 0)
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)
        case (1, 0):
            return (0, 1)


def p1(data):
    obstacles, start, dir = find_obstacles(data)
    x, y = start
    steps = set()
    while 0 <= x < len(data) and 0 <= y < len(data[0]):
        if (x, y) in obstacles:
            x, y = (x - dir[0], y - dir[1])
            dir = change_dir(dir)
            continue
            
        steps.add((x, y))
        x, y = (x + dir[0], y + dir[1])
    return len(steps)


def p2(data):
    obstacles, start, start_dir = find_obstacles(data)
    x, y = start
    steps = set()
    dir = start_dir
    res = 0
    for yy in range(len(data)):
        for xx in range(len(data[0])):
            if (xx, yy) not in obstacles:
                obstacles.add((xx, yy))
                x, y = start
                dir = start_dir
                steps = set()   
                while 0 <= x < len(data) and 0 <= y < len(data[0]):
                    if (x, y) in obstacles:
                        x, y = (x - dir[0], y - dir[1])
                        dir = change_dir(dir)
                        continue

                    if ((x, y), dir) in steps:
                        res += 1
                        break

                    steps.add(((x, y), dir))
                    x, y = (x + dir[0], y + dir[1])
                obstacles.remove((xx, yy))
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

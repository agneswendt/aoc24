import time
from aocd.models import Puzzle
import re
import time

day, year = 14, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    for line in data.splitlines():
        data = tuple(map(int, re.findall(r"-?\d+", line)))
        res.append(data)
    return res


def p1(data):
    seconds = 100
    board_x = 101
    board_y = 103
    quadrants = [0, 0, 0, 0]
    coords = []
    for p1, p2, v1, v2 in data:
        x = (p1 + seconds * v1) % board_x
        y = (p2 + seconds * v2) % board_y
        coords.append((x, y))
        quadrants[0] += 1 if x < board_x // 2 and y < board_y // 2 else 0
        quadrants[1] += 1 if x > board_x // 2 and y < board_y // 2 else 0
        quadrants[2] += 1 if x < board_x // 2 and y > board_y // 2 else 0
        quadrants[3] += 1 if x > board_x // 2 and y > board_y // 2 else 0
    res = 1
    for q in quadrants:
        res *= q
    return res


def print_board(x, y, coords):
    for i in range(y):
        for j in range(x):
            if (j, i) in coords:
                print("#", end="")
            else:
                print(".", end="")
        print()


def p2(data):
    seconds = 7550
    board_x = 101
    board_y = 103
    while True:
        coords = []
        for p1, p2, v1, v2 in data:
            x = (p1 + seconds * v1) % board_x
            y = (p2 + seconds * v2) % board_y
            coords.append((x, y))
        print_board(board_x, board_y, coords)
        print(seconds)
        time.sleep(0.2)
        seconds += 1


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

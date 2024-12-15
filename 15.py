import time
from aocd.models import Puzzle
import re
from copy import deepcopy

day, year = 15, 2024


def get_input():
    data = Puzzle(year, day).input_data
    half = False
    board = []
    moves = []
    for line in data.splitlines():
        if not half:
            if line == "":
                half = True
                continue
            board.append(list(line))
        else:
            moves.append(line)
    return board, "".join(moves)


def print_board(board):
    for line in board:
        print("".join(line))


def can_move(board, pos, dir):
    while True:
        x, y = pos
        dx, dy = dir
        if board[y + dy][x + dx] == ".":
            return (x + dx, y + dy)
        if board[y + dy][x + dx] == "#":
            return False
        pos = (x + dx, y + dy)


def p1(data):
    board, moves = data
    board = deepcopy(board)
    pos = (0, 0)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "@":
                pos = (x, y)
                break
    assert pos != (0, 0)
    dirs = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in moves:
        dir = dirs[move]
        dx, dy = dir
        new_pos = can_move(board, pos, dir)
        if new_pos:
            x, y = pos
            board[y][x] = "."
            nx, ny = new_pos
            board[ny][nx] = board[y + dy][x + dx]
            board[y + dy][x + dx] = "@"
            pos = x + dx, y + dy
    res = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "O":
                res += y * 100 + x
    return res


def p2(data):
    board, moves = data
    new_board = [["" for _ in range(len(board[0]) * 2)] for _ in range(len(board))]
    pos = (0, 0)
    dirs = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for y in range(len(board)):
        for x in range(len(board[y])):
            match board[y][x]:
                case "@":
                    new_board[y][2 * x] = "@"
                    pos = (2 * x, y)
                    new_board[y][2 * x + 1] = "."
                case ".":
                    new_board[y][2 * x] = "."
                    new_board[y][2 * x + 1] = "."
                case "#":
                    new_board[y][2 * x] = "#"
                    new_board[y][2 * x + 1] = "#"
                case "O":
                    new_board[y][2 * x] = "["
                    new_board[y][2 * x + 1] = "]"
    board = new_board
    assert pos != (0, 0)

    for move in moves:
        dir = dirs[move]
        n_board = deepcopy(board)
        success = move_dir(n_board, pos, dir)
        if success:
            board = n_board
            pos = pos[0] + dir[0], pos[1] + dir[1]

    res = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "[":
                res += y * 100 + x
    return res


def move_dir(board, pos, dir):
    dx, dy = dir
    new_pos = can_move(board, pos, dir)
    x, y = pos
    if new_pos:
        while pos != new_pos:
            nx, ny = new_pos
            if board[ny][nx] in ("[", "]") and dir in ((0, -1), (0, 1)):
                branch_x = nx + 1 if board[ny][nx] == "[" else nx - 1
                success = move_dir(board, (branch_x, ny), dir)
                if not success:
                    return False
            board[ny][nx] = board[ny - dy][nx - dx]
            new_pos = nx - dx, ny - dy
        board[y][x] = "."
    else:
        return False
    return True


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

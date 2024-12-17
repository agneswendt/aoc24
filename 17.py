import time
from aocd.models import Puzzle
import re
from math import gcd

day, year = 17, 2024


def get_input():
    data = Puzzle(year, day).input_data
    res = []
    half = False
    for line in data.splitlines():
        l = line
        if not half:
            if line == "":
                half = True
                continue
            res.append(int(l.split(": ")[1]))
        else:
            res.append(list(map(int, l.split(": ")[1].split(","))))

    return res


def run(A, B, C, program):
    i = 0
    output = []
    while i < len(program):
        operand, instr = program[i], program[i + 1]
        combo = -1
        if 0 <= instr <= 3:
            combo = instr
        elif instr == 4:
            combo = A
        elif instr == 5:
            combo = B
        elif instr == 6:
            combo = C

        jmp = False
        match operand:
            case 0:
                A = A // (2**combo)
            case 1:
                B = B ^ instr
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    jmp = True
                    i = instr
            case 4:
                B = B ^ C
            case 5:
                output.append(combo % 8)
            case 6:
                B = A // (2**combo)
            case 7:
                C = A // (2**combo)

        if not jmp:
            i += 2
    return output


def p1(data):
    A, B, C, program = data
    return ",".join(map(str, run(A, B, C, program)))


def search(program, mult, i, A=0):
    if i == -1:
        return A
    start = 1 if i == 15 else 0
    ret = [float("inf")]
    for j in range(start, 8):
        res = run(A + mult[i] * j, 0, 0, program)
        if res[i] == program[i]:
            ret.append(search(program, mult, i - 1, A + mult[i] * j))
    return min(ret)


def p2(data):
    _, _, _, program = data
    factors = [8**i for i in range(0, 16)]
    return search(program, factors, 15)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)

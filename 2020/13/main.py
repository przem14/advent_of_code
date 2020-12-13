import functools
import operator


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
        return int(lines[0]), [int(x) if x != "x" else 0 for x in lines[1].split(",")]


def solve_first(schedule):
    time, buses = schedule
    t, bus_id = min([(b - (time % b), b) for b in filter(lambda x: x != 0, buses)])
    return t * bus_id


def mod_inverse(a, b):
    x, y = 1, 0
    r, s = 0, 1
    while b != 0:
        c, q = a % b, a // b
        a, b = b, c
        x, r = r, x - q * r
        y, s = s, y - q * s
    return y


def solve_second(schedule):
    busses = list(filter(lambda x: x[1] > 0, enumerate(schedule[1])))
    x, n = 0, functools.reduce(operator.mul, [x for _, x in busses])
    for i, m in busses:
        ni = n // m
        x += ni * mod_inverse(m, ni) * (m - i)
    return x % n


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

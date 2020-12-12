import functools
import itertools


def read_input(filename):
    with open(filename) as file:
        return [list(line.strip()) for line in file]


def adjacent_seats(seat, seats, skip_list):
    rows, cols = len(seats), len(seats[0])
    dirs = filter(lambda s: s != (0, 0), itertools.product([-1, 0, 1], [-1, 0, 1]))
    result = []
    for dir in dirs:
        x, y = seat[0] + dir[0], seat[1] + dir[1]
        while 0 <= x < cols and 0 <= y < rows and seats[y][x] in skip_list:
            x, y = x + dir[0], y + dir[1]
        result.append((x, y))
    return list(filter(lambda s: 0 <= s[0] < cols and 0 <= s[1] < rows, result))


def make_invalid_grid(seats):
    return [list("X" * len(row)) for row in seats]


def new_value(seat, adj, prev, taken_limit):
    x, y = seat
    if prev[y][x] == "L" and all(prev[b][a] in [".", "L"] for (a, b) in adj):
        return "#"
    elif prev[y][x] == "#" and [prev[b][a] for (a, b) in adj].count("#") >= taken_limit:
        return "L"
    return prev[y][x]


def solve(seats, skip_list, taken_limit):
    prev, current = make_invalid_grid(seats), seats
    while any(l != r for l, r in zip(prev, current)):
        prev, current = current, make_invalid_grid(seats)
        for y in range(len(prev)):
            for x in range(len(prev[y])):
                adj = adjacent_seats((x, y), seats, skip_list)
                current[y][x] = new_value((x, y), adj, prev, taken_limit)

    return functools.reduce(lambda a, b: a + b, [s.count("#") for s in current])


def solve_first(seats):
    return solve(seats, skip_list=[], taken_limit=4)


def solve_second(seats):
    return solve(seats, skip_list=".", taken_limit=5)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

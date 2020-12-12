import math


def read_input(filename):
    with open(filename) as file:
        return [(line[0], int(line[1:])) for line in file]


def rotate(vec, angle):
    s = int(math.sin(angle))
    c = int(math.cos(angle))
    return c * vec[0] + s * vec[1], c * vec[1] - s * vec[0]


def move_fwd_vector(move, current_fwd):
    if move == "N":
        return 0, 1
    if move == "S":
        return 0, -1
    if move == "E":
        return 1, 0
    if move == "W":
        return -1, 0
    return current_fwd


def solve_first(moves):
    loc, fwd = (0, 0), (1, 0)
    for move, step in moves:
        if move in "LR":
            fwd = rotate(fwd, math.radians(step if move == "R" else -step))
        else:
            move_fwd = move_fwd_vector(move, fwd)
            loc = (loc[0] + move_fwd[0] * step, loc[1] + move_fwd[1] * step)
    return abs(loc[0]) + abs(loc[1])


def solve_second(moves):
    loc, way = (0, 0), (10, 1)
    for move, step in moves:
        if move in "LR":
            way = rotate(way, math.radians(step if move == "R" else -step))
        if move == "F":
            loc = (loc[0] + way[0] * step, loc[1] + way[1] * step)
        else:
            move_fwd = move_fwd_vector(move, (0, 0))
            way = (way[0] + move_fwd[0] * step, way[1] + move_fwd[1] * step)
    return abs(loc[0]) + abs(loc[1])


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

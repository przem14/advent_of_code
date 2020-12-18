import functools


def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def cube(x, y, z):
    return {
        (a, b, c)
        for a in [x - 1, x, x + 1]
        for b in [y - 1, y, y + 1]
        for c in [z - 1, z, z + 1]
    }


def adjacent(x, y, z):
    return cube(x, y, z).difference({(x, y, z)})


def adjacent_4d(x, y, z, w):
    return {
        (a, b, c, d) for a, b, c in cube(x, y, z) for d in [w - 1, w, w + 1]
    }.difference({(x, y, z, w)})


def init_set(start, extension):
    res = set()
    for y, line in enumerate(start):
        for x, v in enumerate(line):
            if v == "#":
                res.add((x, y) + extension)
    return res


def solve(start, extension, adjacent_func):
    current = init_set(start, extension)
    for i in range(6):
        new_set = set()
        points = current.union(
            functools.reduce(lambda s, p: s.union(adjacent_func(*p)), current, set())
        )
        for p in points:
            count_active = len(list(filter(lambda p: p in current, adjacent_func(*p))))
            if p in current:
                if count_active in [2, 3]:
                    new_set.add(p)
            else:
                if count_active == 3:
                    new_set.add(p)
        current = new_set
    return len(current)


def solve_first(start):
    return solve(start, extension=(0,), adjacent_func=adjacent)


def solve_second(start):
    return solve(start, extension=(0, 0), adjacent_func=adjacent_4d)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

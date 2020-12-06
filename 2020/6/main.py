import functools


def read_input(filename):
    data = []

    with open(filename) as file:
        groups = []
        for line in file:
            if line == "\n":
                data.append(groups)
                groups = []
            else:
                groups.append(line.strip())
        data.append(groups)
    return data


def solve(func, data):
    return functools.reduce(
        lambda a, b: a + len(b),
        [functools.reduce(func, [set(list(g)) for g in d]) for d in data],
        0,
    )


def solve_first(data):
    return solve(lambda a, b: a.union(b), data)


def solve_second(data):
    return solve(lambda a, b: a.intersection(b), data)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))
    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

import functools


def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip())
    return data


def get_seat_id(input):
    bit = {"F": 0, "B": 1, "L": 0, "R": 1}
    return functools.reduce(lambda x, y: (x << 1) | bit[y], input, 0)


def solve_first(data):
    return max([get_seat_id(d) for d in data])


def solve_second(data):
    s = [get_seat_id(d) for d in data]
    return next(iter(set(range(min(s), max(s))) - set(s)))


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

import functools


def read_input(filename):
    notes = {"list": [], "fields": {}}
    current_key = None

    with open(filename) as file:
        for line in file:
            if line == "\n":
                continue
            if current_key == "nearby tickets":
                notes["list"].append([int(x) for x in line.strip().split(",")])
                continue
            if current_key == "your ticket":
                notes["ticket"] = [int(x) for x in line.strip().split(",")]
                current_key = None
                continue
            current_key, val = [x.strip() for x in line.strip().split(":")]
            if val != "":
                notes["fields"][current_key] = [
                    [int(x) for x in r.strip().split("-")]
                    for r in val.strip().split(" or ")
                ]
        return notes


def solve_first(notes):
    s = 0
    for l in notes["list"]:
        for x in l:
            invalid = True
            for key, ranges in notes["fields"].items():
                r0, r1 = ranges
                if r0[0] <= x <= r0[1] or r1[0] <= x <= r1[1]:
                    invalid = False
            if invalid:
                s += x
    return s


def solve_second(notes):
    v = []
    for lst in notes["list"]:
        valid_fields = [set() for _ in range(0, len(lst))]
        for i, x in enumerate(lst):
            for key, ranges in notes["fields"].items():
                r0, r1 = ranges
                if r0[0] <= x <= r0[1] or r1[0] <= x <= r1[1]:
                    valid_fields[i].add(key)
        if set() not in valid_fields:
            v.append(valid_fields)

    p = v[0]
    for x in filter(lambda a: set() not in a, v):
        for i, y in enumerate(x):
            p[i] = p[i].intersection(y)

    x = next(iter(list(filter(lambda a: len(a) == 1, p))[0]))
    while any(len(s) != 1 for s in p):
        n = None
        for s in filter(lambda a: len(a) != 1 and x in a, p):
            s.remove(x)
            if len(s) == 1:
                n = next(iter(s))
        x = n

    return functools.reduce(
        lambda a, b: a * notes["ticket"][b[0]],
        filter(lambda k: "departure" in k[1], enumerate([list(x)[0] for x in p])),
        1,
    )


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

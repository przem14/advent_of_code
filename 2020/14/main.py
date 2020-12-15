import functools


def read_input(filename):
    with open(filename) as file:
        return [[x.strip() for x in line.split("=")] for line in file]


def apply(mask, val):
    return functools.reduce(
        lambda x, p: (x | (1 & int(p[1].replace("X", "0"))) << p[0])
        & ~((1 ^ int(p[1].replace("X", "1"))) << p[0]),
        enumerate(reversed(mask)),
        val,
    )


def get_addresses(mask, address):
    return functools.reduce(
        lambda s, p: set([a | (int(p[1].replace("X", "1")) << p[0]) for a in s]).union(
            a & ~(p[1].count("X") << p[0]) | (int(p[1].replace("X", "0")) << p[0])
            for a in s
        ),
        enumerate(reversed(mask)),
        {address},
    )


def solve(ops, onMem):
    mask, mem = "X" * 36, {}
    for code, val in ops:
        if code.startswith("mask"):
            mask = val
        elif code.startswith("mem"):
            onMem(mem, int(code[4:-1]), int(val), mask)
    return functools.reduce(lambda x, y: x + y[1], mem.items(), 0)


def solve_first(ops):
    def onMem(mem, address, val, mask):
        mem[address] = apply(mask, val)

    return solve(ops, onMem)


def solve_second(ops):
    def onMem(mem, address, val, mask):
        mem.update({a: val for a in get_addresses(mask, address)})

    return solve(ops, onMem)


if __name__ == "__main__":
    example_data = read_input("example_1.in")
    second_example_data = read_input("example_2.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(second_example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

def read_input(filename):
    contains = {}
    with open(filename) as file:
        for line in file:
            [bag, connections] = line.strip(".\n").split(" contain ")
            contains[bag.rstrip("s")] = list(
                filter(
                    lambda x: x[0] != "no",
                    [v.rstrip("s").split(maxsplit=1) for v in connections.split(", ")],
                )
            )
    return contains


def dfs(graph, memoize, default, func):
    def dfs_internal(b):
        if memoize[b] is not None:
            return memoize[b]
        memoize[b] = default
        for [d, u] in graph[b]:
            memoize[b] = func(d, memoize[b], dfs_internal(u))
        return memoize[b]

    for v in graph.keys():
        dfs_internal(v)


def solve_first(data):
    contains_shiny_gold = {
        b: True if b == "shiny gold bag" else None for b in data.keys()
    }
    dfs(data, contains_shiny_gold, False, lambda d, mem, value: mem or value)
    return list(contains_shiny_gold.values()).count(True) - 1


def solve_second(data):
    count_bags = {b: 0 if len(l) == 0 else None for b, l in data.items()}
    dfs(data, count_bags, 0, lambda d, mem, value: mem + int(d) + int(d) * value)
    return count_bags["shiny gold bag"]


if __name__ == "__main__":
    example_data = read_input("example.in")
    example2_data = read_input("example2.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))
    print("example2 2nd result: {}".format(solve_second(example2_data)))
    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

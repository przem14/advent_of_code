import functools


def read_input(filename):
    with open(filename) as file:
        return [
            [
                x[0].strip().split(),
                x[1].strip(")").removeprefix("contains ").split(", "),
            ]
            for x in [line.strip().split("(") for line in file]
        ]


def find_mapping(food_list):
    ingredients = functools.reduce(lambda s, x: s.union(x[0]), food_list, set())
    allergens = functools.reduce(lambda s, x: s.union(x[1]), food_list, set())

    mapping = {k: ingredients.copy() for k in allergens}
    for i, a in food_list:
        for x in a:
            mapping[x] = mapping[x].intersection(i)

    queue = [y[0] for y in filter(lambda x: len(x[1]) == 1, mapping.items())]
    while len(queue) > 0:
        a = queue.pop()
        for x in allergens:
            if len(mapping[x]) == 1:
                continue
            mapping[x] = mapping[x].difference(mapping[a])
            if len(mapping[x]) == 1:
                queue.append(x)

    return mapping


def solve_first(msg):
    ingredients_with_allergens = functools.reduce(
        lambda s, x: s.union(x), find_mapping(msg).values()
    )
    return functools.reduce(
        lambda s, x: s + len(set(x[0]).difference(ingredients_with_allergens)), msg, 0
    )


def solve_second(msg):
    mapping = find_mapping(msg)
    return ",".join([next(iter(mapping[k])) for k in sorted(mapping)])


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

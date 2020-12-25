def read_input(filename):
    with open(filename) as file:
        return [x for x in file]


def move(p, dir):
    if dir == "e":
        return p[0] + 1, p[1]
    if dir == "w":
        return p[0] - 1, p[1]
    if dir == "se":
        return p[0] + 1, p[1] + 1
    if dir == "sw":
        return p[0], p[1] + 1
    if dir == "ne":
        return p[0], p[1] - 1
    if dir == "nw":
        return p[0] - 1, p[1] - 1
    return p

set()
    for path in paths:
        i = 0
        p = 0, 0
        while i < len(path):
            dir = path[i]
            if dir in "ns":
                dir = path[i : i + 2]
                i += 1
            i += 1
            p = move(p, dir)
        if p in points:
            points.remove(p)
        else:
            points.add(p)
def adjacent(p):
    return [move(p, d) for d in ["e", "w", "se", "sw", "ne", "nw"]]


def init(paths):
    points = set()
    for path in paths:
        i = 0
        p = 0, 0
        while i < len(path):
            dir = path[i]
            if dir in "ns":
                dir = path[i : i + 2]
                i += 1
            i += 1
            p = move(p, dir)
        if p in points:
            points.remove(p)
        else:
            points.add(p)
    return points


def solve_first(paths):
    return len(init(paths))


def solve_second(paths):
    points = init(paths)

    for i in range(0, 100):
        new_points = set()
        all_points = points.copy()
        for p in points:
            all_points = all_points.union(set(adjacent(p)))

        for p in all_points:
            adjs = set(adjacent(p))
            blacks = points.intersection(adjs)
            if p in points:
                if len(blacks) in [1, 2]:
                    new_points.add(p)
            else:
                if len(blacks) == 2:
                    new_points.add(p)
        points = new_points

    return len(points)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

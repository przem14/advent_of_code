import math
import functools


class Border:
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    msg = {}
    i = 0
    while i < len(lines):
        if len(lines[i]) == 0:
            i += 1
            continue
        key = int(lines[i].split()[1][:-1])
        msg[key] = []
        for k in range(10):
            msg[key].append(lines[i + k + 1])
        i += 11
    return msg


def ordered_borders(grid):
    left = "".join([x[0] for x in grid])
    right = "".join([x[-1] for x in grid])
    return [grid[0], left, grid[-1], right]


def transform(grid, n, func):
    new_grid = [["x"] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            xp, yp = func(x, y)
            new_grid[yp][xp] = grid[y][x]

    return ["".join(x) for x in new_grid]


def rotate_grid(grid, n):
    return transform(grid, n, lambda x, y: (y, n - x - 1))


def flip_v_grid(grid, n):
    return transform(grid, n, lambda x, y: (x, n - y - 1))


def flip_h_grid(grid, n):
    return transform(grid, n, lambda x, y: (n - x - 1, y))


TRANSFORMS = [
    lambda x, n: x,
    lambda x, n: rotate_grid(x, n),
    lambda x, n: rotate_grid(rotate_grid(x, n), n),
    lambda x, n: rotate_grid(rotate_grid(rotate_grid(x, n), n), n),
    lambda x, n: flip_v_grid(x, n),
    lambda x, n: rotate_grid(flip_v_grid(x, n), n),
    lambda x, n: rotate_grid(rotate_grid(flip_v_grid(x, n), n), n),
    lambda x, n: rotate_grid(rotate_grid(rotate_grid(flip_v_grid(x, n), n), n), n),
    lambda x, n: flip_h_grid(x, n),
    lambda x, n: rotate_grid(flip_h_grid(x, n), n),
    lambda x, n: rotate_grid(rotate_grid(flip_h_grid(x, n), n), n),
    lambda x, n: rotate_grid(rotate_grid(rotate_grid(flip_h_grid(x, n), n), n), n),
    lambda x, n: flip_h_grid(flip_v_grid(x, n), n),
    lambda x, n: rotate_grid(flip_h_grid(flip_v_grid(x, n), n), n),
    lambda x, n: rotate_grid(rotate_grid(flip_h_grid(flip_v_grid(x, n), n), n), n),
    lambda x, n: rotate_grid(
        rotate_grid(rotate_grid(flip_h_grid(flip_v_grid(x, n), n), n), n), n
    ),
]


def remove_border(grid):
    return [line[1:-1] for line in grid[1:-1]]


def match(pattern, text):
    res = True
    for i in range(len(pattern)):
        if pattern[i] == "#" and text[i] != "#":
            res = False
    return res


def count_sea_monsters(grid):
    pattern = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    points = set()
    for i in range(len(grid) - len(pattern) + 1):
        for j in range(len(grid[i]) - len(pattern[0])):
            if all(
                match(pattern[k], grid[i + k][j : j + len(pattern[k])])
                for k in range(len(pattern))
            ):
                points = points.union(
                    set(
                        filter(
                            lambda x: grid[x[1]][x[0]] == "#"
                            and pattern[x[1] - i][x[0] - j] == "#",
                            {
                                (x, y)
                                for x in range(j, j + len(pattern[0]))
                                for y in [i, i + 1, i + 2]
                            },
                        )
                    )
                )
    return len(points)


def create_full_grid(msg, n, out_ids, out_transform):
    full_grid = [["x"] * n * 8 for _ in range(n * 8)]
    for y in range(len(full_grid)):
        for x in range(len(full_grid[0])):
            i = (y // 8) * n + (x // 8)
            full_grid[y][x] = remove_border(
                TRANSFORMS[out_transform[i]](msg[out_ids[i]], 10)
            )[y % 8][x % 8]
    return ["".join(x) for x in full_grid]


def find_corners(borders, msg):
    corners = {
        k: set(functools.reduce(lambda x, y: x + y, borders[k], [])) for k in msg.keys()
    }
    corners_cp = corners.copy()
    for k in corners.keys():
        for kp in corners.keys():
            if k == kp:
                continue
            corners[k] = corners[k].difference(corners_cp[kp])
    corners = list(filter(lambda x: len(x[1]) == 4, corners.items()))
    return corners


def generate_all(grid):
    return [
        ordered_borders(TRANSFORMS[i](grid, len(grid))) for i in range(len(TRANSFORMS))
    ]


def solve(n, i, borders, out_ids, out_borders, out_transform, corners):
    if (n * n) == i:
        return True

    keys = filter(
        lambda k: k not in out_ids,
        (
            [x[0] for x in corners]
            if i in [0, n - 1, (n * n) - n, n * n - 1]
            else borders.keys()
        ),
    )
    for key in keys:
        for j, b in enumerate(borders[key]):
            if (
                ((i // n) == 0) or out_borders[i - n][Border.BOTTOM] == b[Border.TOP]
            ) and (
                ((i % n) == 0) or out_borders[i - 1][Border.RIGHT] == b[Border.LEFT]
            ):
                out_ids.append(key)
                out_borders.append(b)
                out_transform.append(j)
                if solve(
                    n, i + 1, borders, out_ids, out_borders, out_transform, corners
                ):
                    return True
                out_ids.pop()
                out_borders.pop()
                out_transform.pop()

    return False


def solve_first(msg):
    borders = {key: generate_all(grid) for key, grid in msg.items()}
    corners = find_corners(borders, msg)
    return functools.reduce(lambda x, y: x * y, [a[0] for a in corners], 1)


def solve_second(msg):
    borders = {key: generate_all(grid) for key, grid in msg.items()}
    corners = find_corners(borders, msg)

    out_ids, out_borders, out_transform = [], [], []
    n = int(math.sqrt(len(msg.keys())))
    solve(n, 0, borders, out_ids, out_borders, out_transform, corners)

    full_grid = create_full_grid(msg, n, out_ids, out_transform)
    return functools.reduce(lambda x, y: x + y.count("#"), full_grid, 0) - next(
        x
        for x in [
            count_sea_monsters(TRANSFORMS[i](full_grid, len(full_grid)))
            for i in range(len(TRANSFORMS))
        ]
        if x != 0
    )


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

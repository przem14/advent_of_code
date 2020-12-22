import functools


def read_input(filename):
    decks = [], []
    is_second = True
    with open(filename) as file:
        for line in file:
            if line.startswith("Player"):
                is_second = not is_second
                continue
            if line.strip() == "":
                continue
            decks[int(is_second)].append(int(line.strip()))
    return [list(reversed(x)) for x in decks]


def deck_to_int(deck):
    return functools.reduce(lambda x, y: x * 100 + y, deck, 0)


def recursive_combat(decks, play_recursive=True):
    mem = set()
    while decks[0] and decks[1]:
        ids = deck_to_int(decks[0]), deck_to_int(decks[1])
        if play_recursive and ids in mem:
            return 0, []
        mem.add(ids)
        f, s = decks
        a, b = f.pop(), s.pop()
        if (
            (not play_recursive or len(f) < a or len(s) < b)
            and a < b
            or (
                play_recursive
                and (len(f) >= a and len(s) >= b)
                and recursive_combat((decks[0][-a:], decks[1][-b:]))[0] == 1
            )
        ):
            a, b = b, a
            f, s = s, f
        f.insert(0, a)
        f.insert(0, b)
    return 0 if len(decks[0]) != 0 else 1, decks[0], decks[1]


def solve(decks, play_recursive):
    decks = decks[0].copy(), decks[1].copy()
    game = recursive_combat(decks, play_recursive)
    return functools.reduce(
        lambda x, y: x + (y[0] + 1) * y[1], enumerate(game[game[0] + 1]), 0
    )


def solve_first(decks):
    return solve(decks, play_recursive=False)


def solve_second(decks):
    return solve(decks, play_recursive=True)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

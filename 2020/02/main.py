class Data:
    def __init__(self, line):
        tokens = line.split(" ")
        [self.x, self.y] = [int(x) for x in tokens[0].split("-")]
        self.char = tokens[1][0]
        self.string = tokens[2]


def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(Data(line))
    return data


def solve_first(data):
    return [int(d.string.count(d.char) in range(d.x, d.y + 1)) for d in data].count(1)


def solve_second(data):
    return [
        int((d.string[d.x - 1] == d.char) ^ (d.string[d.y - 1] == d.char)) for d in data
    ].count(1)


if __name__ == "__main__":
    data = read_input("both.in")

    print("1st result: #{}".format(solve_first(data)))
    print("2nd result: #{}".format(solve_second(data)))

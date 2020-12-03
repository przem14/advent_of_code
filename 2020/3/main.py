import functools

def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip())
    return data


def solve_first(step, data):
    count = 0
    [x, y] = [0, 0]
    while y < len(data):
        row = data[y]
        if row[x] == '#':
            count += 1
        [x, y] = [(x + step[0]) % len(row), y + step[1]]
    return count

def solve_second(data):
    steps = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    return functools.reduce(lambda x, y: x * y, [solve_first(x, data) for x in steps])


if __name__ == "__main__":
    data = read_input("both.in")

    print("1st result: {}".format(solve_first([3,1],data)))
    print("2nd result: {}".format(solve_second(data)))


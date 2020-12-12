def read_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(int(line))
    return data


def solve_first(num, data):
    values_count = {}
    for i in data:
        values_count[i] = values_count.get(i, 0) + 1
    for i in data:
        values_count[i] -= 1
        diff = num - i
        if values_count.get(diff, 0) > 0:
            return (i, diff)
    return None


def solve_second(num, data):
    data_copy = data.copy()
    while len(data_copy) > 0:
        c = data_copy.pop()
        other = solve_first(num - c, data_copy)
        if other != None:
            return (other[0], other[1], c)
    return None


if __name__ == "__main__":
    data = read_input("both.in")

    first_res = solve_first(2020, data)
    print(
        "a: {} | b: {} | a * b = {}".format(
            first_res[0], first_res[1], first_res[0] * first_res[1]
        )
    )

    second_res = solve_second(2020, data)
    print(
        "a: {} | b: {} | c: {} | a * b * c = {}".format(
            second_res[0],
            second_res[1],
            second_res[2],
            second_res[0] * second_res[1] * second_res[2],
        )
    )

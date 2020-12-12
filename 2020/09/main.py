def read_input(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file]


def solve_first(numbers, preamble_length):
    valid_values = [set() for _ in range(len(numbers) + preamble_length + 1)]
    for i in range(len(numbers)):
        for j in range(1, preamble_length):
            if i + j >= len(numbers):
                break
            valid_values[i].add(numbers[i] + numbers[i + j])
    for i in range(preamble_length, len(numbers)):
        if all(
            numbers[i] not in valid_values[i - j - 1] for j in range(preamble_length)
        ):
            return numbers[i]
    return None


def solve_second(numbers, value):
    for i in range(len(numbers)):
        sum_v, k = 0, i
        while sum_v < value and k < len(numbers):
            sum_v += numbers[k]
            k += 1
        if sum_v == value and k - i != 1:
            return min(numbers[i:k]) + max(numbers[i:k])
    return None


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    example_result = solve_first(example_data, preamble_length=5)
    print("example 1st result: {}".format(example_result))
    print("example 2nd result: {}".format(solve_second(example_data, example_result)))

    result = solve_first(data, preamble_length=25)
    print("1st result: {}".format(result))
    print("2nd result: {}".format(solve_second(data, result)))

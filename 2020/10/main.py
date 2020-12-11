def read_input(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file]


def solve_first(numbers):
    nums = sorted(numbers)
    diff = [x - y for x, y in zip(nums, [0] + nums)]
    return diff.count(1) * (diff.count(3) + 1)


def solve_second(numbers):
    nums = [0] + sorted(numbers) + [max(numbers) + 3]
    sums = [1 if i == 0 else 0 for i in range(len(nums))]
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[i] - nums[j] <= 3:
            sums[i] += sums[j]
            j -= 1
    return sums[-1]


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

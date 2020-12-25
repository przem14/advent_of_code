def loop_size(pk):
    value = 1
    subject_num = 7
    res = 0
    while value != pk:
        res += 1
        value = (value * subject_num) % 20201227
    return res


def encryption_key(pk, lsize):
    value = 1
    while lsize > 0:
        value = (value * pk) % 20201227
        lsize -= 1
    return value


def solve_first(pks):
    return encryption_key(pks[1], loop_size(pks[0]))


def solve_second(pks):
    return "Merry Christmas!"


if __name__ == "__main__":
    example_data = 5764801, 17807724
    data = 10441485, 1004920

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

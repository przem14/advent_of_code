def solve(seq, n):
    mem = {x: i for i, x in enumerate(seq)}
    for i in range(len(seq) - 1, n - 1):
        seq.append(i - mem[seq[i]] if seq[i] in mem else 0)
        mem[seq[i]] = i
    return seq[-1]


if __name__ == "__main__":
    example_data = [0, 3, 6]
    data = [0, 1, 5, 10, 3, 12, 19]
    print("example 1st result: {}".format(solve(example_data, 2020)))
    print("example 2nd result: {}".format(solve(example_data, 30000000)))

    print("1st result: {}".format(solve(data, 2020)))
    print("2nd result: {}".format(solve(data, 30000000)))

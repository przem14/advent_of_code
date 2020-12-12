import re


def read_input(filename):
    data = []

    with open(filename) as file:
        passport = {}
        for line in file:
            if line == "\n":
                data.append(passport)
                passport = {}
            else:
                passport.update(
                    {k: v for [k, v] in [p.split(":") for p in line.split()]}
                )
        data.append(passport)
    return data


def solve_first(data):
    mandatory_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return sum(len(mandatory_keys - set(x.keys())) == 0 for x in data)


def solve_second(data):
    checks = {
        "byr": r"(19[2-9]\d|200[0-2])$",
        "iyr": r"20(1\d|20)$",
        "eyr": r"20(2\d|30)$",
        "hgt": r"(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$",
        "hcl": r"#(\d|[a-f]){6}$",
        "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"\d{9}$",
    }

    return sum(
        (len(set(checks.keys()) - set(p.keys())) == 0)
        and all(bool(re.match(c, p[k])) for k, c in checks.items())
        for p in data
    )


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))
    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

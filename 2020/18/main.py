import operator


def read_input(filename):
    with open(filename) as file:
        return [
            line.strip().replace("(", "( ").replace(")", " )").strip().split()
            for line in file
        ]


def op_func(c):
    return operator.add if c == "+" else operator.mul


def reduce(values, operators, until_op_eq):
    while len(operators) > 0 and operators[-1] == until_op_eq:
        values[-2] = op_func(operators.pop())(values[-2], values[-1])
        values.pop()


def solve(equations, is_mul_lp):
    results, lower_precedence_op = [], "*" if is_mul_lp else "#"
    for eq in equations:
        literals, ops = [], []
        for literal in eq:
            if literal in "+*(":
                ops.append(literal)
                continue
            elif literal.isnumeric():
                literals.append(int(literal))
            elif literal == ")":
                reduce(literals, ops, lower_precedence_op)
                ops.pop()
            if len(literals) != 1 and ops[-1] not in ("(" + lower_precedence_op):
                reduce(literals, ops, ops[-1])
        reduce(literals, ops, lower_precedence_op)
        results += literals

    return sum(results)


def solve_first(equations):
    return solve(equations, is_mul_lp=False)


def solve_second(equations):
    return solve(equations, is_mul_lp=True)


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

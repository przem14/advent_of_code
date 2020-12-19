def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    rules = {}
    i = 0
    while len(lines[i]) > 0:
        key, rule = lines[i].split(":")
        rules[key] = [r.strip().split(" ") for r in rule.split("|")]
        i += 1
    texts = [x.strip() for x in lines[(i + 1) :]]
    return rules, texts


def generate(v, rules, out):
    if len(rules[v]) == 1 and rules[v][0] and rules[v][0][0].strip('"') in "ab":
        out[v] = set(rules[v][0][0].strip('"'))
    if v in out:
        return out[v]

    out[v] = set()
    for r in rules[v]:
        texts = {""}
        for u in r:
            new_texts = set()
            for t in generate(u, rules, out):
                for x in texts:
                    new_texts.add(x + t)
            texts = new_texts
        out[v] = out[v].union(texts)
    return out[v]


def is_matching(text, out, np, ns):
    if text == "":
        return ns != 0 and np > ns

    res = False
    for prefix in out["42"]:
        if text.startswith(prefix):
            res |= is_matching(text[len(prefix) :], out, np + 1, ns)
    if np > (ns + 1):
        for suffix in out["31"]:
            if text.endswith(suffix):
                res |= is_matching(text[: -len(suffix)], out, np, ns + 1)
    return res


def solve_first(msg):
    valid_strings = generate("0", msg[0], {})
    return sum(int(x in valid_strings) for x in msg[1])


def solve_second(msg):
    out = {}
    generate("0", msg[0], out)
    return sum(is_matching(x, out, 0, 0) for x in msg[1])


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

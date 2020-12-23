class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None

    def set_next(self, nxt):
        self.nxt = nxt

    def drop_next_three(self):
        res = [self.nxt, self.nxt.nxt, self.nxt.nxt.nxt]
        self.nxt = res[-1].nxt
        res[-1].nxt = None
        return res

    def insert(self, nodes):
        nxt = self.nxt
        self.nxt = nodes[0]
        nodes[-1].nxt = nxt


def solve(nums, iterations):
    nodes = {n: Node(n) for n in nums}
    for i, n in enumerate(nums):
        nxt = nodes[nums[(i + 1) % len(nums)]]
        nodes[n].set_next(nxt)

    current = nodes[nums[0]]
    for _ in range(iterations):
        cut = current.drop_next_three()
        dst = (current.value - 1) if current.value > 1 else len(nums)
        while dst in [n.value for n in cut]:
            dst = (dst - 1) if dst > 1 else len(nums)
        nodes[dst].insert(cut)
        current = current.nxt

    return nodes


def solve_first(nums):
    nums = nums.copy()
    nodes = solve(nums, iterations=100)

    res = [1]
    while nodes[res[-1]].nxt.value != 1:
        res.append(nodes[res[-1]].nxt.value)
    return "".join([str(x) for x in res])


def solve_second(nums):
    nums = nums.copy() + list(range(10, 1000001))
    nodes = solve(nums, iterations=10000000)
    return nodes[1].nxt.value * nodes[1].nxt.nxt.value


if __name__ == "__main__":
    example_data = [int(c) for c in list("389125467")]
    data = [int(c) for c in list("219748365")]

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))

    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

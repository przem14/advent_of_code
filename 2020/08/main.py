def read_input(filename):
    with open(filename) as file:
        return [line.strip().split() for line in file]


class AccOp:
    @staticmethod
    def execute(machine, arg):
        machine.counter += 1
        machine.accu += int(arg)


class JmpOp:
    @staticmethod
    def execute(machine, arg):
        machine.counter += int(arg)


class NopOp:
    @staticmethod
    def execute(machine, arg):
        machine.counter += 1


class Machine:
    def __init__(self):
        self.accu = 0
        self.counter = 0
        self.history = []
        self.opcodes = {"acc": AccOp, "jmp": JmpOp, "nop": NopOp}

    def run(self, program, halt_condition):
        while self.counter < len(program) and not halt_condition(
            self.history, self.counter
        ):
            self.history.append(self.counter)
            [opcode, arg] = program[self.counter]
            self.opcodes[opcode].execute(self, arg)
        return self.counter >= len(program)

    def reset(self):
        self.accu = 0
        self.counter = 0
        self.history = []


def solve_first(instructions):
    machine = Machine()
    machine.run(instructions, lambda history, counter: counter in history)
    return machine.accu


def solve_second(instructions):
    def switch_instructions(instruction):
        if instruction[0] != "acc":
            instruction[0] = "jmp" if instruction[0] == "nop" else "nop"

    machine = Machine()
    for i in range(len(instructions)):
        switch_instructions(instructions[i])
        if machine.run(instructions, lambda history, counter: counter in history):
            return machine.accu
        machine.reset()
        switch_instructions(instructions[i])
    return None


if __name__ == "__main__":
    example_data = read_input("example.in")
    data = read_input("both.in")

    print("example 1st result: {}".format(solve_first(example_data)))
    print("example 2nd result: {}".format(solve_second(example_data)))
    print("1st result: {}".format(solve_first(data)))
    print("2nd result: {}".format(solve_second(data)))

# experiment1_rtl_alu.py
# Experiment 1: Register Transfer, Arithmetic and Logic Operations

class ALU:
    def execute(self, operation, a, b):
        if operation == "ADD":
            return a + b
        elif operation == "SUB":
            return a - b
        elif operation == "AND":
            return a & b
        elif operation == "OR":
            return a | b
        else:
            raise ValueError("Invalid ALU operation")


class RegisterFile:
    def __init__(self):
        self.regs = {
            "R0": 12,
            "R1": 5,
            "R2": 9,
            "R3": 3
        }

    def read(self, register):
        return self.regs[register]

    def write(self, register, value):
        self.regs[register] = value

    def display(self):
        print("\nCurrent Register Values:")
        for name, value in self.regs.items():
            print(f"{name} = {value}")


def main():
    registers = RegisterFile()
    alu = ALU()

    # Operation format:
    # (operation, source1, source2, destination)
    program = [
        ("ADD", "R0", "R1", "R2"),
        ("SUB", "R0", "R1", "R3"),
        ("AND", "R2", "R3", "R0"),
        ("OR", "R2", "R3", "R1")
    ]

    print("==============================================")
    print(" EXPERIMENT 1: RTL AND ALU SIMULATION")
    print("==============================================")

    print("\nInitial Register Values:")
    registers.display()

    print("\nExecution Trace")
    print("-" * 65)
    print(f"{'Cycle':<8}{'Operation':<18}{'Source Values':<18}{'Result':<10}")
    print("-" * 65)

    cycle = 1

    for operation, source1, source2, destination in program:

        a = registers.read(source1)
        b = registers.read(source2)

        result = alu.execute(operation, a, b)

        registers.write(destination, result)

        operation_text = f"{destination} <- {source1} {operation} {source2}"
        source_values = f"{a}, {b}"

        print(
            f"{cycle:<8}"
            f"{operation_text:<18}"
            f"{source_values:<18}"
            f"{result:<10}"
        )

        cycle += 1

    print("-" * 65)

    print("\nFinal Register Values:")
    registers.display()

    print("\nALU operations completed successfully.")


if __name__ == "__main__":
    main()
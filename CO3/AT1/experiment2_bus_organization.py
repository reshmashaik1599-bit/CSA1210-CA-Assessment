# experiment2_bus_organization.py
# Experiment 2: Single-Bus vs Multi-Bus Organization


class SingleBusSystem:
    def register_to_register(self):
        return 1

    def alu_operation(self):
        # R2 -> temporary register
        # R3 -> ALU
        # ALU result -> bus -> R1
        return 3

    def memory_load(self):
        return 2

    def memory_store(self):
        return 2

    def four_alu_operations(self):
        return 12


class MultiBusSystem:
    def register_to_register(self):
        return 1

    def alu_operation(self):
        # Bus A -> ALU input A
        # Bus B -> ALU input B
        # ALU result -> Bus C -> destination
        return 1

    def memory_load(self):
        return 1

    def memory_store(self):
        return 1

    def four_alu_operations(self):
        return 4


def main():

    single_bus = SingleBusSystem()
    multi_bus = MultiBusSystem()

    print("======================================================")
    print(" EXPERIMENT 2: SINGLE-BUS VS MULTI-BUS ORGANIZATION")
    print("======================================================")

    print("\nCycle Comparison")
    print("-" * 65)

    operations = [
        (
            "Simple register-to-register move",
            single_bus.register_to_register(),
            multi_bus.register_to_register()
        ),
        (
            "R1 <- R2 + R3 (ALU operation)",
            single_bus.alu_operation(),
            multi_bus.alu_operation()
        ),
        (
            "Load from memory into register",
            single_bus.memory_load(),
            multi_bus.memory_load()
        ),
        (
            "Store register to memory",
            single_bus.memory_store(),
            multi_bus.memory_store()
        ),
        (
            "4 back-to-back ALU operations",
            single_bus.four_alu_operations(),
            multi_bus.four_alu_operations()
        )
    ]

    print(
        f"{'Operation':<40}"
        f"{'Single-Bus':<15}"
        f"{'Multi-Bus':<15}"
    )

    print("-" * 65)

    for operation, single, multi in operations:
        print(f"{operation:<40}{single:<15}{multi:<15}")

    print("-" * 65)

    # Calculate speedup for ALU operation
    single_cycles = single_bus.alu_operation()
    multi_cycles = multi_bus.alu_operation()

    speedup = single_cycles / multi_cycles

    print("\nAnalysis")
    print("----------------------------------------------")
    print(f"Single-bus ALU operation : {single_cycles} cycles")
    print(f"Multi-bus ALU operation  : {multi_cycles} cycle")
    print(f"Speedup                  : {speedup:.2f}x")

    print("\nConclusion:")
    print(
        "The multi-bus organization reduces the number of cycles "
        "required for ALU operations by allowing multiple transfers "
        "to occur in parallel."
    )


if __name__ == "__main__":
    main()
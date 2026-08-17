# experiment3_pipeline.py
# Experiment 3: 5-Stage Instruction Pipeline


def simulate_pipeline(num_instructions, num_stages):

    # Ideal pipeline cycle count
    pipelined_cycles = num_stages + (num_instructions - 1)

    # Non-pipelined execution
    non_pipelined_cycles = num_instructions * num_stages

    # Performance calculations
    speedup = non_pipelined_cycles / pipelined_cycles

    pipelined_throughput = (
        num_instructions / pipelined_cycles
    )

    non_pipelined_throughput = (
        num_instructions / non_pipelined_cycles
    )

    return (
        pipelined_cycles,
        non_pipelined_cycles,
        speedup,
        pipelined_throughput,
        non_pipelined_throughput
    )


def display_pipeline(num_instructions):

    stages = ["IF", "ID", "EX", "MEM", "WB"]

    total_cycles = len(stages) + num_instructions - 1

    print("\nPipeline Execution Diagram")
    print("-" * 80)

    print(f"{'Instruction':<15}", end="")

    for cycle in range(1, total_cycles + 1):
        print(f"{cycle:^8}", end="")

    print()

    print("-" * 80)

    for instruction in range(1, num_instructions + 1):

        print(f"I{instruction:<14}", end="")

        start_cycle = instruction

        for cycle in range(1, total_cycles + 1):

            stage_index = cycle - start_cycle

            if 0 <= stage_index < len(stages):
                print(f"{stages[stage_index]:^8}", end="")
            else:
                print(f"{'':^8}", end="")

        print()

    print("-" * 80)


def main():

    num_instructions = 5
    num_stages = 5

    print("==============================================")
    print(" EXPERIMENT 3: 5-STAGE PIPELINE SIMULATION")
    print("==============================================")

    print("\nPipeline Stages:")
    print("IF -> ID -> EX -> MEM -> WB")

    display_pipeline(num_instructions)

    (
        pipelined_cycles,
        non_pipelined_cycles,
        speedup,
        pipelined_throughput,
        non_pipelined_throughput
    ) = simulate_pipeline(num_instructions, num_stages)

    print("\nPerformance Results")
    print("-" * 60)

    print(f"{'Metric':<35}{'Value':>15}")
    print("-" * 60)

    print(
        f"{'Number of instructions':<35}"
        f"{num_instructions:>15}"
    )

    print(
        f"{'Number of stages':<35}"
        f"{num_stages:>15}"
    )

    print(
        f"{'Pipelined cycles':<35}"
        f"{pipelined_cycles:>15}"
    )

    print(
        f"{'Non-pipelined cycles':<35}"
        f"{non_pipelined_cycles:>15}"
    )

    print(
        f"{'Pipelined throughput':<35}"
        f"{pipelined_throughput:.2f} instr/cycle"
    )

    print(
        f"{'Non-pipelined throughput':<35}"
        f"{non_pipelined_throughput:.2f} instr/cycle"
    )

    print(
        f"{'Speedup':<35}"
        f"{speedup:.2f}x"
    )

    print("-" * 60)

    print("\nConclusion:")
    print(
        "Pipelining improves instruction throughput by allowing "
        "multiple instructions to occupy different pipeline stages "
        "at the same time."
    )


if __name__ == "__main__":
    main()
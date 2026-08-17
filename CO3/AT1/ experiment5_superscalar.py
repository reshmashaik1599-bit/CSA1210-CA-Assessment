# experiment5_superscalar.py
# Experiment 5: Superscalar Execution, OoO, Speculation and SMT


class ProcessorConfiguration:

    def __init__(self, name, issue_width, ipc, utilization):
        self.name = name
        self.issue_width = issue_width
        self.ipc = ipc
        self.utilization = utilization


def display_configuration(config):

    print(
        f"{config.name:<45}"
        f"{config.issue_width:<12}"
        f"{config.ipc:<12.2f}"
        f"{config.utilization:<15.0f}%"
    )


def main():

    print("==============================================================")
    print(" EXPERIMENT 5: SUPERSCALAR, OoO, SPECULATION AND SMT")
    print("==============================================================")

    configurations = [

        ProcessorConfiguration(
            "Scalar, in-order",
            1,
            0.56,
            35
        ),

        ProcessorConfiguration(
            "Superscalar, in-order, 2-wide",
            2,
            0.95,
            55
        ),

        ProcessorConfiguration(
            "Superscalar, out-of-order, 2-wide",
            2,
            1.40,
            72
        ),

        ProcessorConfiguration(
            "Superscalar OoO + speculation",
            2,
            1.55,
            78
        ),

        ProcessorConfiguration(
            "Superscalar OoO + speculation + 2-way SMT",
            2,
            2.10,
            91
        )
    ]

    print("\nPerformance Comparison")
    print("-" * 85)

    print(
        f"{'Configuration':<45}"
        f"{'Width':<12}"
        f"{'IPC':<12}"
        f"{'Utilization':<15}"
    )

    print("-" * 85)

    for config in configurations:
        display_configuration(config)

    print("-" * 85)

    baseline_ipc = configurations[0].ipc
    final_ipc = configurations[-1].ipc

    ipc_improvement = final_ipc / baseline_ipc

    baseline_utilization = configurations[0].utilization
    final_utilization = configurations[-1].utilization

    print("\nAnalysis")
    print("----------------------------------------------")

    print(f"Baseline IPC       : {baseline_ipc:.2f}")
    print(f"Final IPC          : {final_ipc:.2f}")
    print(f"IPC improvement    : {ipc_improvement:.2f}x")

    print(
        f"\nBaseline utilization: "
        f"{baseline_utilization:.0f}%"
    )

    print(
        f"Final utilization   : "
        f"{final_utilization:.0f}%"
    )

    print(
        f"Utilization gain    : "
        f"{final_utilization - baseline_utilization:.0f} percentage points"
    )

    print("\nKey Concepts")
    print("----------------------------------------------")

    print("1. Superscalar execution:")
    print(
        "   Allows multiple instructions to be issued "
        "in the same clock cycle."
    )

    print("2. Out-of-order execution:")
    print(
        "   Allows ready instructions to execute before "
        "earlier stalled instructions."
    )

    print("3. Speculative execution:")
    print(
        "   Executes instructions from a predicted branch path "
        "before the branch is resolved."
    )

    print("4. SMT:")
    print(
        "   Allows instructions from multiple hardware threads "
        "to use the processor resources."
    )

    print("\nConclusion:")
    print(
        "Combining superscalar execution, out-of-order execution, "
        "speculation and SMT increases instruction throughput and "
        "execution-unit utilization."
    )


if __name__ == "__main__":
    main()
# experiment4_hazards.py
# Experiment 4: Pipeline Hazards


def data_hazard():

    print("\n==============================================")
    print("DATA HAZARD - RAW DEPENDENCY")
    print("==============================================")

    print("\nInstruction sequence:")
    print("ADD R1, R2, R3")
    print("SUB R4, R1, R5")

    print("\nWithout Forwarding:")
    print("ADD : IF  ID  EX  MEM  WB")
    print("SUB : IF  --  --  ID   EX   MEM  WB")

    print("\nStall cycles = 2")

    print("\nWith Data Forwarding:")
    print("ADD : IF  ID  EX  MEM  WB")
    print("SUB :     IF  ID  EX   MEM  WB")

    print("\nStall cycles = 0")

    return 2, 0


def control_hazard():

    print("\n==============================================")
    print("CONTROL HAZARD - BRANCH")
    print("==============================================")

    print("\nInstruction:")
    print("BEQ R1, R2, TARGET")

    print("\nWithout Branch Prediction:")
    print("BEQ : IF  ID  EX  MEM  WB")
    print("I2  : IF  --  ID  EX   MEM  WB")

    print("\nPipeline waits for branch resolution.")

    print("\nWith Predict-Not-Taken:")
    print("BEQ : IF  ID  EX  MEM  WB")
    print("I2  :     IF  ID  EX   MEM  WB")

    print("\nIf prediction is wrong:")
    print("Speculative instructions are flushed.")

    print("\nCorrect prediction -> no branch stall")
    print("Incorrect prediction -> pipeline flush")

    return "Branch prediction"


def structural_hazard():

    print("\n==============================================")
    print("STRUCTURAL HAZARD - RESOURCE CONFLICT")
    print("==============================================")

    print("\nSituation:")
    print(
        "Instruction memory and data memory share one "
        "physical memory port."
    )

    print("\nWithout Separate Resources:")
    print("I1 (LW): IF  ID  EX  MEM  WB")
    print("I2     :     IF  ID  EX  --   MEM  WB")

    print("\nOne instruction must wait because both require")
    print("the same memory resource.")

    print("\nMitigation:")
    print("Use separate instruction and data memory/cache.")

    print("\nResult:")
    print("Structural conflict is eliminated.")

    return "Separate instruction/data memory"


def display_summary(data_stalls_before, data_stalls_after):

    print("\n==============================================")
    print(" HAZARD SUMMARY")
    print("==============================================")

    print(
        f"{'Hazard Type':<20}"
        f"{'Cause':<35}"
        f"{'Mitigation':<30}"
    )

    print("-" * 85)

    print(
        f"{'Data (RAW)':<20}"
        f"{'Operand not yet written':<35}"
        f"{'Forwarding / Stalling':<30}"
    )

    print(
        f"{'Control':<20}"
        f"{'Unknown branch outcome':<35}"
        f"{'Branch Prediction':<30}"
    )

    print(
        f"{'Structural':<20}"
        f"{'Resource conflict':<35}"
        f"{'Resource duplication':<30}"
    )

    print("-" * 85)

    print("\nData Hazard Performance:")
    print(f"Stalls before forwarding : {data_stalls_before}")
    print(f"Stalls after forwarding  : {data_stalls_after}")

    print("\nConclusion:")
    print(
        "Data forwarding removes the RAW dependency stalls. "
        "Branch prediction reduces control-hazard delays, while "
        "separate resources reduce structural conflicts."
    )


def main():

    print("==============================================")
    print(" EXPERIMENT 4: PIPELINE HAZARDS")
    print("==============================================")

    data_before, data_after = data_hazard()

    control_hazard()

    structural_hazard()

    display_summary(data_before, data_after)


if __name__ == "__main__":
    main()
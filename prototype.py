"""
Universe 25 Population Simulator - Functional Prototype (Progress Report 2)

This file only handles input and output (menu, printing, summary).
All calculations are done by the functions in model.py (Part A).
"""

from model import run_simulation


def print_table(history):
    """Print the generation-by-generation report."""
    print(f"{'Gen':<6}{'Males':<10}{'Females':<10}{'Total':<10}"
          f"{'Births':<10}{'Deaths':<10}{'Resources':<10}")
    print("-" * 66)
    for r in history:
        print(f"{r['generation']:<6}{r['males']:<10}{r['females']:<10}{r['total']:<10}"
              f"{r['births']:<10}{r['deaths']:<10}{r['resources']:<10}")


def check_bookkeeping(history):
    """Confirm the two required identities and that nothing is negative."""
    for prev, cur in zip(history, history[1:]):
        if cur["total"] != prev["total"] + cur["births"] - cur["deaths"]:
            return False
    for r in history:
        if r["males"] + r["females"] != r["total"]:
            return False
        if min(r["males"], r["females"], r["total"], r["births"], r["deaths"], r["resources"]) < 0:
            return False
    return True


def end_state(history):
    """Describe how the run ended."""
    last = history[-1]
    if last["total"] == 0:
        return "Extinct (no mice left)"
    if last["resources"] == 0:
        return "Resources depleted (population limited by supply)"
    return "Population surviving with resources remaining"


def print_summary(history):
    """Print the final summary."""
    last = history[-1]
    print("\nFinal summary")
    print("-" * 66)
    print(f"Generations run     : {last['generation']}")
    print(f"Final population    : {last['total']} (males {last['males']}, females {last['females']})")
    print(f"Total births        : {sum(r['births'] for r in history)}")
    print(f"Total deaths        : {sum(r['deaths'] for r in history)}")
    print(f"Final resources     : {last['resources']}")
    print(f"End-state           : {end_state(history)}")
    print(f"Bookkeeping check   : {'PASSED' if check_bookkeeping(history) else 'FAILED'}")
    print("Note: this is a simplified simulation, not a prediction of real mice.")


def run_and_show(title, males, females, resources, generations, birth_rate, death_rate, replenishment):
    """Run one scenario and print everything."""
    print(f"\n=== {title} ===")
    print(f"Inputs: males={males}, females={females}, resources={resources}, "
          f"generations={generations}, birth_rate={birth_rate}, "
          f"death_rate={death_rate}, replenishment={replenishment}\n")
    try:
        history = run_simulation(males, females, resources, generations,
                                 birth_rate, death_rate, replenishment)
    except ValueError as error:
        print(f"Invalid input rejected: {error}")
        return
    print_table(history)
    print_summary(history)


def custom_scenario():
    """Let the user type their own settings."""
    try:
        males = int(input("Initial males: "))
        females = int(input("Initial females: "))
        resources = int(input("Starting resources: "))
        generations = int(input("Generations (1-100): "))
        birth_rate = float(input("Birth rate (0 to 1): "))
        death_rate = float(input("Death rate (0 to 1): "))
        replenishment = int(input("Resource replenishment per generation: "))
    except ValueError:
        print("Invalid input rejected: please type numbers only.")
        return
    run_and_show("Custom scenario", males, females, resources, generations,
                 birth_rate, death_rate, replenishment)


def main():
    while True:
        print("\nUNIVERSE 25 POPULATION SIMULATOR (Prototype)")
        print("1. Baseline scenario (plenty of resources)")
        print("2. Resource-constrained scenario")
        print("3. Boundary test: no females")
        print("4. Invalid-input test: negative males")
        print("5. Enter my own settings")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            run_and_show("Baseline", 10, 10, 200, 10, 0.5, 0.1, 30)
        elif choice == "2":
            run_and_show("Resource-constrained", 10, 10, 60, 12, 0.5, 0.1, 15)
        elif choice == "3":
            run_and_show("Boundary: no females", 10, 0, 100, 8, 0.5, 0.1, 10)
        elif choice == "4":
            run_and_show("Invalid input: negative males", -5, 10, 100, 8, 0.5, 0.1, 10)
        elif choice == "5":
            custom_scenario()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Please choose 0 to 5.")


if __name__ == "__main__":
    main()
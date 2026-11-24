import math


def round_population(value):
    """Round population calculations to the nearest whole number."""
    return int(value + 0.5)


def calculate_deaths(population, death_rate):
    """Calculate normal deaths based on the death rate."""
    deaths = round_population(population * death_rate)
    return min(deaths, population)


def apply_resource_shortage(males, females, resources):
    """Reduce the surviving population if resources are insufficient."""
    total_population = males + females

    if total_population <= resources:
        return males, females

    if resources <= 0:
        return 0, 0

    # Distribute the available survival capacity proportionally.
    male_survivors = int(resources * males / total_population)
    female_survivors = int(resources * females / total_population)

    remaining = resources - male_survivors - female_survivors

    # Assign any remaining capacity to the group with
    # the larger fractional remainder
    male_remainder = (resources * males / total_population) - male_survivors
    female_remainder = (resources * females / total_population) - female_survivors

    if remaining > 0:
        if male_remainder >= female_remainder:
            male_survivors += 1
        else:
            female_survivors += 1

    return male_survivors, female_survivors


def calculate_births(females, males, birth_rate, available_resources):
    """Calculate births while considering reproduction and resources."""
    if males <= 0 or females <= 0:
        return 0

    possible_births = round_population(females * birth_rate)

    # Births cannot exceed the available resources.
    actual_births = min(possible_births, available_resources)

    return actual_births


def advance_generation(state, birth_rate, death_rate, resource_replenishment):
    """Calculate and update the population for one generation."""

    males = state['males']
    females = state['females']
    resources = state['resources']

    # Step 1: Add new resources.
    resources += resource_replenishment

    # Step 2: Calculate normal deaths.
    male_deaths = calculate_deaths(males, death_rate)
    female_deaths = calculate_deaths(females, death_rate)

    males -= male_deaths
    females -= female_deaths

    total_deaths = male_deaths + female_deaths

    # Step 3: Apply additional deaths caused by resource shortage
    old_total = males + females

    males, females = apply_resource_shortage(males, females, resources)

    shortage_deaths = old_total - (males + females)
    total_deaths += shortage_deaths

    # Step 4: Deduct resources consumed by surviving mice.
    surviving_population = males + females
    resources -= surviving_population

    # Step 5: Calculate births.
    births = calculate_births(females, males, birth_rate, resources)

    # Step 6: Separate newborn mice into males and females.
    newborn_males = births // 2
    newborn_females = births - newborn_males

    # Add newborn mice to the existing population
    males += newborn_males
    females += newborn_females

    # Step 7: Deduct resources consumed by newborn mice.
    resources -= births

    # Step 8: Update the simulation state.
    new_state = {
        "generation": state["generation"] + 1,
        "males": males,
        "females": females,
        "total": males + females,
        "births": births,
        "deaths": total_deaths,
        "resources": max(0, resources),
    }

    return new_state


def validate_inputs(initial_males, initial_females, initial_resources, generations, birth_rate, death_rate, resource_replenishment):

    whole_numbers = [
        initial_males,
        initial_females,
        initial_resources,
        generations,
        resource_replenishment,
    ]

    if any(type(value) is not int for value in whole_numbers):
        raise ValueError("Population and resource values must be whole numbers")

    if any(value < 0 for value in whole_numbers):
        raise ValueError("Population and resource values cannot be negative")

    if not 1 <= generations <= 100:
        raise ValueError("Generations must be between 1 and 100")

    if (not isinstance(birth_rate, (int, float))
            or isinstance(birth_rate, bool)
            or not math.isfinite(birth_rate)):
        raise ValueError("Birth_rate must be a finite number")

    if (not isinstance(death_rate, (int, float))
            or isinstance(death_rate, bool)
            or not math.isfinite(death_rate)):
        raise ValueError("Death_rate must be a finite number")

    if not 0 <= birth_rate <= 1:
        raise ValueError("Birth_rate must be between 0 and 1")

    if not 0 <= death_rate <= 1:
        raise ValueError("Death_rate must be between 0 and 1")


def run_simulation(initial_males, initial_females, initial_resources, generations, birth_rate, death_rate, resource_replenishment):

    """Run the population simulation for the specified generations."""

    validate_inputs(
        initial_males,
        initial_females,
        initial_resources,
        generations,
        birth_rate,
        death_rate,
        resource_replenishment
    )

    state = {
        "generation": 0,
        "males": initial_males,
        "females": initial_females,
        "total": initial_males + initial_females,
        "births": 0,
        "deaths": 0,
        "resources": initial_resources,
    }

    # Store the results of every generation.
    history = [state.copy()]

    # Process each generation.
    for _ in range(generations):
        state = advance_generation(state, birth_rate, death_rate, resource_replenishment)

        history.append(state.copy())

    return history


def display_results(history):
    """Display the population and resource results."""

    print(
        f"{'Gen':<6}{'Males':<10}{'Females':<10}"
        f"{'Total':<10}{'Births':<10}"
        f"{'Deaths':<10}{'Resources':<10}"
    )

    print("-" * 66)

    for record in history:
        print(
            f"{record['generation']:<6}"
            f"{record['males']:<10}"
            f"{record['females']:<10}"
            f"{record['total']:<10}"
            f"{record['births']:<10}"
            f"{record['deaths']:<10}"
            f"{record['resources']:<10}"
        )


if __name__ == "__main__":
    # Example simulation
    results = run_simulation(
        initial_males=10,
        initial_females=10,
        initial_resources=10,
        generations=5,
        birth_rate=0.5,
        death_rate=0.5,
        resource_replenishment=1,
    )

    display_results(results)
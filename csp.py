from places import places


def calculate_total_time(selected):
    return sum(places[p]["visit_time"] for p in selected)


def calculate_total_cost(selected):
    return sum(places[p]["cost"] for p in selected)


def is_valid(selected, available_time, budget):
    total_time = calculate_total_time(selected)
    total_cost = calculate_total_cost(selected)

    return (
        total_time <= available_time
        and total_cost <= budget
    )


def backtrack(
    place_list,
    index,
    selected,
    available_time,
    budget,
    interests,
    best_solution
):

    # Check whether current solution is better
    if len(selected) > len(best_solution):
        best_solution.clear()
        best_solution.extend(selected)

    # All places have been checked
    if index >= len(place_list):
        return

    place = place_list[index]

    # -----------------------------
    # OPTION 1: Include this place
    # -----------------------------

    if places[place]["category"] in interests:

        selected.append(place)

        if is_valid(
            selected,
            available_time,
            budget
        ):
            backtrack(
                place_list,
                index + 1,
                selected,
                available_time,
                budget,
                interests,
                best_solution
            )

        # BACKTRACK
        selected.pop()

    # -----------------------------
    # OPTION 2: Skip this place
    # -----------------------------

    backtrack(
        place_list,
        index + 1,
        selected,
        available_time,
        budget,
        interests,
        best_solution
    )


def optimize_itinerary(
    available_time,
    budget,
    interests
):

    place_list = list(places.keys())

    selected = []
    best_solution = []

    backtrack(
        place_list,
        0,
        selected,
        available_time,
        budget,
        interests,
        best_solution
    )

    return best_solution

if __name__ == "__main__":

    result = optimize_itinerary(
        available_time=6,
        budget=100,
        interests=["Temple"]
    )

    print("Optimized Itinerary:")

    total_time = 0
    total_cost = 0

    for place in result:

        print("-", place)

        total_time += places[place]["visit_time"]
        total_cost += places[place]["cost"]

    print("Total Time:", total_time, "hours")
    print("Total Cost: ₹", total_cost)
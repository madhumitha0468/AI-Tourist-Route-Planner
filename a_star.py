import heapq
from places import places, heuristics


def a_star_route(start, destination):

    priority_queue = []

    # (f_cost, g_cost, current_place, path)
    heapq.heappush(
        priority_queue,
        (0, 0, start, [start])
    )

    visited = set()

    while priority_queue:

        f_cost, g_cost, current, path = heapq.heappop(
            priority_queue
        )

        if current == destination:
            return path, g_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbour, distance in places[current]["nearby"].items():

            if neighbour in visited:
                continue

            new_g_cost = g_cost + distance

            h_cost = heuristics.get(
                neighbour, {}
            ).get(destination, 0)

            new_f_cost = new_g_cost + h_cost

            new_path = path + [neighbour]

            heapq.heappush(
                priority_queue,
                (
                    new_f_cost,
                    new_g_cost,
                    neighbour,
                    new_path
                )
            )

    return None, None


# Test A* algorithm
if __name__ == "__main__":

    route, distance = a_star_route(
        "Meenakshi Temple",
        "Gandhi Memorial Museum"
    )

    print("A* Route:")

    if route:
        print(" → ".join(route))
        print("Total Distance:", distance, "km")
    else:
        print("No route found.")
import heapq

roads = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)]
}


def dijkstra(roads, start, destination):
    # Step 1: Initialise distances
    distances = {}

    for location in roads:
        distances[location] = float("inf")

    distances[start] = 0

    # Step 2: Remember the previous location
    previous = {}

    # Step 3: Create a priority queue
    queue = [(0, start)]

    while queue:
        # Get the location with the smallest known distance
        current_distance, current = heapq.heappop(queue)

        # Skip outdated entries
        if current_distance > distances[current]:
            continue

        # We have found the shortest distance to the destination
        if current == destination:
            break

        # Step 4: Examine neighbouring locations
        for neighbour, travel_time in roads[current]:

            new_distance = current_distance + travel_time

            # Step 5: Update if we found a shorter route
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

                previous[neighbour] = current

                heapq.heappush(
                    queue,
                    (new_distance, neighbour)
                )

    # Step 6: Check whether the destination is reachable
    if distances[destination] == float("inf"):
        return None, []

    # Step 7: Reconstruct the route
    route = []
    current = destination

    while current != start:
        route.append(current)
        current = previous[current]

    route.append(start)
    route.reverse()

    return distances[destination], route


# Test the program
travel_time, route = dijkstra(roads, "A", "E")

print("Shortest travel time:", travel_time, "minutes")
print("Shortest route:", " -> ".join(route))

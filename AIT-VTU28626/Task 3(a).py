import heapq

# Road network graph
graph = {
    'Hospital': [('Junction A', 4), ('Junction B', 3)],
    'Junction A': [('Residential Area', 5)],
    'Junction B': [('Traffic Signal', 2)],
    'Traffic Signal': [('Residential Area', 3)],
    'Residential Area': [('Emergency Location', 2)],
    'Emergency Location': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'Hospital': 8,
    'Junction A': 6,
    'Junction B': 5,
    'Traffic Signal': 3,
    'Residential Area': 2,
    'Emergency Location': 0
}

# A* Algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        # Goal reached
        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, None


# Run the algorithm
path, distance = a_star("Hospital", "Emergency Location")

print("Optimal Ambulance Route:")
print(" -> ".join(path))
print("Total Distance:", distance, "km")

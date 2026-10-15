import random

# Locations
locations = ["Hotel", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]

# Distance matrix
DIST = [
    [0, 4, 8, 6, 7, 3, 5, 9, 4],
    [4, 0, 5, 7, 6, 8, 4, 5, 7],
    [8, 5, 0, 4, 5, 7, 6, 3, 8],
    [6, 7, 4, 0, 3, 5, 8, 6, 4],
    [7, 6, 5, 3, 0, 4, 7, 5, 6],
    [3, 8, 7, 5, 4, 0, 6, 8, 5],
    [5, 4, 6, 8, 7, 6, 0, 4, 3],
    [9, 5, 3, 6, 5, 8, 4, 0, 7],
    [4, 7, 8, 4, 6, 5, 3, 7, 0]
]

# Function to calculate total distance
def calculate_distance(route):
    total = DIST[0][route[0]]  # Hotel to first location

    for i in range(len(route) - 1):
        total += DIST[route[i]][route[i + 1]]

    total += DIST[route[-1]][0]  # Last location back to Hotel
    return total


# Generate initial random route
def generate_route():
    route = list(range(1, 9))
    random.shuffle(route)
    return route


# Hill Climbing Algorithm
def hill_climbing():
    current = generate_route()
    current_distance = calculate_distance(current)

    while True:
        best = current[:]
        best_distance = current_distance

        # Try all possible swaps
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                new_route = current[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]

                new_distance = calculate_distance(new_route)

                if new_distance < best_distance:
                    best = new_route
                    best_distance = new_distance

        # Stop if no improvement
        if best_distance == current_distance:
            break

        current = best
        current_distance = best_distance

    return current


# Run program
initial_route = generate_route()
optimized_route = hill_climbing()

print("Initial Route:", "Hotel ->", " -> ".join(locations[i] for i in initial_route), "-> Hotel")
print("Initial Distance:", calculate_distance(initial_route))

print("\nOptimized Route:", "Hotel ->", " -> ".join(locations[i] for i in optimized_route), "-> Hotel")
print("Minimum Distance:", calculate_distance(optimized_route))

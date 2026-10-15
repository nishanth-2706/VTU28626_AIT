import random

# Input
n = int(input("Enter number of locations (including restaurant): "))

print("Enter distance matrix:")
dist = []
for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

# Initialize pheromone
pheromone = [[1 for _ in range(n)] for _ in range(n)]

alpha = 1
beta = 2
evaporation = 0.5
ants = 5
iterations = 20

# Function to calculate distance
def route_length(route):
    total = 0
    for i in range(len(route)-1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]
    return total

best_route = None
best_distance = float('inf')

for _ in range(iterations):
    routes = []

    for _ in range(ants):
        route = [0]

        while len(route) < n:
            current = route[-1]
            probs = []

            for j in range(n):
                if j not in route:
                    p = (pheromone[current][j] ** alpha) * ((1 / dist[current][j]) ** beta)
                else:
                    p = 0
                probs.append(p)

            total = sum(probs)
            probs = [p / total for p in probs]

            next_city = random.choices(range(n), weights=probs)[0]
            route.append(next_city)

        routes.append(route)

    for r in routes:
        d = route_length(r)
        if d < best_distance:
            best_distance = d
            best_route = r

    # Evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)

    # Add pheromone
    for r in routes:
        d = route_length(r)
        for i in range(len(r)-1):
            pheromone[r[i]][r[i+1]] += 1 / d

# Output
print("\nBest Route:", best_route)
print("Minimum Distance:", best_distance)

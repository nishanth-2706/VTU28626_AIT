class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Check if assigning color c to vertex v is safe
    def is_safe(self, v, color, c):
        for i in range(self.v):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    # Backtracking function
    def solve_util(self, m, color, v):
        if v == self.v:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c

                if self.solve_util(m, color, v + 1):
                    return True

                # Backtracking
                color[v] = 0

        return False

    # Main function
    def graph_coloring(self, m):
        color = [0] * self.v

        if not self.solve_util(m, color, 0):
            print("No solution exists")
            return False

        print("\nSolution exists. Assigned colors:")
        for i in range(self.v):
            print(f"Building {i+1} -> Color {color[i]}")
        return True


# ----------- INPUT SECTION -----------

v = int(input("Enter number of buildings: "))
g = Graph(v)

print("Enter adjacency matrix:")
for i in range(v):
    g.graph[i] = list(map(int, input().split()))

m = int(input("Enter number of colors: "))

# ----------- OUTPUT SECTION -----------

g.graph_coloring(m)

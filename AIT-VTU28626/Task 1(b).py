# Graph representation
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # to store visited nodes

# DFS function
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")   # print in one line
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver code
print("Following is the Depth-First Search:")
dfs(visited, graph, '5')

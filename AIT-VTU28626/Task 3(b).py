def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()

    g = {}  # store distance from starting node
    parents = {}  # store parents of nodes

    # distance of starting node from itself is zero
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # find node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # if stop node is reached or node not found
        if n == stop_node or n is None or n not in Graph_nodes:
            break

        # check neighbors
        for (m, weight) in get_neighbors(n):

            # if new node, add to open_set
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                # check if better path exists
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # move n from open to closed
        open_set.remove(n)
        closed_set.add(n)

    # if path not found
    if n is None:
        print('Path does not exist!')
        return None

    # reconstruct path
    if n == stop_node:
        path = []

        while parents[n] != n:
            path.append(n)
            n = parents[n]

        path.append(start_node)
        path.reverse()

        print('Path found:', path)
        return path

    print('Path does not exist!')
    return None


# function to return neighbors
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None


# heuristic values
def heuristic(n):
    h_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return h_dist[n]


# graph definition
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

print("Following is the A* Algorithm:")
aStarAlgo('A', 'G')

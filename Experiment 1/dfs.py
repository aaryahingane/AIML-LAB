# Create a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# DFS function
def dfs(graph, node, visited):
    # Check if node is already visited
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        # Visit all neighbouring nodes
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Create visited list
visited = []

print("DFS Traversal:")

# Start DFS from node A
dfs(graph, 'A', visited)

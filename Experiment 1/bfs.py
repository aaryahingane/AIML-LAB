from collections import deque

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

# BFS function
def bfs(graph, start):
    visited = []
    queue = deque()

    # Add starting node
    queue.append(start)
    visited.append(start)

    print("BFS Traversal:")

    while queue:
        # Remove first node from queue
        node = queue.popleft()
        print(node, end=" ")

        # Visit neighbouring nodes
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Starting node
start = 'A'

# Call BFS
bfs(graph, start)

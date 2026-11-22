graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_list = [start]
    cost = {start: 0}
    parent = {}

    while open_list:
        current = min(open_list, key=lambda n: cost[n] + heuristic[n])
        open_list.remove(current)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()

            print("Path:", path)
            print("Total Cost:", cost[goal])
            return

        for neighbour, weight in graph[current]:
            new_cost = cost[current] + weight

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current

                if neighbour not in open_list:
                    open_list.append(neighbour)

astar('A', 'G')

from collections import deque

# City map represented as a graph
city_map = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}

def bfs(start, goal):
    queue = deque([[start]])   # store paths
    visited = []

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return path

        if city not in visited:
            visited.append(city)

            for neighbor in city_map[city]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return "No Path Found"

# Test
print("Path from A to E:", bfs('A', 'E'))

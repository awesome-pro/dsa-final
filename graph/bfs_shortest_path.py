
from collections import deque

from graph.breadth_first_search import GraphList


def bfs_shortest_pat(graph, start, target):
    """
    Find shortest path from start to target using BFS
    Returns path and distance
    """
    if start == target:
        return [start], 0

    # Keep track of visited vertices
    visited = set()
    # Initialize queue with starting vertex
    queue  = deque([(start, [start], 0)]) # (vertex, path, distance)

    while queue:
        # Get the next vertex from the queue
        vertex, path, distance = queue.popleft()

        # If the vertex has not been visited, add it to the result
        if vertex not in visited:
            # Add the vertex to the visited set
            visited.add(vertex)

            # If the vertex is the target, return the path and distance
            if vertex == target:
                return path, distance

            # Add all unvisited neighbors to the queue
            for neighbour, _ in graph.get_neighbors(vertex):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour], distance + 1))

    # If no path is found, return None
    return None, -1

# Example usage
graph = GraphList()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
print(bfs_shortest_pat(graph, 0, 3))
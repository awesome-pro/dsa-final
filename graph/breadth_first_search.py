# Breadth First Search (BFS)

# BFS is a graph traversal algorithm that starts at the root node and explores all the nodes at the current level before moving on to the nodes at the next level.


from collections import defaultdict, deque

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        """Add edge from u to v with optional weight"""
        self.graph[u].append((v, weight))
        # For undirected graph, add reverse edge
        # self.graph[v].append((u, weight))
    
    def get_neighbors(self, u):
        """Get all neighbors of vertex u"""
        return self.graph[u]
    
    def has_edge(self, u, v):
        """Check if edge exists from u to v"""
        return any(neighbor[0] == v for neighbor in self.graph[u])
    
    def get_vertices(self):
        """Get all vertices in the graph"""
        vertices = set()
        for u in self.graph:
            vertices.add(u)
            for v, _ in self.graph[u]:
                vertices.add(v)
        return list(vertices)
    
    def display(self):
        """Display the adjacency list"""
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
graph = GraphList()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.display()


def bfs(graph, start):
    # Keep track of visited vertices
    visited = set()
    # Initialize queue with starting vertex
    queue = deque([start])
    # Keep track of visited vertices
    result = []
    # Process vertices in the queue
    while queue:
        # Get the next vertex from the queue
        vertex = queue.popleft()
        # If the vertex has not been visited, add it to the result
        if vertex not in visited:
            # Add the vertex to the visited set
            visited.add(vertex)
            # Add the vertex to the result
            result.append(vertex)

            # Add all unvisited neighbors to the queue
            for neighbour, _ in graph.get_neighbors(vertex):
                if neighbour not in visited:
                    queue.append(neighbour)
    return result

print(bfs(graph, 0))
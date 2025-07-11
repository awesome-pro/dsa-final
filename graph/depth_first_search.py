# Depth First Search (DFS)

class GraphList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # Ensure destination vertex exists in graph
        self.graph[u].append((v, weight))

    def get_neighbors(self, u):
        return self.graph.get(u, [])  # Return empty list if vertex doesn't exist
    
    def has_edge(self, u, v):
        if u not in self.graph:
            return False
        return any(neighbor[0] == v for neighbor in self.graph[u])
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage
graph = GraphList()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.display()


def dfs_iterative(graph, start):
    """Iterative DFS implementation using a stack"""
    visited = set()
    result = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            # Add neighbors in reverse order to maintain left-to-right traversal
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result

# Recursive DFS
def dfs_recursive(graph, start, visited=None, result=None):
    """Recursive DFS implementation"""
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(start)
    result.append(start)
    
    for neighbor, _ in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result

print("DFS Recursive:", dfs_recursive(graph, 0))
print("DFS Iterative:", dfs_iterative(graph, 0))

# Alternative DFS that returns the path
def dfs_path(graph, start, target):
    """DFS to find a path from start to target"""
    visited = set()
    path = []
    
    def dfs_helper(current):
        if current in visited:
            return False
        
        visited.add(current)
        path.append(current)
        
        if current == target:
            return True
        
        for neighbor, _ in graph.get_neighbors(current):
            if dfs_helper(neighbor):
                return True
        
        path.pop()  # Backtrack
        return False
    
    if dfs_helper(start):
        return path
    return None

print("Path from 0 to 3:", dfs_path(graph, 0, 3))
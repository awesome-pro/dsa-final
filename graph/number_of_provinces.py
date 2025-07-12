# Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Example 3:
# Input: isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# Output: 1
# Example 4:


from typing import List


# Time Complexity: O(n^2) - we visit each city and each neighbour
# Space Complexity: O(n) - we use a visited array to keep track of visited cities and a stack to keep track of the cities to visit
def find_circle_num_dfs(is_connected: List[List[int]]) -> int:
    n: int = len(is_connected)
    visited: List[bool] = [False] * n
    provinces: int = 0

    def dfs(city: int) -> None:
        visited[city] = True

        for neighbour in range(n):
            if is_connected[city][neighbour] == 1 and not visited[neighbour]:
                dfs(neighbour)

        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            provinces += 1

    return provinces


# Test Cases
print(find_circle_num_dfs([[1,1,0],[1,1,0],[0,0,1]])) # 2
print(find_circle_num_dfs([[1,0,0],[0,1,0],[0,0,1]])) # 3
print(find_circle_num_dfs([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])) # 1

# Approach 2: BFS
# Time Complexity: O(n^2) - we visit each city and each neighbour
# Space Complexity: O(n) - we use a visited array to keep track of visited cities and a queue to keep track of the cities to visit
def find_circle_num_bfs(is_connected: List[List[int]]) -> int:
    n: int = len(is_connected)
    visited: List[bool] = [False] * n
    provinces: int = 0


    def bfs(city: int) -> None:
        queue: List[int] = [city]
        visited[city] = True
        
        while queue:
            current_city: int = queue.pop(0)

            for neighbour in range(n):
                if is_connected[current_city][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            provinces += 1
    
    return provinces




    
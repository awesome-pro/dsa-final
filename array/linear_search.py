# Linear Search

# Time complexity: O(n)
# Space complexity: O(1)
def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test cases
print(linear_search([1, 2, 3, 4, 5], 3)) # Output: 2
print(linear_search([1, 2, 3, 4, 5], 6)) # Output: -1

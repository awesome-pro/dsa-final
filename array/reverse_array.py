# Reverse an Array

from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_array(arr: List[int]) -> List[int]:
    return arr[::-1]

# print(reverse_array([1, 2, 3, 4, 5]))

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_array_recursive(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    return [arr[-1]] + reverse_array_recursive(arr[:-1])

print(reverse_array_recursive([1, 2, 3, 4, 5]))
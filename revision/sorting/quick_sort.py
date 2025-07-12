# Quick Sort

from typing import List


# Time Complexity: O(n log n)
# Space Complexity: O(n)
def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5, 4, 3, 2, 1]))
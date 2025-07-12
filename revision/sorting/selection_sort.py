# Selection Sort

from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 4, 3, 2, 1]))
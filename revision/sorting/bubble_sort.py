# Bubble sort

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 12, 3, 22, 1]))
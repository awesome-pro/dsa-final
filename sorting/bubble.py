# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# the approach is to sort the array by repeatedly swapping the adjacent elements if they are in wrong order

def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 25, 210, 22, 11]))
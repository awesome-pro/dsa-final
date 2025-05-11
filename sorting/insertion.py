# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# the approach is to sort the array by repeatedly swapping the adjacent elements if they are in wrong order
# we start from the second element and compare it with the first element
# if the second element is smaller than the first element, we swap them
# we repeat the process for the remaining array


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))
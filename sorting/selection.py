# Selection Sort - in this we find the minimum element and place it at the beginning
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# the approach is to find the minimum element and place it at the beginning
# we start from the first element and find the minimum element in the remaining array
# we swap the minimum element with the first element
# we repeat the process for the remaining array

def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))

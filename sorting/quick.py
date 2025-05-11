# Quick Sort
# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# the approach is to choose the pivot element and partition the array into two halves
# we start from the first element and partition the array into two halves
# we repeat the process for the remaining array
# we merge the two halves


def quick_sort(arr: list[int]) -> list[int]:
    if(len(arr) <= 1):
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort(arr))
# Recursive Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# the approach is to use recursion to sort the array
# we start from the first element and compare it with the next element
# if the first element is greater than the next element, we swap them
# we repeat the process for the remaining array
# we merge the two halves


def bubble_sort_recursive(arr: list[int], n: int) -> list[int]:
    if(n == 1):
        return arr
    for i in range(n-1):
        if(arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble_sort_recursive(arr, n-1)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_recursive(arr, len(arr))
    print("Sorted array is:", arr)
    
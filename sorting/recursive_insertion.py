# Recursive Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def insertion_sort_recursive(arr: list[int], i: int, n: int) -> list[int]:
    if i == n:
        return arr
    j = i
    while j > 0 and arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
    return insertion_sort_recursive(arr, i+1, n)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort_recursive(arr, 0, len(arr))
    print(arr)
# Remove Duplicates from Sorted Array, ensuring the elements in the relative order in result array

# Approach 1: Brute Force
def remove_duplicates_from_sorted_array(arr: list[int]) -> int:
    if not arr:
        return 0
    i = 1
    for j in range(1, len(arr)):
        if(arr[j] != arr[j-1]):
            arr[i] = arr[j]
            i += 1
    return i
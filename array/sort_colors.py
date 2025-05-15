# Sort Colors

# Approach 1: Counting Sort
# Time complexity: O(n)
# Space complexity: O(1)
def sort_colors(arr: list[int]) -> list[int]:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
    arr[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
    return arr

# Approach 2: Dutch National Flag Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
def sort_colors_2(arr: list[int]) -> list[int]:
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# Approach 3: Using Extra Array
# Time complexity: O(n)
# Space complexity: O(1)
def sort_colors_3(arr: list[int]) -> list[int]:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
    arr[:count_0] = [0] * count_0
    arr[count_0:count_0 + count_1] = [1] * count_1
    arr[count_0 + count_1:] = [2] * count_2
    return arr


# Approach 4: Using Sorting
# Time complexity: O(n log n)
# Space complexity: O(1)
def sort_colors_4(arr: list[int]) -> list[int]:
    arr.sort()
    return arr

# Approach 5: Using Counting Sort
# Time complexity: O(n)
# Space complexity: O(1)
def sort_colors_5(arr: list[int]) -> list[int]:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
    arr[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
    return arr



# Test cases
print(sort_colors([2, 0, 2, 1, 1, 0])) # Output: [0, 0, 1, 1, 2, 2]
# print(sort_colors_2([2, 0, 2, 1, 1, 0])) # Output: [0, 0, 1, 1, 2, 2]
# print(sort_colors_3([2, 0, 2, 1, 1, 0])) # Output: [0, 0, 1, 1, 2, 2]
# print(sort_colors_4([2, 0, 2, 1, 1, 0])) # Output: [0, 0, 1, 1, 2, 2]
# print(sort_colors_5([2, 0, 2, 1, 1, 0])) # Output: [0, 0, 1, 1, 2, 2]




            
            
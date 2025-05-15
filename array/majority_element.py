# Majority Element

# Approach 1: Brute Force
# Time complexity: O(n^2)
# Space complexity: O(1)
def majority_element(arr: list[int]) -> int:
    n = len(arr)
    for i in range(n):
        count: int = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n/2:
            return arr[i]
    return -1

# Approach 2: Using Hash Map
# Time complexity: O(n) 
# Space complexity: O(n)
def majority_element_hash_map(arr: list[int]) -> int:
    count_map = {}
    n = len(arr)
    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        if count_map[num] > n/2:
            return num
    return -1

# Approach 3: Using Sorting
# Time complexity: O(n log n)
# Space complexity: O(1)
def majority_element_sorting(arr: list[int]) -> int:
    arr.sort()
    return arr[len(arr)//2]


# Approach 4: Using Moore's Voting Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
def majority_element_moore(arr: list[int]) -> int:
    count: int = 0
    candidate: int = None
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

# Approach 5: Using Hash Map
# Time complexity: O(n)
# Space complexity: O(n)
def majority_element_hash_map(arr: list[int]) -> int:
    count_map = {}
    n = len(arr)
    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        if count_map[num] > n/2:
            return num
    return -1
            
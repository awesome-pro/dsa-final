# Left Rotate Array by K Places

# Approach 1: Brute Force
# Time complexity: O(n * k)
# Space complexity: O(1)
def left_rotate_by_k_places(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last
    return arr


# Approach 2: Using Extra Array
# Time complexity: O(n)
# Space complexity: O(n)
def left_rotate_by_k_places_2(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    arr[:] = arr[k:] + arr[:k]
    return arr

# Test cases
print(left_rotate_by_k_places([1, 2, 3, 4, 5], 2)) # Output: [3, 4, 5, 1, 2]
print(left_rotate_by_k_places([1, 2, 3, 4, 5], 1)) # Output: [2, 3, 4, 5, 1]


# Approach 2: Using Extra Array
# Time complexity: O(n)
# Space complexity: O(n)
def left_rotate_by_k_places_extra_array(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    temp = [0] * n
    for i in range(n):
        temp[(i - k) % n] = arr[i]
    return temp



# Approach 3: Reversing the Array
# Time complexity: O(n)
# Space complexity: O(1)
def left_rotate_by_k_places_reversing(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    arr[:] = arr[k:] + arr[:k]
    return arr

# Approach 4: Using Cyclic Replacements
# Time complexity: O(n)
# Space complexity: O(1)
def left_rotate_by_k_reverse(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    return arr
    
    
    
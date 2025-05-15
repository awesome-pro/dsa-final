# Maximum Subarray

# Approach 1: Brute Force
# Time complexity: O(n^3)
# Space complexity: O(1)
def maximum_subarray(arr: list[int]) -> int:
    max_sum: int = float('-inf')
    n: int = len(arr)
    for i in range(n):
        for j in range(i, n):
            current_sum: int = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)
    return max_sum

# Approach 2: Kadane's Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
def maximum_subarray_kadane(arr: list[int]) -> int:
    max_sum: int = float('-inf')
    current_sum: int = 0
    n: int = len(arr)
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

# Approach 3: Using Prefix Sum
# Time complexity: O(n^2)
# Space complexity: O(n)
def maximum_subarray_prefix_sum(arr: list[int]) -> int:
    n: int = len(arr)
    prefix_sum: list[int] = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    max_sum: int = float('-inf')
    for i in range(n):
        for j in range(i, n):
            current_sum: int = prefix_sum[j] - prefix_sum[i] + arr[i]
            max_sum = max(max_sum, current_sum)
    return max_sum

# Approach 4: Using Divide and Conquer
# Time complexity: O(n log n)
# Space complexity: O(log n)
def maximum_subarray_divide_and_conquer(arr: list[int]) -> int:
    def find_max_crossing_subarray(arr: list[int], low: int, mid: int, high: int) -> int:
        left_sum: int = float('-inf')
        current_sum: int = 0
        for i in range(mid, low-1, -1):
            current_sum += arr[i]
            if current_sum > left_sum:
                left_sum = current_sum
                max_left = i
        right_sum: int = float('-inf')
        current_sum = 0
        for i in range(mid+1, high+1):
            current_sum += arr[i]
            if current_sum > right_sum:
                right_sum = current_sum
                max_right = i
        return max_left, max_right, left_sum + right_sum
    
    
    
# Test cases
print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
print(maximum_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
print(maximum_subarray_prefix_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
print(maximum_subarray_divide_and_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6

    


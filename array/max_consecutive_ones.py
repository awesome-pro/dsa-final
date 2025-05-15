# Max Consecutive Ones

# Approach 1: Using two pointers
# Time complexity: O(n)
# Space complexity: O(1)
def max_consecutive_ones(arr: list[int]) -> int:
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)

# Test cases
print(max_consecutive_ones([1, 1, 0, 1, 1, 1])) # Output: 3
print(max_consecutive_ones([1, 0, 1, 1, 0, 1])) # Output: 2

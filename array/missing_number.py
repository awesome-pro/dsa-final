# Missing Number

# Approach 1: Using sum
# Time complexity: O(n)
# Space complexity: O(1)
def missing_number(arr: list[int]) -> int:
    n = len(arr)
    total = n * (n + 1) // 2
    return total - sum(arr)

# Approach 2: Using XOR
# Time complexity: O(n)
# Space complexity: O(1)
def missing_number_xor(arr: list[int]) -> int:
    xor = 0
    for num in arr:
        xor ^= num
    for i in range(1, len(arr) + 1):
        xor ^= i    
    return xor

# Test cases
print(missing_number([0, 2, 3, 1, 5])) # Output: 6
print(missing_number_xor([0, 2, 3, 1, 5])) # Output: 6


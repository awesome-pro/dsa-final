# Single Number

# Approach 1: Using XOR
# Time complexity: O(n)
# Space complexity: O(1)
def single_number(arr: list[int]) -> int:
    xor = 0
    for num in arr:
        xor ^= num
    return xor

# Test cases
print(single_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 11


# Approach 2: Using Map
# Time complexity: O(n)
# Space complexity: O(n)
def single_number_map(arr: list[int]) -> int:
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            return num
    return -1
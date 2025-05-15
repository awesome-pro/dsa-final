# Time complexity: O(n)
# Space complexity: O(n)
def moveZeroes1(nums: list[int]) -> list[int]:
    
    n = len(nums)
    
    
    # Count zeros
    zero_count = 0
    
    # First pass: Count zeros and move non-zero elements
    for i in range(n):
        if nums[i] == 0:
            zero_count += 1

    # Make all the non-zero elements retain their original order.      
    new_nums = []
    for num in nums:
        if num != 0:
            new_nums.append(num)

    # Move all zeros to the end
    for _ in range(zero_count):
        new_nums.append(0)

    # Copy the result back to the original list
    for i in range(n):
        nums[i] = new_nums[i]

    return nums



# Approach 2: Two pointers
# Time complexity: O(n)
# Space complexity: O(1)
def moveZeroes(nums: list[int]) -> list[int]:
    n = len(nums)
    last_non_zero_found_at = 0
    
    # If the current element is not 0, then we need to
    # append it just in front of the last non 0 element we found.
    for i in range(n):
        if nums[i] != 0:
            nums[last_non_zero_found_at] = nums[i]
            last_non_zero_found_at += 1
            
    # After we have finished processing new elements,
    # all the non-zero elements are already at beginning of array.
    # We just need to append the remaining zeros to the end of array.
    for i in range(last_non_zero_found_at, n):
        nums[i] = 0

    return nums

# Approach 3: 
def moveZeroes2(nums: list[int]) -> list[int]:
    # Initialize pointer for next non-zero element position
    last_non_zero_found_at = 0
    
    # Move all non-zero elements to the front
    for cur in range(len(nums)):
        if nums[cur] != 0:
            nums[last_non_zero_found_at], nums[cur] = nums[cur], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

    return nums

# Test cases
print(moveZeroes2([0, 1, 0, 3, 12])) # Output: [1, 3, 12, 0, 0]
print(moveZeroes2([0])) # Output: [0]
print(moveZeroes2([1, 2, 0, 4, 0, 0, 5, 6, 7, 0, 8, 9, 10])) # Output: [1, 2, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0]


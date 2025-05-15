# Union of two arrays

# Approach 1: Using set
# Time complexity: O(n + m)
# Space complexity: O(n + m)
def union1(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1 + arr2))


def union(arr1: list[int], arr2: list[int]) -> list[int]:
   freq = {}    
   union = []
   
   for num in arr1:
      freq[num] = freq.get(num, 0) + 1
   
   for num in arr2:
          freq[num] = freq.get(num, 0) + 1
   
   for num in freq:
      union.append(num)
   return union

# Test cases
print(union([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(union([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # Output: [1, 2, 3, 4, 5]
print(union([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


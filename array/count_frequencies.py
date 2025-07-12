# Count Frequencies of each element in an array

from typing import List, Dict

# Time Complexity: O(n)
# Space Complexity: O(n)
def count_frequencies(arr: List[int]) -> Dict[int, int]:
    frequencies: Dict[int, int] = {}
    for num in arr:
        frequencies[num] = frequencies.get(num, 0) + 1
    return frequencies

# print(count_frequencies([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# Time Complexity: O(n)
# Space Complexity: O(n)
def count_frequencies_using_hash_table(arr: List[int]) -> Dict[int, int]:
    frequencies: Dict[int, int] = {}
    for num in arr:
        frequencies[num] = frequencies.get(num, 0) + 1
    return frequencies

# print(count_frequencies_using_hash_table([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

def find_highest_frequency(arr: List[int]) -> int:
    frequencies: Dict[int, int] = {}
    for num in arr:
        frequencies[num] = frequencies.get(num, 0) + 1
    return max(frequencies, key=frequencies.get)
    # max_frequency = max(frequencies.values())
    # for num, frequency in frequencies.items():
    #     if frequency == max_frequency:
    #         return num
    # return -1

print(find_highest_frequency([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 25, 2, 2, 2, 2]))

# Time Complexity: O(n)
# Space Complexity: O(n)
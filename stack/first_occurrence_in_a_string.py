# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Approach 1: Brute Force
# Time Complexity: O(n * m)
# Space Complexity: O(1)

# Approach 2: Rabin-Karp Algorithm
# Time Complexity: O(n + m)
# Space Complexity: O(1)

# Approach 3: Knuth-Morris-Pratt Algorithm
# Time Complexity: O(n + m)
# Space Complexity: O(1)


# This is the brute force approach
def first_occurrence(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1   

# This is the Rabin-Karp algorithm
def first_occurrence_rabin_karp(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# This is the Knuth-Morris-Pratt algorithm
def first_occurrence_knuth_morris_pratt(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    lps = [0] * len(needle)
    i = 1
    j = 0
    while i < len(needle):
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    i = 0
    j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(needle):
            return i - j
    return -1

# This is the Boyer-Moore algorithm
def first_occurrence_boyer_moore(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    return -1

# This is the Sunday algorithm
print(first_occurrence("hello", "ll")) # 2
print(first_occurrence("hello", "lo")) # 3
print(first_occurrence("hello", "")) # 0
print(first_occurrence("hello", "hello")) # 0
print(first_occurrence("hello", "world")) # -1
print(first_occurrence("hello", "hello")) # 0
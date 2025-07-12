# Pallindrome String

def is_pallindrome(s: str) -> bool:
    return s == s[::-1]

# Time Complexity: O(n)
# Space Complexity: O(1)
print(is_pallindrome("racecar"))
print(is_pallindrome("hello"))

# Time Complexity: O(n)
# Space Complexity: O(n)
def is_pallindrome_recursive(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    return s[0] == s[-1] and is_pallindrome_recursive(s[1:-1])

# print(is_pallindrome_recursive("racecar"))
# print(is_pallindrome_recursive("hello"))
# GCD of two numbers

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(12, 18))

# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(log(min(a, b)))
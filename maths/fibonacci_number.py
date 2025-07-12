# Fibonacci Number

# Time Complexity: O(2^n)
# Space Complexity: O(n)
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))
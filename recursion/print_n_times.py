
def print_n_times(num:int, n:int):
    if n <= 0:
        return
    
    print("num:", num)
    print_n_times(num, n-1)

# print_n_times(123, 7)

def print_from_1_to_n(n:int):
    if n <= 0:
        return
    
    print_from_1_to_n(n-1)
    print("n:", n)

# print_from_1_to_n(7)

def sum_n(n: int):
    if n <= 1:
        return n
    return n + sum_n(n-1)

# print("sum upto n: ", sum_n(12))

def factorial_n(n: int):
    if n <= 1:
        return 1
    
    return n * factorial_n(n-1)

print("factorial of n: ", factorial_n(10))
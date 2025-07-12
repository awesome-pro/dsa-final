# print all divisors of a number
def print_divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i, end=" ")
print_divisors(100)

# count digits in a number
def count_digits(n):
    count = 0
    while n>0:
        count += 1
        n = n//10
    return count
print(count_digits(12345))

# reverse a number
def reverse_number(n):
    rev = 0
    while n>0:
        rev = rev*10 + n%10
        n = n//10
    return rev
print(reverse_number(12345))

# check if a number is prime
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(11))
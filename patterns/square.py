# Print the square pattern
# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()


def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print("$", end=" ")
        print()
print_hollow_square(9)

# for i in range(6):
#     for j in range(i+1):
#         print(j, end=" ")
#     print()

# inverted right angle triangle
# for i in range(6):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# inverted right angle triangle
# for i in range(6):
#     for j in range(6-i):
#         print("*", end=" ")
#     print()

# 
# for i in range(6):
#     for j in range(6):
#         if i==0 or i==5 or j==0 or j==5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# def print_isosceles_triangle(n):
#     for i in range(n):
#         for _ in range(n-i-1):
#             print(" ", end=" ")
#         for _ in range(2*i+1):
#             print("*", end=" ")
#         print()

# print_isosceles_triangle(5)

# def print_inverted_isosceles_triangle(n):
#     for i in range(n):
#         for _ in range(i):
#             print(" ", end=" ")
#         for _ in range(2*(n-i)-1):
#             print("*", end=" ")
#         print()

# print_inverted_isosceles_triangle(5)


# print diamond pattern
def print_diamond_pattern(n):
    for i in range(n):
        for _ in range(n-i-1):
            print("*", end=" ")
        for _ in range(2*i+1):
            print("-", end=" ")
        print()
    for i in range(n-1,0,-1):
        for _ in range(n-i):
            print("*", end=" ")
        for _ in range(2*i-1):
            print("-", end=" ")
        print()

# print_diamond_pattern(5)
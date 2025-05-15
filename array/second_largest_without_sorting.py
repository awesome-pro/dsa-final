# Second largest element in Array without sorting

# Approach 1: Brute Force
def second_largest_brute(arr: list[int]) -> int:
    largest = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > largest):
            largest = arr[i]
    second_largest = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > second_largest and arr[i] != largest):
            second_largest = arr[i]
    return second_largest

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(second_largest_brute(arr))    


# Approach 2: Better Approach
def second_largest_better(arr: list[int]) -> int:
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(1, len(arr)):
        if(arr[i] > largest):
            second_largest = largest
            largest = arr[i]
        elif(arr[i] < largest and arr[i] > second_largest):
            second_largest = arr[i]
    return second_largest

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(second_largest_better(arr))

# Approach 3: Optimal Approach
def second_largest_optimal(arr: list[int]) -> int:
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(1, len(arr)):
        if(arr[i] > largest):
            second_largest = largest
            largest = arr[i]
        elif(arr[i] < largest and arr[i] > second_largest):
            second_largest = arr[i]
    return second_largest
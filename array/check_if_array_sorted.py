# Check if Array is originally sorted

# Approach 1: Brute Force
def check_if_array_sorted(arr: list[int]) -> bool:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] > arr[j]):
                return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(check_if_array_sorted(arr))


# Approach 2: Better Approach
def check_if_array_sorted_better(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if(arr[i] < arr[i-1]):
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(check_if_array_sorted_better(arr))
    
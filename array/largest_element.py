# Larget Element in an Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# the approach is to use a loop to find the largest element in the array
# we start from the first element and compare it with the next element
# if the first element is greater than the next element, we swap them
# we repeat the process for the remaining array
# we merge the two halves


# Approach 1: Linear Search

def largest_element(arr: list[int]) -> int:
    max = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max


# Approach 2: Recursion

def largest_element_recursive(arr: list[int], n: int) -> int:
    if(n == 1):
        return arr[0]
    return max(arr[n-1], largest_element_recursive(arr, n-1))


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(largest_element(arr))
    print(largest_element_recursive(arr, len(arr)))


# Approach 3: Using sort

def largest_element_sort(arr: list[int]) -> int:
    arr.sort()
    return arr[-1]


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(largest_element_sort(arr))


# Approach 4: Using max function

def largest_element_max(arr: list[int]) -> int:
    return max(arr)

# Approach 5: Using sort and max function

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(largest_element_max(arr))
    print(largest_element_sort(arr))

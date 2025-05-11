# Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# the approach is to divide the array into two halves, sort them separately, and then merge them
# we start from the middle of the array and divide it into two halves
# we repeat the process for the remaining array
# we merge the two halves


def merge_sort(arr: list[int]) -> list[int]:
    if(len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(merge_sort([34, 234, 2342, 234234, 1, 25, 12, 22, 11]))
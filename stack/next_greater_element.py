# Next Greater Element

def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

if __name__ == "__main__":
    arr = [1, 3, 2, 4]
    print(next_greater_element(arr))
# Implement Stack using Queue

from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, val: int) -> None:
        self.q1.append(val)

    def pop(self) -> int:
        if not self.q1:
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        if not self.q1:
            return -1
        return self.q1[-1]

    def empty(self) -> bool:
        return not self.q1

if __name__ == "__main__":
    stack = Stack()
    stack.push(1) # 1
    stack.push(2) # 2
    stack.push(3) # 3
    print(stack.pop()) # 3
    print(stack.top()) # 2
    print(stack.empty()) # False
# Valid Parentheses


# Stack Implementation

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def print_stack(self):
        for i in range(len(self.items)):
            print(self.items[i], end=" ")
        print()
    


# Valid Parentheses
def valid_parentheses(s: str) -> bool:
    stack = Stack()
    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            else: 
                top = stack.pop()
                if top == "(" and char == ")":
                    pass
                elif top == "[" and char == "]":
                    pass
                elif top == "{" and char == "}":
                    pass
                else:
                    return False
    return stack.is_empty()


if __name__ == "__main__":
    s = "[{()[]}]"
    print(valid_parentheses(s))

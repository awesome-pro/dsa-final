# Infix to Postfix


def infix_to_postfix(expression: str) -> str:
    precedence = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    right_associative = {"^"}

    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        elif char in precedence:
            while (
                stack
                and stack[-1] != "("
                and (
                    precedence[stack[-1]] >= precedence[char]
                    and char not in right_associative
                )
            ):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append()

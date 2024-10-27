def is_balanced(example):
    bracket = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in example:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket:
            if not stack or stack.pop() != bracket[char]:
                return "Not Balanced"
    
    return "Balanced" if not stack else "Not Balanced"

example1 = "[()]{}{()()}"
example2 = "[(])"

print(f"{example1} -> {is_balanced(example1)}")  
print(f"{example2} -> {is_balanced(example2)}")
print("hello")

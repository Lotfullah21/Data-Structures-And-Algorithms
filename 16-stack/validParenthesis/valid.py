def ispar(x):
    stack = []
    # Dictionary to store mapping of brackets
    mappings = {')': '(', '}': '{', ']': '['}
    
    for char in x:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack or stack[-1] != mappings[char]:
                return False
            stack.pop()
    
    # If the stack is empty, all brackets are balanced
    return len(stack) == 0

# Test the function
if __name__ == "__main__":
    exp1 = "{([])}"
    if ispar(exp1):
        print("balanced")
    else:
        print("not balanced")
    
    exp2 = "()"
    if ispar(exp2):
        print("balanced")
    else:
        print("not balanced")
    
    exp3 = "(["
    if ispar(exp3):
        print("balanced")
    else:
        print("not balanced")

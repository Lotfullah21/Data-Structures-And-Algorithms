def removeAdjacentDuplicate(s: str) ->str:
    "remove two consecutive characters in an a string."
    def peek(s):
        return s[-1]
    stack = []
    for i in range(len(s)):
        if len(stack)==0 or s[i]!=stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    newString = "".join(stack)
    return newString 
result = removeAdjacentDuplicate("abbbccde")
print(result)
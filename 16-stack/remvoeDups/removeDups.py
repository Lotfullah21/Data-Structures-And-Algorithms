def removeConsecutiveDuplicates(s: str) ->str:
    "remove two consecutive characters in an a string."
    def peek(s):
        return s[-1]
    stack = []
    for i in range(len(s)):
        if len(stack)==0 or s[i]!=stack[-1]:
            stack.append(s[i])
        # If top element and the current element is same, remove the similar element from stack.
        else:
            stack.pop()
    newString = "".join(stack)
    return newString 
result = removeConsecutiveDuplicates("aaabbaaccd")
print(result)
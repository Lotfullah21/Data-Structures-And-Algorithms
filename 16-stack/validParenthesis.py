def validParenthesis(s: str) -> bool:
    "to check  a given string is valid parenthesis or not"
    stack = []
    for i in range(len(s)):
        if len(stack)==0 or s[i]=="[" or s[i] == "{" or s[i]=="(":
            stack.append(s[i])
        else:
            if s[i] == ")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif s[i]=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            else:
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
    if len(stack)==0:
        return True
    else:
        return False
    
    
result = validParenthesis("{([])}")
print(result)


class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,s):
        "to check  a given string is valid parenthesis or not"
        stack = []
        for i in range(len(s)):
            if len(stack)==0 or s[i]=="[" or s[i] == "{" or s[i]=="(":
                stack.append(s[i])
            else:
                if s[i] == ")":
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                elif s[i]=="]":
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
solution = Solution()
print(solution.ispar("{}[]}"))
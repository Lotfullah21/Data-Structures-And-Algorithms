def patternMatch(s: str, p: str):
    n = len(s)
    m = len(p)
    for i in range(n):
        flag = True
        for j in range(m):
            if s[i+j]!=p[j]:
                flag = False
                break
        if flag==True:
            return True

    else:
        return False
    # print("Not matching")
    
    
# Test the function
s = "Hello"
p = "ell"
print(patternMatch(s, p))  # Output: True

p = "elo"
print(patternMatch(s, p))  # Output: False
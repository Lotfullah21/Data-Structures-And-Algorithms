def isSubSeq(s1: str, s2: str) -> bool:
    "Returns True if s2 is subsequence of s1"
    if len(s1)<len(s2):
        return False
    i,j = 0,0
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j==len(s2):
        return True
    else:
        return False
    
    
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = isSubSeq(s1, s2)
print(result)
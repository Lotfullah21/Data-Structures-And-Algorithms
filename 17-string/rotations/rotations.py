def isRotations(s1: str, s2: str) -> bool:
    "Returns true if s1 can be obtained by rotating string s2."
    if len(s1)!=len(s2):
        return False
    # S1 is the text we are looking for the pattern.
    s = s1+s1
    # S2 is the pattern we are looking for.
    if s.find(s2)!=-1:
        return True
    
    
    
s1 = "ABCD"
s2 = "CDAB"
result = isRotations(s1, s2)
print(result)
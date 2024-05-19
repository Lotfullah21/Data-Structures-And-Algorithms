def isAnagram(s1: str, s2: str) -> str:
    "Returns True if two strings are anagram of each other."
    if len(s1)!=len(s2):
        return False
    counts = [0]*256
    for i in range(len(s1)):
        counts[ord(s1[i])] +=1
        counts[ord(s2[i])] -=1
    for count in counts:
        if count!=0:
            return False
        return True

result = isAnagram("AABCD","BADCA")
print(result)
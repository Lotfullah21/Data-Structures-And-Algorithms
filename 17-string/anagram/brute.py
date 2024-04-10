class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        "Returns True if two strings are anagram of each other."
        if len(a)!=len(b):
            return False
        l1 = sorted(a)
        l2 = sorted(b)
        if l1==l2:
            return True
        
        
solution = Solution()
result = solution.isAnagram("AABCD","BADCA")
print(result)
class Solution:
    def isPossible(self, S):
        hm = {}
        for c in S:
            if c in hm:
                hm[c]+=1
            if c not in hm:
                hm[c]=1
        odd=0
        for count in hm.values():
            if count%2!=0:
                odd+=1
            if odd>1:
                return True
        return False
    
    
    
solution = Solution()
print(solution.isPossible("civic"))  # Output: 1 (Already a palindrome)
print(solution.isPossible("ivicc"))  # Output: 1 (Can be rearranged to "civic")
print(solution.isPossible("hello"))  # Output: 0 (Cannot be rearranged to a palindrome)
print(solution.isPossible("aabbcc"))  # Output: 1 (Can be rearranged to "abcabc" or "acbbca")

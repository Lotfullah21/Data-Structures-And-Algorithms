class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a, b = {},{}
        for i in range(len(s)):
            a[s[i]] = a.get(s[i],0)+1
        for i in range(len(t)):
            b[t[i]] = b.get(t[i],0)+1
        for i in range(len(s)):
            if a[s[i]]!=b.get(s[i],0):
                return False
        return True
    
solution = Solution()
# Test Case 3: Different Lengths
s3 = "hello"
t3 = "helloo"
print(f"Is '{s3}' an anagram of '{t3}'? {solution.isAnagram(s3, t3)}")  # False

# Test Case 4: Same Letters, Different Counts
s4 = "aabbcc"
t4 = "abc"
print(f"Is '{s4}' an anagram of '{t4}'? {solution.isAnagram(s4, t4)}")  # False
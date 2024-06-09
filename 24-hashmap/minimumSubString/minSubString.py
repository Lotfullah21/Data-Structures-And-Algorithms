class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # Generate two hashmaps to keep the frequency of each character in s and t respectively.
        hms = {}
        hmt = {}
        
        # Add all characters from string t to hmt, the character being the key and its frequency being the value.
        for char in t:
            hmt[char] = hmt.get(char, 0) + 1
        
        ans = float("inf")
        startingIndex = -1
        endingIndex = -1
        startingPoint = 0
        endingPoint = 0
        matchCount = 0
        
        while endingPoint < len(s):
            # Acquire new characters to our substring so that all chars from t are included
            hms[s[endingPoint]] = hms.get(s[endingPoint], 0) + 1
            if hms[s[endingPoint]] <= hmt.get(s[endingPoint], 0):
                matchCount += 1
            endingPoint += 1
            
            # Check if we got all characters from t into our substring.
            while matchCount == len(t):
                if (endingPoint - startingPoint) < ans:
                    ans = endingPoint - startingPoint
                    startingIndex = startingPoint
                    endingIndex = endingPoint
                # Now, release characters to reduce the length of the substring that contains all t.
                hms[s[startingPoint]] -= 1
                if hms[s[startingPoint]] < hmt.get(s[startingPoint], 0):
                    matchCount -= 1
                startingPoint += 1
        
        # No valid window found
        if startingIndex == -1:
            return ""
        
        return s[startingIndex:endingIndex]

# Example usage
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Should print "BANC"
print(sol.minWindow("a", "a"))  # Should print "a"
print(sol.minWindow("a", "aa"))  # Should print ""
print(sol.minWindow("abc", "ac"))  # Should print "abc"
print(sol.minWindow("abc", "ab"))  # Should print "ab"
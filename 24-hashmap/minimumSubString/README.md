## Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

<h2><a href="https://leetcode.com/problems/minimum-window-substring/description/">leetcode-76</a></h2>

```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        # Generate two hashmaps to keep the frequency of each character in s and t respectively.
        hms = {}
        hmt = {}
        # Add all characters from string t to hmt, the character being the key and its frequency being the value.
        for i in range(len(t)):
            hmt[t[i]] = hmt.get(t[i], 0)+1
        ans = float("inf")
        startingIndex = -1
        endingIndex = -1
        startingPoint = 0
        endingPoint = 0
        matchCount = 0
        while(endingPoint<len(s)):
            # Check if we got all characters from t into our substring.
            if matchCount == len(t):
                if (endingPoint-startingPoint)<ans:
                    ans = endingPoint-startingPoint+1
                    startingIndex = startingPoint
                    endingIndex = endingPoint
                    # Now, release characters to reduce the lenght of the substring that contains all t.
                    hms[s[startingPoint]] = hms[s[startingPoint]]-1
                    if hms[s[startingPoint]]<hmt.get(s[startingPoint],0):
                        matchCount-=1
                startingPoint+=1
            # Acquire new characters to our substring so that all chars from t is included
            else:
                hms[s[endingPoint]] = hms.get(s[endingPoint], 0)+1
                if hms[s[endingPoint]]<=hmt.get(s[endingPoint],0):
                    matchCount+=1
                endingPoint+=1

        while matchCount==len(t):
            if endingPoint-startingPoint<ans:
                ans = endingPoint-startingPoint+1
                startingIndex = startingPoint
                endingIndex = endingPoint
            hms[s[startingPoint]] = hms[s[startingPoint]]-1
            if hms[s[startingPoint]]<hmt.get(s[startingPoint],0):
                matchCount-=1
            startingPoint+=1
        print(startingIndex, endingIndex)
        return s[startingIndex:endingIndex+1]


```

## Analysis:

`Time Complexity`: `O(n)+O(m)` where n is length of string s and m is length of string t. Each character in s is processed once when expanding the window and potentially once more when contracting the window, resulting in each character being processed at most twice.
Constructing hmt requires `O(m)` operations.

`Space Complexity`: `O(n)+O(m)` because of constructing hms and hmt.

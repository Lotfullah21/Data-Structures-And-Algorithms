## Is Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
In another words, the length of two strings and frequency of each word should match to consider two strings to be anagram of each other.

a = "ahmad"
b = "hamad"

frequency map in a = {a:2, h:1,m:1, d:1}
frequency map in a = {h:1, a:2, m:1, d:1}
And len(a)==len(b), Hence, they are anagram of each other.

<h2><a href="https://leetcode.com/problems/valid-anagram/description/">leetcode-242</a></a>

## Idea-1:

Create a count frequency for each string, values being as keys and count of them as frequency.

At the end compare if both of the dictionaries are same, if not return false.

```py
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
```

`if a[s[i]]!=b.get(s[i],0):` this point it crucial, if we just compare `if a[s[i]]!=b[s[i]]`, s[i] might not be present in b and that will return `KeyError`.

## Analysis:

`Time Complexity`: `O(len(s)+len(t))`, because we are iterating through end of each string to find their frequency.
`Space Complexity`: `O(len(s)+len(t))`, because we need to save two strings inside a hashmap.

## Idea-2:

Use sorting and compare two string, if they are equal they are anagram of each other.

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
```

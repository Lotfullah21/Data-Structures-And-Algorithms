"""
You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.

Input:
s = Hello world

Output: 
2
"""
class Solution:
    def countWords(self,s: str) -> int:
        s = s.split(" ")
        return len(s)

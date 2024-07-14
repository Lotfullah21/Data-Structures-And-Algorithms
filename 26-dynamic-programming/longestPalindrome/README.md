## Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

<h2><a href="https://leetcode.com/problems/longest-palindromic-subsequence/description/">leetcode-516</a></h2>

## Idea:

Reversal of the String: By reversing the string s to get s1, we convert the problem into finding the longest common subsequence (LCS) between s and s1. This is because a palindrome reads the same forward and backward, so finding the LCS between s and its reverse gives us the longest palindromic subsequence.

If either index i or j is less than 0, it means we've reached the end of one of the strings, so we return 0.
If the characters s[i] and s1[j] match, then this character is part of the palindromic subsequence, so we add 1 and continue to check the next characters (i-1, j-1).
If they do not match, we take the maximum value from either skipping the current character of s or skipping the current character of s1

### Complexity Analysis

`Time Complexity:` O(n*n).
where n is the length of the string. This is because each state (i, j) is computed only once and there are n * n possible states.
`Space Complexity:` O(N\*M).

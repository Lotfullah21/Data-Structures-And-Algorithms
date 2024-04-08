### Subsequence:

A subsequence of a string is a sequence of characters that appears in the same order as they appear in the original string, but not necessarily consecutively

Input: "ABCDE"
Output: "AB", "ADE" are subsequences of input sequence.
But, "ED", "EBC" are not a subsequence.

Number of subsequences of a sequence with length n is `2^n`.

### Idea-1:

Generate all subsequences of a sequence and compare it with the given string, if they are same, then that is a subsequence.

### Idea-2:

Start from left most characters and check if both of the chars match.

If matched, increment both, else, just increment the source string.

At the end, if whole of s2 is processed, it means all matched chars found in s1, hence s2 is a subsequence of s1.

### Analysis:

`Time Complexity`: `O(N+M)`, as we are checking at most either both of them or one of the strings.

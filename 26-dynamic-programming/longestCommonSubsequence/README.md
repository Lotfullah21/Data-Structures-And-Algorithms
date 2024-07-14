## Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

A common subsequence of two strings is a subsequence that is common to both strings.

<h2><a href="https://leetcode.com/problems/longest-common-subsequence/submissions/1319776501/">leetcode-1143</a></h2>

## Idea:

- Sort on the basis of one parameter(width)
- Use longest increasing subsequence on the second parameter (height)

We are guessing on which side is our common subsequence.
If on first sequence, explore that.
If on second Sequence, explore that.
Since we do not know on which side is our most common subsequence, we call it recursively to find out.

### Brute Force

`Time Complexity:` O(N*M).
`Space Complexity:` O(N*M).

Ways to create a 2-D array:

1. Nested List

```py
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)  # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

```

2. Using loops

```py
rows, cols = 3, 4
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    matrix.append(row)
print(matrix)  # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

3. Using List comprehension

```py
rows, cols = 3, 4
matrix = [[0] * cols for _ in range(rows)]
print(matrix)  # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

```

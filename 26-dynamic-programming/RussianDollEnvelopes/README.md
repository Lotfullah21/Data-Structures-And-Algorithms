## Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

<h2><a href="https://leetcode.com/problems/russian-doll-envelopes/description/">leetcode-354</a></h2>

## Idea:

- Sort on the basis of one parameter(width)
- Use longest increasing subsequence on the second parameter (height)

### Brute Force

`Time Complexity:` O(NlogN).
`Space Complexity:` O(N).

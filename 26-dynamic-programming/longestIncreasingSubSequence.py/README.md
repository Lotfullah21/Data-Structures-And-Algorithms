## Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence

<h3><a href="https://leetcode.com/problems/longest-increasing-subsequence/">leetcode-300</a></h3>

<ul>
Companies
<li>Google</li>
<li>Microsoft</li>
<li>Amazon</li>
<li>Apple</li>
<li>Adobe</li>
</ul>

## Table:

```
| Iteration | `i` | `arr[i]` | `low` | `high` | `mid` | `dp`                      | `ans` |
|-----------|-----|----------|-------|--------|-------|---------------------------|-------|
| 1         | 0   | 10       | 0     | 0      | -     | [10, 0, 0, 0, 0, 0, 0, 0] | 1     |
| 2         | 1   | 9        | 0     | 1      | 0     | [9, 0, 0, 0, 0, 0, 0, 0]  | 1     |
| 3         | 2   | 2        | 0     | 1      | 0     | [2, 0, 0, 0, 0, 0, 0, 0]  | 1     |
| 4         | 3   | 5        | 0     | 1      | 0     | [2, 5, 0, 0, 0, 0, 0, 0]  | 2     |
| 5         | 4   | 3        | 0     | 2      | 1     | [2, 3, 0, 0, 0, 0, 0, 0]  | 2     |
| 6         | 5   | 7        | 0     | 2      | 1     | [2, 3, 7, 0, 0, 0, 0, 0]  | 3     |
| 7         | 6   | 101      | 0     | 3      | 1, 2  | [2, 3, 7, 101, 0, 0, 0, 0]| 4     |
| 8         | 7   | 18       | 0     | 4      | 2, 3  | [2, 3, 7, 18, 0, 0, 0, 0] | 4     |

```

## Analysis:

## Optimal

`Time Complexity:` O(N^2).
`Space Complexity:` O(N).

### Brute Force

`Time Complexity:` O(NlogN).
`Space Complexity:` O(N).

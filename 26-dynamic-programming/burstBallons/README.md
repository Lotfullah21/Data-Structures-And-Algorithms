# Burst Balloons

<h3><a href="https://leetcode.com/problems/burst-balloons/description/">leetcode-312</a></h3>

## 1. Brute Force Approach:

Padding the Array: The input array nums is padded with 1 at both ends. This simplifies the calculation by ensuring there are always values to multiply at the boundaries.
Recursive Calculation: The helper function calculates the maximum coins that can be obtained by bursting all balloons between indices s and e.
Base Case: When s + 1 == e, there are no balloons to burst between s and e, so the function returns 0.
Recursive Step: For each possible balloon to burst between s and e, the function calculates the maximum coins by considering the left and right subproblems recursively and adding the product of the current burst value.

### Analysis:

Each recursive call can further split into more subproblems, leading to an exponential growth in the number of calls. Specifically, each call to helper(s, e) results in O(n) recursive calls, where n is the length of the subarray from s to e.

##### Recursive Calls:

The depth of recursive call is also `O(N-1)`, because at each recursive call, we are reducing the range, Hence;
`Time Complexity`: `O(N)*T(N-1)` = `O(N!)`.
`Space Complexity`: `O(N)`, because of recursive stack.

## 2. Optimal Approach

Use memoization and store the results of sub problems.

### Analysis:

`Time Complexity`: `O(N^3)`
`Space Complexity`: `O(N^2)`, because of recursive stack.

The entry memo[s][e] stores the maximum coins that can be obtained by bursting all the balloons between the indices s and e (exclusive) in the padded nums array.

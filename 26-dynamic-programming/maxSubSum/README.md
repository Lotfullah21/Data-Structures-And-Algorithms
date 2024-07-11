## House Robber Problem

Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. ith house has a[i] amount of money present in it.

<h2><a href="https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1?itm_source=geeksforgeeks">Geeks for Geeks</a></h2>

```text
helper(a, 6)
|
|-- helper(a, 5)
|   |
|   |-- helper(a, 4)
|   |   |
|   |   |-- helper(a, 3)
|   |   |   |
|   |   |   |-- helper(a, 2)
|   |   |   |   |
|   |   |   |   |-- helper(a, 1)
|   |   |   |   |   |
|   |   |   |   |   |-- helper(a, 0) -> 6
|   |   |   |   |   |-- helper(a, -1) -> 0
|   |   |   |   |   |   Max of (6, 0) -> 7 (store in dp[1])
|   |   |   |   |
|   |   |   |   |-- helper(a, -1) -> 0
|   |   |   |       Max of (7, 1) -> 7 (store in dp[2])
|   |   |
|   |   |-- helper(a, 1) + a[3]
|   |       |
|   |       |-- helper(a, 0) -> 6
|   |       |-- helper(a, -1) -> 0
|   |           Max of (6, 30) -> 36 (store in dp[3])
|   |
|   |-- helper(a, 2) + a[4]
|       |
|       |-- (already computed dp[2]) -> 7
|       |-- (already computed dp[0]) -> 6
|           Max of (7, 8) -> 36 (store in dp[4])
|
|-- helper(a, 3) + a[5]
    |
    |-- (already computed dp[3]) -> 36
    |-- (already computed dp[1]) -> 7
        Max of (36, 2) -> 36 (store in dp[5])


```

## Analysis:

### Recursion Approach

For each function, we are doing a constant work, but we are having n of such functions, so time complexity is `O(N)`.
Space complexity is `O(N)` for using stack space and dp.

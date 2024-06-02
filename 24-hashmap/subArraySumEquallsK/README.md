## Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

<h2><a href="https://leetcode.com/problems/subarray-sum-equals-k/description/">leetcode-560</a></h2>

## Idea-1:

Check for all sub arrays and count how many times, it results to k, but the time complexity here is O(N^2).

```py

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        n = len(nums)
        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum+=nums[j]
                if currentSum==k:
                    c+=1
        return c
```

`Time Complexity`: `O(N^2)`.

## Idea-2:

Use a hashmap.

The following table illustrates the state of the `countMap` and `ans` at each step of the function execution:

### State of `countMap` and `ans` at Each Step

| `ep` | `arr[ep]` | `pf[ep]` | `diff` (`pf[ep] - sum`) | `countMap` Before               | `ans` Before | Update to `ans` | `countMap` After                       | `ans` After |
| ---- | --------- | -------- | ----------------------- | ------------------------------- | ------------ | --------------- | -------------------------------------- | ----------- |
| 0    | 1         | 1        | -6                      | {0: 1}                          | 0            | No              | {0: 1, 1: 1}                           | 0           |
| 1    | 2         | 3        | -4                      | {0: 1, 1: 1}                    | 0            | No              | {0: 1, 1: 1, 3: 1}                     | 0           |
| 2    | 3         | 6        | -1                      | {0: 1, 1: 1, 3: 1}              | 0            | No              | {0: 1, 1: 1, 3: 1, 6: 1}               | 0           |
| 3    | 4         | 10       | 3                       | {0: 1, 1: 1, 3: 1, 6: 1}        | 0            | Yes (ans += 1)  | {0: 1, 1: 1, 3: 1, 6: 1, 10: 1}        | 1           |
| 4    | 5         | 15       | 8                       | {0: 1, 1: 1, 3: 1, 6: 1, 10: 1} | 1            | No              | {0: 1, 1: 1, 3: 1, 6: 1, 10: 1, 15: 1} | 1           |

`Time Complexity`:( O(N) + O(N) = O(N)).
`Space Complexity`: we are using spaces for keeping prefix and hashmap count and we are not returning them as our answer, so, O(N) + O(N) = O(N).

### Why countMap initialized with {0:1}.

It is an exceptional case when the prefix sum equals to K and we did not save the 0 as starting point in the prefixsum array.

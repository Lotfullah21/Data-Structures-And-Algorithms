## Problem Statement

Given an array of integers arr and an integer k, find the maximum sum of any subarray of length k.

Example
Input: arr = [1, 2, 3, 4, 5, 6], k = 3
Output: 15
Explanation
In the array [1, 2, 3, 4, 5, 6], the subarrays of length 3 are:

[1, 2, 3] with sum 6
[2, 3, 4] with sum 9
[3, 4, 5] with sum 12
[4, 5, 6] with sum 15

## 1. Brute Force approach

```py
def sub(arr, k):
    ans = float("-inf")
    for i in range(len(arr)-k+1):
        currentSum=0
        for j in range(i, k+i):
            currentSum = currentSum+arr[j]
        if currentSum>ans:
            ans = currentSum
    return ans
print(sub([1,2,3,4,5,6],3))

```

`Time Complexity: O(N*K)`

## 2. Sliding Window

1. Calculate the first k-size window sum
2. Add one index from the end point of kth window to the first k-size window sum and release one index from starting point of kth window.
   `s = s + nums[eIdx]-nums[sIdx-1]`

```py

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int], k) -> int:
        s = 0
        # Calculate the first K-Size window sum
        for i in range(k):
            s = s+nums[i]
        ans = s
        eIdx = k
        sIdx = 1
        n = len(nums)
        while eIdx<n:
            s = s + nums[eIdx]-nums[sIdx-1]
            ans = max(ans, s)
            sIdx+=1
            eIdx+=1
        return ans

sol = Solution()
nums = [1,2,3,4,5,6]
k = 3
print(sol.maxSubArray(nums, k))


```

`Time Complexity: O(N)`

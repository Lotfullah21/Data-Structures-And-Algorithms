<a href="https://leetcode.com/problems/two-sum/">leetcode</a>

### Idea-1: Brute Force

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] ==target:
                    return [i,j]
        return []

```

### Idea-2: Using Two Pointers

If array is sorted, finding the target can be done in `0(N)` operations.
If the array is not sorted, then the array should be sorted. The time complexity would be `O(N+Nlogn) = O(NlogN)`.

The following code only works if the array is already sorted, because in the question, it asks us to return the original indices, there is a need to tweak the implementation.

```py
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()

        i = 0
        j = n - 1
        while i < j:
            sum_val = nums[i] + nums[j]
            if sum_val == target:
                return [i, j]
            elif sum_val < target:
                i += 1
            else:
                j -= 1

        return [0, 0]

```

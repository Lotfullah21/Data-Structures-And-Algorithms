from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        # Iterate overall possible starting points starting from 0.
        for s in range(n):
            # Defined inside loop so that for each sub array, it should be refreshed.
            currentSum = 0
            # Outer loop being starting point, iterate overall ending poins
            for e in range(s, n):
                currentSum+=nums[e]
                if currentSum==k:
                    count+=1
        return count
solution = Solution()
nums = [1, 2, 3, 20 ,4, 5, 4 ,5 ,21]
k = 26
result = solution.subarraySum(nums, k)
print("Number of subarrays that sum to", k, ":", result)
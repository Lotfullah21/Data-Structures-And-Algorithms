from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = float("-inf")
        n = len(nums)
        
        for i in range(n):
            currentSum = 0
            for j in range(i, n):
                currentSum += nums[j]
                if currentSum > maxNum:
                    maxNum = currentSum
        
        return maxNum

    
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

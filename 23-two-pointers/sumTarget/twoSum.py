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

nums = [3, 2, 400, 90]
target = 402
solution = Solution()
x = solution.twoSum(nums, target)
print(x)

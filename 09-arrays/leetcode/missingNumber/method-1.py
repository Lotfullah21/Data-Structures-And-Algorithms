from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


# Example usage:
nums = [3, 0, 1, 2, 4]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 5
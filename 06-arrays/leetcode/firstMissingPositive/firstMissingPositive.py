from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            if nums[i]<1 or nums[i]>n or i == nums[i]-1:
                i+=1
            else:
                idx = nums[i]-1
                if nums[i]==nums[idx]:
                    i+=1
                else:
                    temp = nums[idx]
                    nums[idx] = nums[i]
                    nums[i] = temp
        for i in range(n):
            if i!=nums[i]-1:
                return i+1
        return n+1

nums = [7,8,9,11,12]
solution = Solution()
answer = solution.firstMissingPositive(nums)
print("First Missing Natural numbers: ",answer)
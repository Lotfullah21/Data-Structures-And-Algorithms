from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf = [0]*len(nums)
        pf[0] = nums[0]
        for i in range(1, len(nums)):
            pf[i] = pf[i-1]*nums[i]
        suffix = 1
        n = len(nums)
        for i in range(n-1, 0, -1):
            pf[i] = pf[i-1]*suffix
            suffix = suffix*nums[i]
        pf[0] = suffix
        return pf
    

    

    
    
nums = [1,2,3,4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)
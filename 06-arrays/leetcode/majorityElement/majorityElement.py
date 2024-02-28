from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = nums[0]
        count = 1
        n = len(nums)
        for ele in range(1, n):
            if nums[ele] == value:
                count+=1
            else:
                if count==0:
                    value = nums[ele]
                    count = 1
                else:
                    count = count -1
        return value
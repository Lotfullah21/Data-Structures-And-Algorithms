from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        n = len(nums)
        for i in range(1, n):
            answer = answer^nums[i]
        return answer
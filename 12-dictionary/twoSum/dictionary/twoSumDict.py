from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToIdx = {}
        for idx,num in enumerate(nums):
            # target = num + unknown
            # unknown = target - num
            unknown = target - num
            if unknown in numsToIdx and numsToIdx[unknown]!=idx:
                return [numsToIdx[unknown], idx]
            else:
                # Until we find the unknown, we will be adding the target.
                numsToIdx[num] = idx
        return []

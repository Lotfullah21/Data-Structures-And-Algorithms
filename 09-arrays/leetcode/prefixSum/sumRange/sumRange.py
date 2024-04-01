from typing import List
class NumArrayBruteForce:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right+1):
            sum = sum + self.nums[i]
        return sum


class NumArray:
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.nums[right]-self.nums[left-1]
        else:
            return self.nums[right]
        


# Your NumArray object will be instantiated and called as such:
nums = [2,1,2,3,3]
obj = NumArrayBruteForce(nums)
param_1 = obj.sumRange(0,2)
print(param_1)
from typing import List
class SolutionBrute:
    def runningSumBruteForce(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i+1):
                sum = sum + nums[j]
            new_arr.append(sum)
        return new_arr
    
class SolutionInPlace:
    def runningSumInPlace(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            # change in place(directly modifying the nums array), the 0th index will not change,So, we are keeping it intact. After 0th index, each element in nums array will be a new number.
            nums[i] = nums[i] + nums[i - 1]
        return nums
    
class Solution:
    def runningSumPf(self, nums: List[int]) -> List[int]:
        # create an array of size nums
        pf = [0]*(len(nums))
        for i in range(len(nums)):
            # for pf[0], in previously declared pf array, we are having the 0 at the last index,So, pf[0] = pf[-1]+pf[0] = 0 + 2 = 2
            pf[i] = pf[i-1] + nums[i]
        return pf
    
    
solution = Solution()
runningSum = solution.runningSumPf([2,1,2,3,3])
print(runningSum)

solutionBrute = SolutionBrute()
runningSumBrute = solutionBrute.runningSumBruteForce([2,1,2,3,3])
print(runningSumBrute)


solutionInPlace = SolutionInPlace()
runningSumInPlace = solutionInPlace.runningSumInPlace([2,1,2,3,3])
print(runningSumInPlace)
from typing import List
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        # Find the xor of two single numbers
        n = len(nums)
        answer = 0
        for i in range(n):
            answer = answer^nums[i]
        # Find the index that is set in answer
        idx = 0
        for i in range(32):
            if self.checkBit(answer, i) == True:
                idx = i
                break
            
        # Use two sets to find the single numbers
        set1 = 0
        set2 = 0
        singleNumbers = []
        for i in range(n):
            num = nums[i]
            if self.checkBit(num,idx) == True:
                set2 = set2^num
            else:
                set1 = set1^num
        singleNumbers.append(set1)
        singleNumbers.append(set2)
        return singleNumbers

    def checkBit(self, N, i):
        if N&(1<<i)!=0:
            return True
        else:
            return False
        
nums = [1,2,1,3,2,5]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
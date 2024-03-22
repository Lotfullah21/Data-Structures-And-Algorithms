from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            count = 0
            for j in range(n):
                # Check the i-th bit for each number
                if nums[j] & (1 << i):
                    count += 1
            # For negative numbers, count the bits differently
            if count % 3 == 1:
                # Handle negative numbers correctly by checking the sign bit
                # If it's the sign bit
                if i == 31:  
                # Set the sign bit for negative result
                    ans -= (1 << i)  
                else:
                # Set the bit in the answer
                    ans = ans | (1 << i) 

        return ans
    
    
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
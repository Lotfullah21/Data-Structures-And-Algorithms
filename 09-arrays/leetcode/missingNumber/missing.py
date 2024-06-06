from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2  
        currentTotal = sum(nums)         
        return total - currentTotal  
    
    
# Example usage:
nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))  # Output: 2
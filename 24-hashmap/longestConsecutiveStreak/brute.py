from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        currentStreak = 1
        longestStreak = 1
        for i in range(1, len(nums)):
            # If there is no duplicates.
            if nums[i]!=nums[i-1]:
                # If current is == to its previous element.
                if nums[i] == nums[i-1]+1:
                    currentStreak+=1
                else:
                    # Save the longest streak here, if in later iteration there is no longer streak than current longestStreak, it will be our answer
                    longestStreak = max(currentStreak, longestStreak)
                    # Update the current streak to its initial value, because the sequence is started again.
                    currentStreak = 1
        return max(longestStreak, currentStreak)
    
    
# Input: [10, 30, 20]
# Output: 1
# Explanation: No numbers are consecutive, so the longest consecutive sequence length is 1.
solution = Solution()
print(solution.longestConsecutive([10, 30, 20]))  # Output: 1

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0
        for num in numSet:
            if num-1 not in numSet:
                currentStreak = 1
                while num+1 in numSet:
                    currentStreak+=1
                    num+=1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak


# Input: [1, 2, 3, 4, 5]
# Output: 5
# Explanation: The entire array is a consecutive sequence.
solution = Solution()
print(solution.longestConsecutive([1, 2, 3, 4, 5]))  # Output: 5
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int], k) -> int:
        s = 0
        # Calculate the first K-Size window sum
        for i in range(k):
            s = s+nums[i]
        ans = s
        eIdx = k
        sIdx = 1
        n = len(nums)
        while eIdx<n:
            s = s + nums[eIdx]-nums[sIdx-1]
            ans = max(ans, s)
            sIdx+=1
            eIdx+=1
        return ans
    
sol = Solution()
nums = [1,2,3,4,5,6]
k = 3
print(sol.maxSubArray(nums, k))

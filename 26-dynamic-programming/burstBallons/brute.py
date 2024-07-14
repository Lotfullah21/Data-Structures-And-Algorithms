class Solution:
    def maxCoins(self, nums) -> int:
        newNums = [1]
        nums = newNums + nums
        nums.append(1)
        n = len(nums)
        s = 0
        e = n-1
        # Base Case when there is no gap between s and e
        return self.helper(nums, s, e)
    def helper(self, n, s, e):
        if s+1>=e:
            return 0
        ans = float("-inf")
        for i in range(s+1, e):
            left = self.helper(n, s, i)
            right = self.helper(n, i, e)
            myAns = left + right + n[s]*n[i]*n[e]
            ans = max(myAns, ans)
        return ans   
    
solution = Solution()
nums = [3,1,5,8]
print("maximum number of coins =",solution.maxCoins(nums))
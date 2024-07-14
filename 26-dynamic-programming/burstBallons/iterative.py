class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for gap in range(2, len(nums)):
            for s in range(0, n-gap):
                e = s+gap
                ans = float("-inf")
                for i in range(s+1, e):
                    myAns = memo[s][i]+memo[i][e]+nums[s]*nums[i]*nums[e]
                    ans = max(ans, myAns)
                memo[s][e] = ans
        return memo[0][n-1]
        
solution = Solution()
nums = [3,1,5,8]
print(solution.maxCoins(nums))
        
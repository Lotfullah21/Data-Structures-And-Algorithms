class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        s = 0
        e = n-1
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.helper(nums, s, e,memo)    
    
    def helper(self, n, s, e, memo):
        # Base Case when there is no gap between s and e
        if s+1>=e:
            return 0
        # Initializing the answer.
        if memo[s][e]!=-1:
            return memo[s][e]
        ans = float("-inf")
        for i in range(s+1, e):
            left = self.helper(n, s, i,memo)
            right = self.helper(n, i, e,memo)
            myAns = left + right + n[s]*n[i]*n[e]
            ans = max(myAns, ans)
        memo[s][e]= ans
        print(memo)
        return ans            
    
solution = Solution()
nums = [3,1,5,8]
print(solution.maxCoins(nums))
        
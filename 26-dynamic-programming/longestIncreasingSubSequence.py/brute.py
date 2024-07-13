class Solution:
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        ans =  1
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            ans = max(ans, dp[i])
        return ans
    
# Usage example
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")
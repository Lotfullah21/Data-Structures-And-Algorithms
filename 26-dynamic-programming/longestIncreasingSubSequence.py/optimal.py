class Solution:
    def lengthOfLIS(self,arr):
        ans = 0
        dp = [0]*len(arr)
        for i in range(len(arr)):
            low = 0
            high = ans
            while low<high:
                mid = (low+ high)//2
                if arr[i]>dp[mid]:
                    low = mid+1
                else:
                    high = mid
            dp[low] = arr[i]
            if low==ans:
                ans+=1
        return ans
                
                
            
# Usage example
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    print(f"The length of the longest increasing subsequence is {solution.lengthOfLIS(nums)}")
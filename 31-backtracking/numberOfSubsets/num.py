class Solution:
    
    def subsetSum(self, arr,k):
        ans = [0]
        i = 0
        sum=0
        self.helper(arr, k , i, sum,ans)
        return ans[0]
        
        
    def helper(self, arr, k, i, sum,ans):
        if i==len(arr):
            if sum==k:
                ans[0]+=1
            return 
        self.helper(arr, k, i+1, sum+arr[i],ans)
        self.helper(arr, k, i+1, sum,ans)
        
arr = [12, 4, 9, 8, 3, 7, -1]
k = 11
sol = Solution()
res = sol.subsetSum(arr, k)
print(res)
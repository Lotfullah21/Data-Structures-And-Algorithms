class Solution:
    
    def subsetSum(self, arr, k):
        ans = []
        results = []
        self.helper(arr, k, 0, 0, ans, results)
        return results
        
    def helper(self, arr, k, i, current_sum, ans, results):
        if i == len(arr):
            if current_sum == k:
                results.append(ans.copy())
            return 
        # Include arr[i] in the current subset
        ans.append(arr[i])
        self.helper(arr, k, i + 1, current_sum + arr[i], ans, results)
        # Exclude arr[i] from the current subset
        ans.pop()  # Correct way to remove the last added element
        self.helper(arr, k, i + 1, current_sum, ans, results)
        
arr = [12, 4, 9, 8, 3, 7, -1]
k = 11
sol = Solution()
res = sol.subsetSum(arr, k)
print(res)

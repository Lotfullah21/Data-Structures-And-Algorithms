class Solution:
    def minSwaps(self, nums, b):
        n = len(nums)
        # Get the sliding window size by counting number of elements<=b
        k=0
        for i in range(n):
            if nums[i]<=b:
                k+=1
        # Count number of elements smaller than b first window
        c=0
        for i in range(k):
            if nums[i]<=b:
                c+=1
        s=1
        e=k
        ans = k-c
        while(e<n):
            if nums[e]<=b:
                c+=1
            if nums[s-1]<=b:
                c-=1
            ans = min(ans, k-c)
            e+=1
            s+=1
        return ans
            
            
# Example usage
solution = Solution()
print(solution.minSwaps([2, 1, 5, 6, 3], 3))  # Output: 1
print(solution.minSwaps([2, 7, 9, 5, 8, 7, 4], 5))  # Output: 2
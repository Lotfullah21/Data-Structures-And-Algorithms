class Solution:
    def sameDifference(self, arr):
        ans = 0
        for i in range(len(arr)):
            for j in range(i):
                if arr[j]-j == arr[i]-i:
                    ans+=1
        print(ans)
        return ans
    


arr = [3,5,1,4,6,6]
solution = Solution()
solution.sameDifference(arr)
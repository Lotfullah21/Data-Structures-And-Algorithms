class Solution:
    def leftSmaller(self,n,arr):
        stack = []
        ans = [-1]*n
        for i in range(n-1, -1, -1):
            while len(stack)>0 and arr[i]<arr[stack[-1]]:
                idx = stack.pop()
                ans[idx] = arr[i]
            stack.append(i)
        return ans
N = 4
arr = [1, 3, 2, 4]
solution = Solution()
result = solution.leftSmaller(N,arr)
print(result)
class Solution:
    def nextLargerElement(self,arr,n):
        stack = []
        print(stack)
        ans = [-1]*n
        for i in range(n):
            while len(stack)>0 and arr[i]>arr[stack[-1]]:
                idx = stack.pop()
                print("idx",idx)
                ans[idx] = arr[i]
            stack.append(i)
            
        while stack:
            idx = stack.pop()
            ans[idx] = -1

        return ans
    
    
N = 4
arr = [1, 3, 2, 4]
solution = Solution()
result = solution.nextLargerElement(arr,N)
print(result)


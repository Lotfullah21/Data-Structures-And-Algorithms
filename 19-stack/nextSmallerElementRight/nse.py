class Solution:
    def help_classmate(self,arr,n):
        stack = []
        answer = [-1]*n
        for i in range(n):
            while len(stack)>0 and arr[i]<arr[stack[-1]]:
                idx = stack.pop()
                answer[idx] = arr[i]
            stack.append(i)
        return answer
N = 4
arr = [1, 3, 2, 4]
solution = Solution()
result = solution.help_classmate(arr,N)
print(result)


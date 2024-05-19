### Question:

Given an array a of integers of length n, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

<a href="https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1?itm_source=geeksforgeeks" target="_blank">GGF</a>

```py
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

[-1, 1, 1, 2]
```

#### Analysis:

`Time Complexity` is `O(N)`, for each element, there is a finite number of possibilities, either replace, do not replace or replace and at max replace N element at last if previous could not.
`Space Complexity` is `O(N)` for stack space

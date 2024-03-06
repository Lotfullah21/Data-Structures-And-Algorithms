### Idea-1: Brute Force

Time complexity `O(N^2)` ans space complexity `O(1)`

```py
class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    ans +=1
        return ans

```

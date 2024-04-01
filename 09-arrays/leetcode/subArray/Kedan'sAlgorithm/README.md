## Brute Force Algorithm

```PY
class Solution:
    ##Complete this function
    def maxSubArraySum(self,arr,N):
        n = len(arr)
        subarray_sum = []
        for s in range(n):
            sum = 0
            for e in range(s, n):
                # It just adds the sum, it does not generate sub arrays.
                sum += arr[e]
                subarray_sum.append(sum)
        return max(subarray_sum)
```

<a href="https://leetcode.com/problems/maximum-subarray/submissions/1183390026/">leetcode</a>

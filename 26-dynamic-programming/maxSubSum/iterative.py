class Solution:
    def FindMaxSum(self, a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0], a[1])
        
        prev2 = a[0]
        prev1 = max(a[0], a[1])
        
        for i in range(2, n):
            current = max(prev1, a[i] + prev2)
            prev2 = prev1
            prev1 = current
        
        return prev1
22
### Brute Force

```py

class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        gcd = []
        maxi = max(a, b)
        for i in range(1,maxi+1):
            if a%i==0 and b%i==0:
                gcd.append(i)
        if len(gcd)>0:
            return max(gcd)
        else:
            return 1
```

### Idea-2:

```py
class Solution:
    def gcd(self, a: int, b: int) -> int:
        if a==0:
            return b
        else:
            return self.gcd(b%a, a)

solution = Solution()
result = solution.gcd(0, 10)



```

#### Analysis:

`Time Complexity` is `O(32)=O(logN)` as we are taking N/2 steps in each function call to reach to 0.
`Space Complexity` is `O(logN)` is the stack space, it can be removed if the implementation is done using Iterative approach.

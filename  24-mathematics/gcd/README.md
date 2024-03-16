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

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        epsilon = 0.0001
        while (ans*ans)<x:
            ans = ans + epsilon
        return math.floor(ans)
x = Solution()
print(x.mySqrt(8))

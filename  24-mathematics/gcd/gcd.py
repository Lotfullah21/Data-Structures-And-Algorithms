class Solution:
    def gcd(self, a: int, b: int) -> int:
        if a==0:
            return b
        else:
            return self.gcd(b%a, a)
        
solution = Solution()
result = solution.gcd(0, 10)
print(result)
class Solution:
    def isCoPrime(self, a, b):
        if self.gcd(a, b)==1:
            return True
        else:
            return False
    
    def coPrimes(self, n):
        for i in range(n // 2):
            print(2 * i + 1, 2 * i + 2)



    def gcd(self, a: int, b: int) -> int:
        if a==0:
            return b
        else:
            return self.gcd(b%a, a)
        
solution = Solution()
result = solution.isCoPrime(9, 10)
coPrimePairs = solution.coPrimes(10)
print(result)
print(coPrimePairs)
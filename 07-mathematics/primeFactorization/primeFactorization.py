class Solution:
    def isPrime(self, n):
        if n==1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def factorization(self, n):
        factors = []
        for i in range(2, n+1):
            if self.isPrime(i):
                x = i
                while n%x==0:
                    factors.append(i)
                    x=x*i
        return factors
                    
                    
solution = Solution()
factors = solution.factorization(100)
for ele in factors:
    print(ele)
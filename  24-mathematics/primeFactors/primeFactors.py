class Solution:
    def  leastPrimeFactor(self, n: int) -> list:
        "Returns smallest prime factor for each."
        spf = [0]*(n+1)
        spf[0]=spf[1] = 1
        for i in range(2,n+1):
            spf[i] = i
        for i in range(2, int((n**0.5)+1)):
            # If spf[i]==i; mean it is a prime number, it also means the factors are not yet placed. 
            if spf[i]==i:
                for j in range(i*2, n+1, i):
                    # Place at each index, min of current index or the places prime factors.
                    spf[j] =  min(spf[j], i)
        return spf
    def primeFactors(self, n, q):
        spf = self.leastPrimeFactor(n)
        x = q
        while x>1:
            print(spf[x],end=" ")
            x = int(x/spf[x])             
        print()
        
                    
solution = Solution()
# n = int(input("Enter a number: "))
n = 13
result = solution.leastPrimeFactor(n)
result = solution.primeFactors(n, 10)
print(result)

class Solution:
    def isPrime(self, n):
        "Returns True if a given n is a prime number."
        count = 0
        for i in range(1, n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        else:
            return False
        
    def printPrime(self,n):
        "Returns prime numbers up to n, including n."
        primeNumbers = []
        for i in range(2,n+1):
            # 
            if self.isPrime(i):
                primeNumbers.append(i)
        return primeNumbers
        
solution = Solution()
n = int(input("Enter a number: "))
result = solution.isPrime(n)
result = solution.printPrime(n)
print(result)
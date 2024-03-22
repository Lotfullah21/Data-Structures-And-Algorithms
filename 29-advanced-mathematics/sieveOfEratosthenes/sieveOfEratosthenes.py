class Solution:
    def  sieveOfEratosthenes(self, n: int) -> list:
        "Returns a list of prime number up to n; including n."
        # Create an array of size n.
        primes = [True]*(n+1)
        # Fill with False the first two indices.
        primes[0] = False
        primes[1] = False
        # for i in range(2, (n)+1):
        for i in range(2, int(n**0.5)+1):
            if primes[i]==True:
                for j in range(2*i, n+1, i):
                    primes[j]=False
        # print(primes)
        primes_list = []
        for i in range(n+1):
            if primes[i]==True:
                primes_list.append(i)
        return primes_list
                    
solution = Solution()
# n = int(input("Enter a number: "))
n = 13
result = solution.sieveOfEratosthenes(n)
print(result)

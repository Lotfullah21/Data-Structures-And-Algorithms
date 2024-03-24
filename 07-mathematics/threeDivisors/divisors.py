import math

class Solution:
    def countNumbersWith3Divisors(self, N: int) -> int:
        """
        Returns the count of numbers less than or equal to N
        that have exactly 3 divisors.
        """
        count = 0
        for i in range(2, N + 1):
            if self.countDivisors(i) == 3:
                count += 1
        return count

    def countDivisors(self, n: int) -> int:
        """
        Returns the number of divisors of integer n
        """
        divisors = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                # If divisors are same, increment once.
                if n // i == i:
                    divisors += 1
                # Otherwise, increment twice.
                else:
                    divisors += 2
        return divisors
    
solution = Solution()
n = int(input("Enter an integer: "))    
divisors  = solution.divisors(n)
exactlyThree = solution.exactly3Divisors(n)
print("all divisors of",n,"are =",divisors)
print("Exactly three divisors", exactlyThree)
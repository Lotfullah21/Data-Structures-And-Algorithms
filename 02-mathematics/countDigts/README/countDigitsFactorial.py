class Solution:
    def digitsInFactorial(self,N: int) ->int:
        "Given N number, it returns how many digits are there in factorial of N"
        if N>14:
            return "Enter a lower integer between 1-15"
        digits = self.factorial(N)
        count = 0
        while digits>0:
            digits = digits//10
            count+=1
        return count
        
    def factorial(self, N):
        if N==1 or N==0:
            return 1
        return N * self.factorial(N-1)
    
solution = Solution()
N = int(input("Enter an integer between (1-14): "))
result = solution.digitsInFactorial(N)
print("total number of digits = ",result)
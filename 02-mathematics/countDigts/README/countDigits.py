class CountDigits:
    def countDigits(self, N: int) -> int:
        "Given integer N, it returns number of digits present in N"
        count  = 0
        while N>0:
            N = N//10
            count+=1
        return count
    
solution = CountDigits()
number = int(input("Enter an integer: "))
result = solution.countDigits(number)
print("total number of digits =", result)
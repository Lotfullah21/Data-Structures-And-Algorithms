class Solution:
    def divide(self, divisioned: int, divisor: int) -> int:
        sign = 1
        if divisioned < 0:
            sign = -sign
        if divisor < 0:
            sign = -sign
        divisioned = abs(divisioned)
        divisor = abs(divisor)
        temp = 0
        answer = 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i)) <= divisioned:
                answer = answer + (1 << i)
                temp = temp + (divisor << i)
        if sign < 0:
            answer = -answer

        if answer > 2**31 - 1:
            return 2**31 - 1
        elif answer < -(2**31):
            return -(2**31)
        else:
            return answer

            
solution = Solution()
result = solution.divide(2147483647,1)
print(result)
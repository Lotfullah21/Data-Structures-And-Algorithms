class Solution:
    def divide(self, a: int, b: int) -> int:
        ans = 0
        count = 0
        sign = 1

        # Handle the sign of the result
        if a<0:
            sign = -sign
        if b<0:
            sign = -sign

        a = abs(a)
        b = abs(b)

        while a >= b:
            a -= b
            count += 1
        ans = count * sign

        # Handle overflow
        if ans > 2**31 - 1:
            return 2**31 - 1
        elif ans < -2**31:
            return -2**31
        else:
            return ans

solution = Solution()
result = solution.divide(21, 1)
print(result)

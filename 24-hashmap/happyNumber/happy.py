class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            totalSum  = 0
            while n>0:
                digit = n%10
                totalSum+=digit*digit
                n = n//10
            return totalSum
        prevSet = set()
        while n!=1 and n not in prevSet:
            prevSet.add(n)
            n = getNext(n)
        if n==1:
            return True
        else:
            return False



# Example usage:
solution = Solution()
print(solution.isHappy(129))  # True, because 129 is a happy number

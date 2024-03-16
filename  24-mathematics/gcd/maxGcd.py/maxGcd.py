class Solution:
    
    def prefixGCD(self, arr: list) -> list:
        n  = len(arr)
        sgcd = [0]*n
        sgcd[0] = arr[0]
        for i in range(1,n):
            sgcd[i] = self.gcd(sgcd[i-1],arr[i])
        return sgcd
    
    def suffixGCD(self,arr: list) -> list:
        n  = len(arr)
        pgcd =  [0]*n
        pgcd[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            pgcd[i] = self.gcd(pgcd[i+1],arr[i])
        return pgcd
    
    def maxGcd(self, arr):
        n = len(arr)
        pgcd = self.prefixGCD(arr)
        sgcd = self.suffixGCD(arr)
        answer = 0
        answer = max(answer, sgcd[1])
        for  i in range(1, n-1):
            left = pgcd[i-1]
            right = sgcd[i+1]
            overAllGCD = self.gcd(left, right)
            answer = max(overAllGCD, answer)
        answer = max(answer, pgcd[n-2])
        return answer
    
    def gcd(self, a, b):
        if a==0:
            return b
        return self.gcd(b%a, a)
            
solution = Solution()
arr = [24, 16, 18, 30, 15]
result = solution.maxGcd(arr)
print(result)

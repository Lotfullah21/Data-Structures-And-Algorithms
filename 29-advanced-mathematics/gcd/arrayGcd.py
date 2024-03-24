class Solution:
    def gcdArray(self, arr: list) ->int :
        "return the gcd among all element of the give array"
        answer = abs(arr[0])
        n = len(arr)
        for i in range(1, n):
            answer = self.gcd(answer, abs(arr[i]))
        return answer
     
    def gcd(self, a: int, b: int) -> int:
        if a==0:
            return b
        else:
            return self.gcd(b%a, a)
    
solution = Solution()
arr = [0, 100]
result = solution.gcdArray(arr)
print(result)
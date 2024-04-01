class Solution:
    def gcdArray(self, arr: list) ->int :
        "returns True if the gcd is == 1 for any subsequence in the array."
        answer = abs(arr[0])
        n = len(arr)
        # Calculate the gcd for all, because if gcd is ==1 for one sequence, then the whole array's gcd will be 1.
        for i in range(1, n):
            answer = self.gcd(answer, abs(arr[i]))
        # if GCD==1
        if answer==1:
            return True
        else:
            return False
     
    def gcd(self, a: int, b: int) -> int:
        if a==0:
            return b
        else:
            return self.gcd(b%a, a)
    
solution = Solution()
arr = [1,123]
result = solution.gcdArray(arr)
print(result)
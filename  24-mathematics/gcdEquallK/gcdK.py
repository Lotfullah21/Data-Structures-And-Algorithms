class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            ans = 0
            for j in range(i, n):
                ans = self.gcd(ans, nums[j])
                if ans<k:
                    break
                elif ans==k:
                    count+=1
        return count
    def gcd(self, a, b):
        if a==0:
            return b
        return self.gcd(b%a, a)
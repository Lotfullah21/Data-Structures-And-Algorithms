from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        countDict = {}
        for ele in deck:
            if ele in countDict:
                countDict[ele]+=1
            else:
                countDict[ele] = 1
        ans = 0
        print(countDict)
        for i,c in countDict.items():
            ans = self.gcd(ans, c)
        if ans>1:
            return True
        return False
        
        
    def gcd(self, a, b):
        if a==0:
            return b
        return self.gcd(b%a, a)
        

arr = [1,2,3,4,4,3,2,1]
solution = Solution()
result = solution.hasGroupsSizeX(arr)
print(result)
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0
        while low<=high:
            mid = low + (high-low)//2
            requiredDays = self.calculateDays(weights, mid)
            if requiredDays<=days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
        return ans

    def calculateDays(self, weights, mid):
        day = 1
        totalWeights = 0
        for i in range(len(weights)):
            if totalWeights+weights[i]>mid:
                day+=1
                totalWeights=0
            totalWeights = totalWeights+weights[i]
        return day
                
                
solution = Solution()
w = [5, 5, 12, 20, 18, 2, 1, 31]
days = 2
result = solution.shipWithinDays(w, days)
print(result)  

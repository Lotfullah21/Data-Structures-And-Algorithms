from typing import List
class Solution:
    def shipWithinDays(self, time: List[int], workers: int) -> int:
        low = max(time)
        high = sum(time)
        ans = 0
        while low<=high:
            mid = low + (high-low)//2
            requiredDays = self.calculateDays(time, mid)
            if requiredDays<=workers:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
        return ans

    def calculateDays(self, time, mid):
        day = 1
        totalWeights = 0
        for i in range(len(time)):
            if totalWeights+time[i]>mid:
                day+=1
                totalWeights=0
            totalWeights = totalWeights+time[i]
        return day
                
                
solution = Solution()
w = [5, 5, 12, 20, 18, 2, 1, 31]
workers = 2
result = solution.shipWithinDays(w, workers)
print(result)  

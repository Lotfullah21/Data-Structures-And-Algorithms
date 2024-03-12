from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = -10
        n = len(height)
        i = 0
        j = n-1
        while i<j:
            minHeight = min(height[i], height[j])
            width = j - i
            totalWater = minHeight * width
            print(totalWater)
            answer = max(totalWater, answer)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return answer
        
        
input= [1,8,6,2,5,4,8,3,7]
solution = Solution()
answer = solution.maxArea(input)
print("max walls", answer)
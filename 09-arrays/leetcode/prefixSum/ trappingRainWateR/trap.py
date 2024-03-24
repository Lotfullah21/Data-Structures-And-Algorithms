from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # By prefix-max, we can get the max heigh of the wall before current wall
        prefix_max = [0]*n
        # By suffix-max, we can get the max height of the wall after current wall.
        suffix_max = [0]*n
        # First element is always is the max based on 0th index.
        prefix_max[0] = height[0]
        for i in range(1, n):
            # Calculate the max height before the current wall and compare it with the height, choose the max of them.
            prefix_max[i] = max(prefix_max[i-1],height[i])
        # Last element is the max height if the starting point is tail of the wall series.
        suffix_max[n-1]=height[n-1]
        for i in range(n-2,-1, -1):
            # Compare the height of current wall with the height of previous wall, choose the max one.
            suffix_max[i] = max(suffix_max[i+1],height[i])
        amount = 0
        # For current Wall
        for i in range(1, n-1):
            # Left wall gives us the wall with the max height before the current wall.
            leftWall = prefix_max[i-1]
            # Right wall gives the wall with max height after the current wall.
            rightWall = suffix_max[i+1]
            # Choose the min of left and right, so that water can trap and do not overflow.
            pivotWall = min(leftWall,rightWall)
            # Subtract from current height, because the current height is the height of the wall from ground. We do not need to count already filled height.
            waterSaved = pivotWall - height[i]
            # pivot wall is>current height, it means we can save water, Hence, the water save sign will be +ve and water unit can be added to the total water.
            if waterSaved>0:
                amount = amount + waterSaved
        return amount
            
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
result = solution.trap(height)
print(result)            
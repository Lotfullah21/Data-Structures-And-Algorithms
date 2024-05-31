from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0:0}
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total+=brick
                countGap[total] = 1 + countGap.get(total, 0)
        ans = len(wall)-max(countGap.values())
        return ans
        
        
wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

solution = Solution()
ans = solution.leastBricks(wall)
print(ans)
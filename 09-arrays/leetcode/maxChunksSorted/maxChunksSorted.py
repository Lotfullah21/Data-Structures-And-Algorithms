from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = [0] * n
        suffix_min = [0] * n
        
        prefix_max[0] = arr[0]
        suffix_min[n - 1] = arr[n - 1]
        
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
        
        ans = 0
        
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                ans += 1
        
        ans += 1
        return ans

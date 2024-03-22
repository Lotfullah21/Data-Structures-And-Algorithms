from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxTillNow = float("-inf")
        count = 0
        n = len(arr)
        for i in range(n):
            maxTillNow = max(maxTillNow, arr[i])
            if maxTillNow == i:
                count+=1
        return count
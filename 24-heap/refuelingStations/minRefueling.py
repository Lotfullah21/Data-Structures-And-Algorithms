import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        currentDist = startFuel
        i = 0
        pq = []
        heapq.heapify(pq)
        
        while currentDist < target:
            while i < len(stations) and currentDist >= stations[i][0]:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1
            currentDist += -heapq.heappop(pq)
            ans += 1
        return ans

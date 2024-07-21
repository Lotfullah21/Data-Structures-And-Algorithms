from typing import List
import heapq

class Solution:
    class Pair:
        def __init__(self, x, h):
            self.x = x
            self.h = h
        
        def __lt__(self, other):
            if self.x != other.x:
                return self.x < other.x
            else:
                return self.h < other.h

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        newList = []
        ans = []
        
        # Convert the buildings into events
        for building in buildings:
            sp, ep, ht = building
            newList.append(self.Pair(sp, -ht))  # Start of a building
            newList.append(self.Pair(ep, ht))   # End of a building
        
        # Sort the events
        newList.sort()
        
        # Priority queue (min-heap) to store the heights
        pq = []
        heapq.heappush(pq, 0)  # Initialize with height 0
        prevH = 0
        
        for event in newList:
            x, h = event.x, event.h
            
            if h < 0:  # Starting of a building
                heapq.heappush(pq, h)  # Push negative height to the heap
            else:  # Ending of a building
                pq.remove(-h)  # Remove the height from the heap
                heapq.heapify(pq)  # Re-heapify after removal
            
            # Get the current height
            currentH = -pq[0] if pq else 0
            
            # Check if we need to add a new key point
            if prevH != currentH:
                ans.append([x, currentH])
                prevH = currentH
        
        return ans

# Example usage:
sol = Solution()
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [6, 8, 10], [7, 9, 8]]
print(sol.getSkyline(buildings))

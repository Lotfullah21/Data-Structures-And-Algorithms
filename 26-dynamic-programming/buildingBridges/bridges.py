class Solution:
    class Pair:
        def __init__(self, w, h):
            self.x = w
            self.y = h
            
        def __repr__(self):
            return f"Pair(w={self.x}, h={self.y})"
        def __lt__(self, other):
            if self.x!=other.w:
                if self.x<other.w:
                    return True
                # else:
                #     return False
            else:
                if self.y>other.h:
                    return True
                # else:
                #     return False
        
        
    def buildBridges(self, coordinates):
        n = len(coordinates)
        arr = []
        for i in range(n):
            arr.append(self.Pair(coordinates[i][0], coordinates[i][1]))
        print("Before sorting:", arr)
        arr.sort()
        print("After sorting:", arr)
        ans = 0
        dp = [0]*n
        for i in range(n):
            low = 0
            high = ans
            while low<high:
                mid = (low+high)//2
                if arr[i].h>dp[mid]:
                    low = mid+1
                else:
                    high = mid
            dp[low] = arr[i].h
            if ans==low:
                ans+=1
        return ans

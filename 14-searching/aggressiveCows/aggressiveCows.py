class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        low =self.minDistance(stalls)
        high = stalls[-1]-stalls[0]
        ans = -1
        while low<=high:
            mid = low + (high-low)//2
            cowsPlaced = self.cowsCount(mid, stalls)
            if cowsPlaced>=k:
                low = mid+1
                ans = mid
            else:
                high = mid - 1        
        return ans
        
    
    def minDistance(self, arr):
        minDistance = float("inf")
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<=minDistance:
                minDistance = arr[i+1]-arr[i]
        return minDistance
    
    
    def cowsCount(self, mid, stalls):
        cow = 1
        lastCount = stalls[0]
        n = len(stalls)
        for i in range(1, n):
            if stalls[i]-lastCount>=mid:
                cow+=1
                lastCount=stalls[i]
        return cow
    
n=5 
k=3
stalls = [10, 1, 2, 7, 5]
solution = Solution()
result = solution.solve(n,k,stalls)
print(result)
        
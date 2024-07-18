class Solution:
    #Function to determine number of connected components.
    def findNumberOfConnectedComponents(self,n,arr,rank1):
        par = [0]*(n+1)
        rank1 = [0]*(n+1)
        for i in range(n):
            par[i] = i
        for edge in arr:
            a = edge[0]
            b = edge[1]
            self.unionNodes(a, b, par, rank1)
        ans = 0
        for i in range(len(par)):
            if par[i]==i:
                ans+=1
        return ans
    
    #Function to merge two nodes a and b.
    def unionNodes(self,a,b,arr,rank1):
        pa = self.find(a, arr)
        pb = self.find(b, arr)
        if rank1[pa]>rank1[pb]:
            arr[pb] = pa
        elif rank1[pb]>rank1[pa]:
            arr[pa] = pb
        else:
            arr[pa] = pb
            rank1[pb]+=1
        # code here
    
    def find(self,x, arr):
        if x==arr[x]:
            return x
        temp = self.find(arr[x],arr)
        return temp
            
    
    
# Example usage:
# Create an instance of the Solution class
obj = Solution()

# Example 1
n = 5
arr = [(1, 3), (1, 5)]
rank1 = [0]*(n+1)
print(obj.findNumberOfConnectedComponents(n, arr, rank1))  # Output: 3

# Example 2
n = 5
arr = [(1, 4), (2, 3), (1, 5)]
print(obj.findNumberOfConnectedComponents(n, arr, rank1))  # Output: 2
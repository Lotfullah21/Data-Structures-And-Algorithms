class Solution:    
    def printNos(self,N):
        if N==1:
            print(N, end=" ")
            return 
        self.printNos(N-1)
        print(N, end=" ")
        
# Example usage:
sol = Solution()
sol.printNos(5)  
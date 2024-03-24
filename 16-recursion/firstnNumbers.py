class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        nums = [ ]
        if  N==0:
            return
        else:
            self.printNos(N-1)
            print(N, end="")
    
            
        

solution  = Solution()
result = solution.printNos(12)
print(result)
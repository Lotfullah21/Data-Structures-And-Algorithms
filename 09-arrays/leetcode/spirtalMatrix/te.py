class Solution:
    def spiralMatrix(self, arr: list[list]) -> list[int]:
        n = len(arr)
        m = len(arr[0])
        ans = []
        count = 0
        i = 0
        j = 0
        rowSteps = n - 1
        colSteps = m - 1
        while(rowSteps>=1 and colSteps>=1):
            for _ in range(colSteps):
                ans.append(arr[i][j])
                j+=1
            for _ in range(rowSteps):
                ans.append(arr[i][j])
                i+=1
            for _ in range(colSteps):
                ans.append(arr[i][j])
                j-=1
            for _ in range(rowSteps):
                ans.append(arr[i][j])
                i-=1
                
            colSteps-=2
            rowSteps-=2
            i +=1
            j +=1
        if rowSteps==0:
            for _ in range(colSteps+1):   
                ans.append(arr[i][j])
                j+=1
        elif colSteps==0:
            for _ in range(rowSteps+1):
                ans.append(arr[i][j])
                i+=1
                
                
# The array has be to a same dimensional array.
arr = [[1,2,3,30],[4,5,6,60],[7,8,9,90],[10,11,12,120]]
solution = Solution()
solution.spiralMatrix(arr)
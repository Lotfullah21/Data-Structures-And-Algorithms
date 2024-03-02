class Solution:
    def printSpiralMatrix(self, arr: list[list]) -> list[int]:
        i = 0
        j = 0
        steps = len(arr)-1
        
        if not arr:
            return []
    
        while steps >= 1:
            for k in range(steps):
                print(arr[i][j], end=" ")
                j += 1

            for k in range(steps):
                print(arr[i][j], end=" ")
                i += 1

            for k in range(steps):
                print(arr[i][j], end=" ")
                j -= 1

            for k in range(steps):
                print(arr[i][j], end=" ")
                i -= 1

            i += 1
            j += 1
            steps -= 2

        if steps == 0:
            print(arr[i][j], end=" ")
# The array has be to a same dimensional array.
arr = [[1,2,3,30],[4,5,6,60],[7,8,9,90],[10,11,12,120]]
solution = Solution()
solution.printSpiralMatrix(arr)
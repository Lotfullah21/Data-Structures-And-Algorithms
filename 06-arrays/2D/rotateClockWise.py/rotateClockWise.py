class Solution:
    def transpose(self, matrix):
        row = len(matrix)
        print("Original Array", matrix)
        # Starting from row-1 means, we are going with lower half of the matrix.
        for r in range(1, row):
            for c in range(0,r):
                # save the current [row][col] in temp
                temp = matrix[r][c]
                # Change the matrix[row][col] = matrix[col][row]
                matrix[r][c] = matrix[c][r]
                # Change the matrix[col][row] = matrix[row][col]
                matrix[c][r] = temp
                
    def rotate(self, matrix):
        self.transpose(matrix)   
        start = 0
        end = len(matrix)-1
        for i in range(len(matrix)):
            arr = matrix[i]
            while start<end:
               temp = arr[start]
               arr[start] = arr[end]
               arr[end] = temp
               start+=1
               end-=1
        return matrix
    
arr = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
solution = Solution()
rotated_matrix = solution.rotate(arr)
print(rotated_matrix)
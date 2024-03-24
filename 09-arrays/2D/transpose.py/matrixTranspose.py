class Solution:
    def transpose(self, matrix, n):
        row = len(matrix)
        col = len(matrix[0])
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
        print("Transpose_matrix", matrix)         
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n = len(arr)
solution = Solution()
transpose_array = solution.transpose(arr,n)
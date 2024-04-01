class Solution:
    def transpose(self, matrix):
        row = len(matrix)
        print("Original Array", matrix)
        # Starting from row-1 means, we are going with lower half of the matrix.
        for r in range(1, row):
            for c in range(0, r):
                # save the current [row][col] in temp
                temp = matrix[r][c]
                # Change the matrix[row][col] = matrix[col][row]
                matrix[r][c] = matrix[c][r]
                # Change the matrix[col][row] = matrix[row][col]
                matrix[c][r] = temp

    def rotateAntiClockWise(self, matrix):
        self.transpose(matrix)
        n = len(matrix)
        for i in range(n):
            start = 0
            end = len(matrix) - 1
            while start < end:
                # Keep the columns fixed, move from top to bottom and reverse the indices.
                temp = matrix[start][i]
                matrix[start][i] = matrix[end][i]
                matrix[end][i] = temp
                start += 1
                end -= 1          
        return matrix


arr = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
solution = Solution()
rotated_matrix = solution.rotateAntiClockWise(arr)
print("Rotated matrix", rotated_matrix)

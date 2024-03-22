### Idea-1: Using Extra Space

in this approach we need to create an empty matrix of same size as input array.
`Note:` this code only works for square matrices, rows and columns are same.
For rectangular matrices, we need to create a matrix where the sizes are same as the size of the matrix after transposing.

```py
class Solution:
    def transpose(self, matrix, n):
        row = len(matrix)
        col = len(matrix[0])
        print("Original Array", matrix)
        # Create an array of same size as origin array
        temp = [[0 for i in range(col)] for i in range(row)]
        # First, save the transpose of current array in temp array.
        for i in range(row):
            for j in range(col):
                temp[i][j] = matrix[j][i]
        # Copy the elements of temp array back to main array.
        for i in range(row):
            for j in range(col):
                matrix[i][j] = temp[i][j]
        return matrix
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n = len(arr)
solution = Solution()
transpose_array = solution.transpose(arr,n)
print("Transpose Array",transpose_array)

```

### Idea: Transposing In Place:

Here, we don't need to travel whole matrix. the diagonal of a matrix does not change even after transposing. we either travel the lower half of upper half of the matrix and start transposing them

```py
class Solution:
    def transpose(self, matrix, n):
        row = len(matrix)
        col = len(matrix[0])
        print("Original Array", matrix)
        for r in range(1, row):
            for c in range(0,r):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        print("Transpose_matrix", matrix)

solution.transpose(arr,n)

arr = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


Iteration-0:

r = 1; col = 0
temp = matrix[r][c] = matrix[1][0] = 4
matrix[r][c] = matrix[1][0] = matrix[col][row] = matrix[0][1] = 2
matrix[c][r] = matrix[0][1] = temp = 4
arr = [[1, 4, 0],
        [2, 5, 0],
        [0, 0, 9]]

Iteration-1:

r = 2; col = 0
temp = matrix[r][c] = matrix[2][0] = 7
matrix[r][c] = matrix[2][0] = matrix[col][row] = matrix[0][2] = 3
matrix[c][r] = matrix[0][2] = temp = 7
arr = [[1, 4, 7],
        [2, 5, 0],
        [3, 0, 9]]

r = 2; col = 1
temp = matrix[r][c] = matrix[2][1] = 8
matrix[r][c] = matrix[2][1] = matrix[col][row] = matrix[1][2] = 6
matrix[c][r] = matrix[1][2] = temp = 8
arr = [[1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]]



```

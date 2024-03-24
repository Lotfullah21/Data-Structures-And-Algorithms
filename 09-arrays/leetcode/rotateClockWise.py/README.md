<a href="https://leetcode.com/problems/rotate-image/">leetcode</a>

### Rotation of an array clock wise can be done in two steps:

This is what rotation in clock wise means:

```

Array = [[10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]

Rotation = [[70, 40, 10],
            [80, 50, 20],
            [90, 60, 30]]

This is how transpose of main array looks like

Transpose = [[10, 40, 70],
             [20, 50, 80],
             [30, 60, 90]]

If we look carefully, the transposed matrix is exactly like the rotated one, but with one difference, the rows needs to be reversed in transposed matrix.


Rotation_reversed_row = [[70, 40, 10],
                         [80, 50, 20],
                         [90, 60, 30]]

```

Based on the above findings:

- step-1: Transpose the array.
- step-2: Reverse every single row.

```py

class Solution:
    def transpose(self, matrix):
        row = len(matrix)
        print("Original Array", matrix)
        for r in range(1, row):
            for c in range(0,r):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

    def rotate(self, matrix):
        self.transpose(matrix)
        for row in matrix:
            row.reverse()
        return matrix

arr = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
solution = Solution()
rotated_matrix = solution.rotate(arr)
print(rotated_matrix)
```

### Rotation of an array Anti-clock wise can be done in two steps:

```

Array = [[10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]

Rotation = [[30, 60, 90],
            [20, 50, 80],
            [10, 40, 70]]

This is how transpose of main array looks like

Transpose = [[10, 40, 70],
             [20, 50, 80],
             [30, 60, 90]]

If we look carefully, the transposed matrix is exactly like the rotated one, but with one difference, the columns needs to be reversed in transposed matrix.


Rotation_reversed_row = [[30, 60, 90],
                         [20, 50, 80],
                         [10, 40, 70]]

```

```py
class Solution:
    def transpose(self, matrix):
        row = len(matrix)
        for r in range(1, row):
            for c in range(0, r):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
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

```

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
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
        for i in range(len(matrix)):
            start = 0
            end = len(matrix)-1
            arr = matrix[i]
            while start<end:
               temp = arr[start]
               arr[start] = arr[end]
               arr[end] = temp
               start+=1
               end-=1
        return matrix

```

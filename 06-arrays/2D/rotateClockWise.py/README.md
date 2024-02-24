Rotation of an array clock wise can be done in two steps:

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

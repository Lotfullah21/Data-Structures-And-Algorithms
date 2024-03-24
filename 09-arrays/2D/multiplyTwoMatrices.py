class Solution:
 #Function to add two matrices.
    def sumMatrix(self,A,B):
      
        row1 = len(A)
        col1 = len(A[0])
        row2 = len(B)
        col2 = len(B[0])
        # Initialize a result matrix with zeros of the same size as A and B
        result = [[0 for i in range(col1)] for j in range(row1)]
        # Make sure the dimensions are correct.
        if col1!=col2:
            return []
        for i in range(row1):
            for j in range(col1):
                result[i][j] = A[i][j] * B[i][j]
        return result

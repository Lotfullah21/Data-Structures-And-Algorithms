class NumMatrix:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.pSum = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if j==0:
                    self.pSum[i][j] = matrix[i][j]
                else:
                    self.pSum[i][j] = self.pSum[i][j-1]+matrix[i][j]
                    
                
        for j in range(self.m):
            for i in range(1,self.n):
                if i==0:
                    self.pSum[i][j] = matrix[i][j]
                else:
                    self.pSum[i][j] = self.pSum[i-1][j]+self.pSum[i][j]
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.pSum[row2][col2]
        # final: pf[row2][col2]-pf[row1-1][col2]-pf[row2][col1-1]+pf[row1-1][col1-1]
        # Handle the edge cases.
        if row1-1>=0:
            answer = answer - self.pSum[row1-1][col2]
        if col1-1>=0:
            answer = answer - self.pSum[row2][col1-1]
        if row1-1>=0 and col1-1>=0:
            answer = answer + self.pSum[row1-1][col1-1]
        return answer
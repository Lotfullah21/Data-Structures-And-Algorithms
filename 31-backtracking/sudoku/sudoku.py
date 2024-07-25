from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board)
    
    def helper(self, board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    for x in range(1, 10):
                        if self.isValid(board, i, j, str(x)):
                            board[i][j] = str(x)
                            if self.helper(board):
                                return True
                            board[i][j] = "."
                    return False
        return True

    def isValid(self, board, row, col, x):
        # Check the row
        for j in range(9):
            if board[row][j] == x:
                return False
        # Check the column
        for i in range(9):
            if board[i][col] == x:
                return False
        # Check the 3x3 sub-box
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == x:
                    return False
        return True

class Solution:
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    n = len(matrix)
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        n = len(matrix)
        # Remember, lists are 0 based index, first row is an even row, because it is 0th index, not first index.
        for i in range(n):
            if i%2==0:
                for j in range(n):
                    print(matrix[i][j],end=",")
                print()
            else:
                for j in range(len(matrix[0])-1,-1, -1):
                    print(matrix[i][j],end=",") 
                print()
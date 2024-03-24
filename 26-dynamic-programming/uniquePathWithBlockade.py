"""
Input format
3 3
1 1 1
1 1 1
1 1 1
Output: 6
"""


def main():
    m, n = map(int, input().split())

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    dp = [[-1 for _ in range(n)] for _ in range(m)]
    numberOfUniquePaths = findPath(matrix, m - 1, n - 1, dp)
    print("Number of unique paths =",numberOfUniquePaths)

def findPath(matrix, row, column, dp):
    m, n = len(matrix), len(matrix[0])

    if row < 0 or column < 0 or matrix[row][column] == 0:
        return 0

    if row == 0 and column == 0:
        return 1

    if dp[row][column] != -1:
        return dp[row][column]
    path1 = findPath(matrix, row - 1, column, dp)
    path2 = findPath(matrix, row, column - 1, dp)

    dp[row][column] = path1 + path2
    return dp[row][column]


if __name__ == "__main__":
    main()

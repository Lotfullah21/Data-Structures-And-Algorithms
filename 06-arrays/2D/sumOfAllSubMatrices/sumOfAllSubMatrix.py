def sumOfAllSubMatrix(matrix: list[list]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    total_sum = 0

    for i in range(n):
        for j in range(m):
            total_sum += matrix[i][j] * (i + 1) * (j + 1) * (n - i) * (m - j)

    return total_sum

# Input, n:number of rows; m:number of columns.
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate and print the sum of all submatrices in matrix.
answer = sumOfAllSubMatrix(matrix)
print(answer)
4
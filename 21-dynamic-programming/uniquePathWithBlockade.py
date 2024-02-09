def main():
    m, n = map(int, input().split())

    arr = []
    for _ in range(m):
        row = list(map(int, input().split()))
        arr.append(row)

    dp = [[-1 for _ in range(n)] for _ in range(m)]
    ans = findPath(arr, m - 1, n - 1, dp)
    print(ans)
    

def findPath(arr, sr, sc, dp):
    m, n = len(arr), len(arr[0])

    if sr < 0 or sc < 0 or arr[sr][sc] == 0:
        return 0

    if sr == 0 and sc == 0:
        return 1

    if dp[sr][sc] != -1:
        return dp[sr][sc]

    path1 = findPath(arr, sr - 1, sc, dp)
    path2 = findPath(arr, sr, sc - 1, dp)

    dp[sr][sc] = path1 + path2
    return dp[sr][sc]


if __name__ == "__main__":
    main()

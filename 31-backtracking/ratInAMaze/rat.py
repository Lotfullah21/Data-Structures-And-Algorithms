class Solution:
    def findPath(self, mat):
        if mat[0][0] == 0:
            return []
        pick = []
        n = len(mat)
        self.helper(mat, 0, 0, n, "", pick)
        return pick if pick else ["-1"]

    def helper(self, mat, r, c, n, path, pick):
        if r < 0 or c < 0 or r >= n or c >= n or mat[r][c] != 1:
            return
        
        if r == n - 1 and c == n - 1:
            pick.append(path)
            return
        
        mat[r][c] = 2  # Mark the cell as visited
        self.helper(mat, r + 1, c, n, path + "D", pick)  # Down
        self.helper(mat, r, c - 1, n, path + "L", pick)  # Left
        self.helper(mat, r - 1, c, n, path + "U", pick)  # Up
        self.helper(mat, r, c + 1, n, path + "R", pick)  # Right
        mat[r][c] = 1  # Unmark the cell
        
# Example usage:
sol = Solution()
mat = [[1, 0, 0, 0],
       [1, 1, 0, 1], 
       [1, 1, 0, 0],
       [0, 1, 1, 1]]
print(sol.findPath(mat))  # Output: ['DDRDRR', 'DRDDRR']

mat = [[1, 0],
       [1, 0]]
print(sol.findPath(mat))  # Output: ['-1']
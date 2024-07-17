class Solution:
    def isNegativeWeightCycle(self, n, edges):
        # Initialize distances from source to all vertices as infinite
        ans = [float("inf")] * n
        ans[0] = 0  # Distance to the source is 0

        # Relax all edges |n-1| times
        for _ in range(n - 1):
            for u, v, wt in edges:
                if ans[u] != float("inf") and ans[u] + wt < ans[v]:
                    ans[v] = ans[u] + wt  # Update distance if a shorter path is found

        # Check for negative-weight cycles
        for u, v, wt in edges:
            if ans[u] != float("inf") and ans[u] + wt < ans[v]:
                return 1  # Negative weight cycle detected

        return 0  # No negative weight cycle found

# Example usage:
edges = [
    (1, 0, 5),
    (1, 2, -2),
    (1, 4, 6),
    (2, 3, 3),
    (3, 1, -4)
]
solution = Solution()
n = 5  # Number of vertices
print(solution.isNegativeWeightCycle(n, edges))  # Expected output: 1

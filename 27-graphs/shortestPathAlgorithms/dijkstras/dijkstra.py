import heapq
class Solution:
    # Class to represent a vertex and its current known shortest distance from the source.
    class Pair:
        def __init__(self, vtx, wts):
            self.wts = wts
            self.vtx = vtx
            
        # This method ensures that the priority queue maintains the vertex with the smallest weight at the top.
        def __lt__(self, other):
            if self.wts<other.wts:
                return True
            else:
                return False
            
    def dijkstra(self, V, adj, S):
        pq = []
        ans = [float("inf")]*V
        heapq.heappush(pq, Solution.Pair(S, 0))
        # As long as there is something in our heap
        while pq:
            # Pop up the vertex with the smallest known distance
            rem = heapq.heappop(pq)
            # Check if the removed vertex is is not in the answer
            if ans[rem.vtx]!=float("inf"):
                continue
            # Record the shortest distance to this vertex.
            ans[rem.vtx] = rem.wts
            # Check for its neighbors for two purpose,
            # If there are already in the answer list or to add them in heapq
            for nbr, wt in adj[rem.vtx]:
                if ans[nbr]!=float("inf"):
                    continue
                heapq.heappush(pq, Solution.Pair(nbr, rem.wts + wt))
        return ans
    
    
    
# Define the graph as an adjacency list
V = 5  # Number of vertices
adj = [
    [(1, 2), (4, 1)],  # Edges from vertex 0 to 1 (weight 2) and to 4 (weight 1)
    [(2, 3), (4, 2)],  # Edges from vertex 1 to 2 (weight 3) and to 4 (weight 2)
    [(3, 6)],          # Edge from vertex 2 to 3 (weight 6)
    [(4, 4)],          # Edge from vertex 3 to 4 (weight 4)
    []                 # Vertex 4 has no outgoing edges
]

# Source vertex
S = 0

# Create an instance of the Solution class and call the dijkstra method
solution = Solution()
shortest_distances = solution.dijkstra(V, adj, S)

# Print the shortest distances from the source vertex to all other vertices
print("Shortest distances from vertex", S, "to all other vertices:")
for i, dist in enumerate(shortest_distances):
    print(f"Vertex {i}: {dist}")
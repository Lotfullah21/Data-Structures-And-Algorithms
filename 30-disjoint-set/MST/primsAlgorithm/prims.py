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
            
    def prims(self, V, adj, S):
        pq = []
        visited = [False]*V
        heapq.heappush(pq, Solution.Pair(S, 0))
        # As long as there is something in our heap
        while pq:
            # Pop up the vertex with the smallest known distance
            rem = heapq.heappop(pq)
            # Check if the removed vertex is visited list, if visited, go to the next element.
            if visited[rem.vtx]!=False:
                continue
            # Record the shortest distance to the removed vertex.
            visited[rem.vtx] = rem.wts
            # Check for its neighbors for two purpose,
            # If there are already in the visited list and to add them to the heap.
            for nbr, wt in adj[rem.vtx]:
                # Check if the removed vertex is visited list, if visited, go to the next element.
                if visited[nbr]!=False:
                    continue
                heapq.heappush(pq, Solution.Pair(nbr, wt))
        s=0
        for ele in visited:
            s +=ele
        return s
    
    
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

# Create an instance of the Solution class and call the prims method
solution = Solution()
shortest_distances = solution.prims(V, adj, S)
print("total of MST =", shortest_distances)
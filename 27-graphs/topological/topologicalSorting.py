from collections import deque
class Solution:
    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        dq = deque()
        # Initialize indegree array
        indegree = [0] * V
        # Calculate indegree for each vertex
        for i in range(V):
            for u in adj[i]:
                indegree[u] += 1
        # Add vertices with zero indegree to the deque
        for i in range(V):
            if indegree[i] == 0:
                dq.append(i)
        ans = []
        while dq:
            # Remove element from deque and add to answer
            removed = dq.popleft()
            ans.append(removed)
            # Decrease the indegree of adjacent vertices
            for ele in adj[removed]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    dq.append(ele)
        return ans

# Create the graph
V = 7
adj = [
    [],      # Node 0 has no outgoing edges
    [2],     # Node 1 has an edge to node 2
    [3, 1],  # Node 2 has edges to nodes 3 and 1
    [],      # Node 3 has no outgoing edges
    [0, 1],  # Node 4 has edges to nodes 0 and 1
    [0, 2],  # Node 5 has edges to nodes 0 and 2
    [2]      # Node 6 has an edge to node 2
]

# Create Solution object
solution = Solution()

# Perform topological sort
topological_order = solution.topoSort(V, adj)

# Print the topological order
print("Topological Sort of the given graph is:")
print(topological_order)

from collections import deque
from typing import List
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # create a visited list to keep track of visited nodes
        visited = [False]*V
        # initialize a queue
        queue = deque()
        answer = []
        # add the source node.
        queue.append(0)
        # make it as visited node.
        visited[0] = True
        while queue:
            removed = queue.popleft()
            answer.append(removed)
            # check for the vertices inside the removed vertex.
            for u in adj[removed]:
                # if those vertices are not visited.
                if visited[u]==False:
                    # make their visited value as true.
                    visited[u] = True
                    # add them to the queue.
                    queue.append(u)
        return answer
    
# Example usage:
V = 5  # Number of vertices
E = 4  # Number of edges
# Adjacency list
adj = [[1, 2, 3], [], [4], [], []] 
# You can create an instance of Solution and call the bfsOfGraph method with the desired V and adjacency list.
solution = Solution()
result = solution.bfsOfGraph(V, adj)
# Output the BFS traversal.
for node in result:
    print(node, end=" ")
print()
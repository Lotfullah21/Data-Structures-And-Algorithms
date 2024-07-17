from collections import deque
from typing import List
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self,adj,source,visited):
        # initialize a queue
        queue = deque()
        answer = []
        # add the source node.
        queue.append(source)
        # make it as visited node.
        visited[source] = True
        while queue:
            removed = queue.popleft()
            answer.append(removed)
            # print(removed,end=" ")
            # check for the vertices inside the removed vertex.
            for u in adj[removed]:
                # if those vertices are not visited.
                if visited[u]==False:
                    # make their visited value as true.
                    visited[u] = True
                    # add them to the queue.
                    queue.append(u)
        return ("BFS Traversal",answer)

    def bfsOfGraphDis(self,adj):
        visited = [False] * len(adj)
        res = 0
        for u in range(len(adj)):
            if visited[u]==False:
                # We are coming inside this condition only if we come across a disconnected component.
                # For instance given a source node which is i, in one go, we will visit all vertices there in that component.
                res+=1
                self.bfsOfGraph(adj,u,visited)
        return res
                
    
# Example usage:

V = 5  # Number of vertices
E = 4  # Number of edges
adj = [
    [1, 2],   # Vertex 0 is connected to 1 and 2
    [0],      # Vertex 1 is connected to 0
    [0],      # Vertex 2 is connected to 0
    [4],      # Vertex 3 is connected to 4
    [3, 5],   # Vertex 4 is connected to 3 and 5
    [4]       # Vertex 5 is connected to 4
]


# You can create an instance of Solution and call the bfsOfGraph method with the desired V and adjacency list.
solution = Solution()
print("Disconnected Components =",solution.bfsOfGraphDis(adj))

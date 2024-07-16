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
            print(removed,end=" ")
            # check for the vertices inside the removed vertex.
            for u in adj[removed]:
                # if those vertices are not visited.
                if visited[u]==False:
                    # make their visited value as true.
                    visited[u] = True
                    # add them to the queue.
                    queue.append(u)
        print()
        return answer

    def bfsOfGraphDis(self,adj):
        visited = [False] * len(adj)
        for u in range(len(adj)):
            if visited[u]==False:
                self.bfsOfGraph(adj,u,visited)
                
    
# Example usage:

V = 5  # Number of vertices
E = 4  # Number of edges
adj = [[1, 2, 3], [], [4], [], []]  # Adjacency list

# You can create an instance of Solution and call the bfsOfGraph method with the desired V and adjacency list.
solution = Solution()
solution.bfsOfGraphDis(adj)

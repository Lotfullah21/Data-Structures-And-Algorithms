from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of the given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False]*V
        ans = []
        q = Queue()
        q.put(0)
        visited[0]=True
        while not q.empty():
            removed = q.get()
            ans.append(removed)
            for vertex in adj[removed]:
                if visited[vertex]==False:
                    visited[vertex]= True
                    q.put(vertex)
        return ans



# Example usage:
# Adjacency list representation of the graph
adj_list = [[1, 4], [0, 4, 2, 3], [1, 3], [1, 2, 4], [0, 1, 3]]

solution = Solution()
bfs_result = solution.bfsOfGraph(5, adj_list)
print("BFS Traversal Output:", bfs_result)
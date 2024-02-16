from typing import List
class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

solution = Solution()
V = 5; E = 7
edges = {(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)}
graph = solution.printGraph(V,edges)
print(graph)
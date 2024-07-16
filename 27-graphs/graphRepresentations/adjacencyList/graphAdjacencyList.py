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
edges = {(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)}

# To ask user the number of vertices should be greater than the max vertex index in the edges dictionary.
maxEdge = -1
for u,v in edges:
    maxEdge = max(maxEdge, u, v)

while True:
    V = int(input("Enter the number of vertices: "))
    if V>maxEdge:
        # Break causes the loop to terminate, in fact it does not make it false, just get of the loop.
        break
    else:
        print("Please enter a number greater than",maxEdge)


graph = solution.printGraph(V,edges)
print(graph)



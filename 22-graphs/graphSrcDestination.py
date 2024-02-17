from collections import deque

class Solution:
    def sourceToDestinationPath(self,adj, srcNode, visNode):
        queue = deque()
        queue.append(srcNode)
        visNode[srcNode] = True
        while queue:
            rem = queue.popleft()
            for v in adj[rem]:
                if not visNode[v]:
                    visNode[v] = True
                    queue.append(v)              
    def find(self):
        srcNode = 0  # Number of vertices
        destNode = 4  # Number of edges
        adj = [[1, 2, 3],  # Node 0 is connected to nodes 1, 2, and 3
            [],         # Node 1 has no outgoing connections
            [],         # Node 2 has no outgoing connections
            [],         # Node 3 has no outgoing connections
            []]         # Node 4 has no outgoing connections
        n  = len(adj)
        visNode = [False] * n
        self.sourceToDestinationPath(adj, srcNode, visNode)

        if visNode[destNode]:
            print("true")
        else:
            print("false")

solution = Solution()
solution.find()

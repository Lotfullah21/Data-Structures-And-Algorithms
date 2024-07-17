class Solution:
    # Function to construct and return cost of MST for a graph
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        # Initialized the vertices distances from the source node
        ans = [100000000]*V
        # Initialize the source node
        ans[S] = 0
        # At most a vertex can be |V-1| vertices away from the source node.
        for _ in range(V-1):
            for src,dest,wt in edges:
                # Every time we update the destination node
                if ans[src]!=100000000 and ans[src]+wt<ans[dest]:
                    ans[dest] = ans[src]+wt
        # To detect negative cycle, if there is a negative cycle, even after doing the above iteration still we would be getting smaller distances.
        for src,dest,wt in edges:
            if ans[src]!=100000000 and ans[src]+wt<ans[dest]:
                return [-1]
        return ans
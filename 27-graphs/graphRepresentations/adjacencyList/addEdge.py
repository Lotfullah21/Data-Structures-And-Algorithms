class Graph:
    def addEdge(self, adj, u, v):
        "Adds an edge from vertex u to v"
        adj[u].append(v)
        adj[v].append(u)
        
    def printGraph(self, adjList):
        "Prints the edges in a graph"
        for edges in adjList:
            print(edges)
        
        
v = int(input("How many vertices do you have: "))
adjList = [[] for _ in range(v)]
graph = Graph()
graph.addEdge(adjList, 0, 1)
graph.addEdge(adjList, 2, 5)
graph.addEdge(adjList, 3, 2)
graph.addEdge(adjList, 1, 4)
graph.printGraph(adjList)
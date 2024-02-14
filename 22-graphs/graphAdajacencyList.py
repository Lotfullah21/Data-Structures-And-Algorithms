class Graph:
    def addEdge(self, adjList, u, v):
        adjList[u].append(v)
        adjList[v].append(u)
    def displayGraph(self, adjList):
        for edges in adjList:
            print(edges)
            

graph = Graph()
v = 5
adjList = [[] for i in range(v)]
graph.addEdge(adjList, 0, 1)
graph.addEdge(adjList, 3, 2)
graph.addEdge(adjList, 4, 3)
graph.addEdge(adjList, 1, 3)
graph.addEdge(adjList, 2, 4)
graph.addEdge(adjList, 1, 4)
graph.addEdge(adjList, 2, 3)

graph.displayGraph(adjList)
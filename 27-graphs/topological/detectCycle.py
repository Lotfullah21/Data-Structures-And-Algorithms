from collections import defaultdict, deque

class Solution:
    @staticmethod
    def topoSort(V, adj):
        # Create an inDegree array
        inDegree = [0] * V
        for i in range(V):
            for v in adj[i]:
                inDegree[v] = inDegree[v] + 1            
        # create a queue.
        q = deque()
        topologicalArray = [0] * V
        # append the first elements with degree 0 to the queue
        for i in range(V):
            if inDegree[i]==0:
                q.append(i)
        # use a queue
        count = 0
        while q:
            node = q.popleft()
            # add the popped element to the topological array
            count  = count + 1
            # For that particular node
            for v in adj[node]:
                # Reduce its inDegree
                inDegree[v] -= 1
                # If inDegree becomes zero, add that element to the queue
                if inDegree[v] == 0:
                    q.append(v)
        if count == V:
            return False
        else:
            return True
    
if __name__ == "__main__":
    V, E = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
    if Solution.topoSort(V, adj):
        print("Cycle is detected")
    else:
        print("Cycle is not detected")



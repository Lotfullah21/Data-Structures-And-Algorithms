## Disjoint Union

## Optimization:

Two optimizations are possible

1. Path Compression
2. Union by rank(length of chain)

### 1. Path Compression

```py
    def find(self,u):
        if u==self.par[u]:
            return u
        return temp
```

For the above snippet, every time we need to find parent of a vertex, we do not need or should not re-compute the find function, simply we can save the return value of that vertex and fill it once, in the next time we can use it.

```py
    def find(self,u):
        if u==self.par[u]:
            return u
        temp = self.find(self.par[u])
        return temp
```

### 2. Union by rank(length of chain)

```py
   def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # if parents are the same, do nothing.
        if pu==pv:
            return
        # Make parent of pu to be pv
        self.par[pu] = pv
    # Find the parent of the vertex v
```

Instead of the above one, we can make the parent of the longer chain the over all parent, Because, if we make the shorter's chain's parent the head of the chains, then for loner chain the traversal is incremented by one for each element.

```py
   self.rank = [0]*V
        for i in range(V):
            self.par[i] = i
        # self.par = list(range(V)). [0, 1, 2, ..., V-1]
    def connectedComponents(self, edges, V):
        # Find the u and v edges, make sure to iterate over edges.
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            self.rank[i]=1
        for u,v in edges:
            self.union(u, v)
        c = 0
        for i in range(len(self.par)):
            if self.par[i]==i:
                c+=1
        return c
    # Merge the two vertex with common edges.
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # if parents are the same, do nothing.
        if pu==pv:
            return
        # Make parent of pu to be pv
        if self.rank[pu]>self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pv]>self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pv] = pu
            self.rank[pu]+=1
```

Now, the time complexity of `union() and find()` becomes `O(1)` and overall time complexity is `O(V+E)`.
Before the above optimizations, the time complexity was `(O(V*E))`

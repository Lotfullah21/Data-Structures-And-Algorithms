# Fully Binary Tree

A binary tree which every node other than leaf nodes has two children

```py
    1
   / \
  2   3
 / \
4   5

```

# Perfect Binary Tree

A fully binary tree that in which all leafs are at the same depth and every parent has two children.

```py
    1
   / \
  2   3
 / \ / \
4  5 6  7

```

# Complete Binary Tree

A binary tree that in which every level, except possibly the last is completely filled and all nodes are as left as possible.

```py
    1
   / \
  2   3
 / \ /
4  5 6

```

# Heap

A heap is a specialized binary tree.
The keys at each node is at least as small as the keys stored in its children.

`Min-Heap`: The key at each node is less than or equal to the keys of its children.
`Max-Heap`: The key at each node is greater than or equal to the keys of its children.

```py
Min-heap

    1
   / \
  3   6
 / \ / \
5  9 8  7




```

```
Max-heap

    9
   / \
  5   6
 / \ / \
2  3 4  1



```

### Applications of Heaps:

Heaps are really good when all we care is the smallest or largest element and we do not care about fast lookup, delete or search for arbitrary elements.
`Priority Queues`: Heaps are used to implement priority queues where the highest (or lowest) priority element needs to be accessed quickly.
`Heap Sort`: A comparison-based sorting algorithm that uses a binary heap.
`Graph Algorithms`: Algorithms like Dijkstra's and Prim's use heaps to find the shortest path and minimum spanning tree, respectively.

| Operation                 | Time Complexity |
| ------------------------- | --------------- |
| Insert                    | \( O(\log n) \) |
| DeleteMin/DeleteMax       | \( O(\log n) \) |
| Extract-Min/Extract-Max   | \( O(\log n) \) |
| Find-Min/Find-Max         | \( O(1) \)      |
| Build-Heap                | \( O(n) \)      |
| Decrease-Key/Increase-Key | \( O(\log n) \) |

## Python Library

heap functionality in python is provided by `heapq` module.

`heapq.heapify(L)`: transforms the elements in L into a heap in-place.
`heapq.nlargest(K, L)`: returns `k` smallest elements from list `L`.
`heapq.nlargest(K, L)`: returns `k` largest elements from list `L`.
`heapq.heappush(h, e)`: pushes a new element on the heap.
`heapq.heappop()`: pops the smallest element from the heap.
`heapq.heappushpop(h, a)`: pushes an element on the heap and pops and returns the smallest element from the heap.

By default, when we talk about heapq in python, it is a min-heap.
To transform a min-heap to max-heap, add negative of the elements.

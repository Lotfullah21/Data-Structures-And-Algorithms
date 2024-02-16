### Breadth First Search

it is same as level order traversal where the edges are printed in level by level from sources node.
by level, we mean how many edges away are those nodes from source node.
![Basic Graph](https://github.com/Lotfullah21/data-structure-and-algorithms/assets/85621380/6702e1f0-f83c-476c-b601-e3503144cfb4)

#### Algorithm to solve BFS:

it is based on queue data structure; first in, first out.
For deciding the source node where you are going to measure the other nodes from, either it will be given in problem statement or you can choose it.

1. keep an array of size V, to track the nodes we visited and to make sure we do not visit a node twice.
2. create a queue
3. Add a vertex to the queue.
4. Remove that vertex from the queue.
5. Add the removed vertex to our answer list or print it.
6. Check for the neighbors of removed vertex, by neighbors we mean the element inside that specific vertex which we removed.
   1. If its neighbors are inside the visited list(added to the queue), do not add them to the queue.
   2. If its neighbors are not in the visited list(added to the queue):
      1. Add them to the queue.
      2. Make that specific index boolean value inside our visited list as True.




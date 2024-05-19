## Find nth element from the end side

Given a linked list of length n, return the nth element from left side of the linked list.
Problem description:

N = 2
LinkedList: 1->2->3->4->5->6->7->9->11
Output: 8
Explanation: In the first example, there are 9 nodes in linked list and we need to find 2nd node from end. 2nd node from end is 9.

If n is greater than length, return nothing.

## Idea-1:

Count number of nodes in the linked list.
The relationship to print an element from the left side is (len - n + 1), which means run the loop till here and return the data.

```py
def findNthNode(head:Node, n: int) -> Node:
    "find the Nth node from last point of a linked list."
    NodeCount = 0
    curr = head
    while curr!=None:
        NodeCount = NodeCount + 1
        curr = curr.next
    print("number of nodes =",NodeCount)
    curr = head
    if n>NodeCount:
        return
    for _ in range(1, NodeCount-n+1):
        curr = curr.next
    return curr.data

```

## Analysis:

`Time Complexity`: `O(N)`, because we are traversing the linked only once to count the number of nodes

`Space Complexity`: `O(1)`, No auxiliary space used.

## Idea-2:

Use two pointers, first and second respectively.

- move first pointer n times.
- move second pointer until first reaches the end.
- return second node's data and that is our answer.
  Here, we do not need to count the number of nodes.

```py


```

Analysis remains same as the first method.

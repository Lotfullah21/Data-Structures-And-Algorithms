## Find Middle

Given a linked list of length n, find its middle. if length of the linked list even, return the 2nd element.

Input:1>2>3>4>5
Output:3
Explanation: middle element is 3

Input:1>3>5>7>9>11
Output: 7
Explanation: Even though the element 5 also can be answer, but based on the requirement output should the second element which is 7.

## Idea-1:

### Algorithm:

Use two loops

- First loop to count the number of nodes
- Second loop to go up to the middle point:

1. ##### Count:
   - Use a count variable and initialized it with zero.
   - Use a loop to go up to the end of the linked list.
     - At each iteration, add one to the count.
   - Exit the loop when you are at the end.

```py

def findMid(head):
    curr = head
    if head is None:
        return None
    elif head.next is None:
        return 1
    curr = head
    count = 0
    # First loop to find number of nodes in the linked list.
    while curr!=None:
        count = count + 1
        curr = curr.next
    # Important to update the current, because it has reached to the end because of previous loop.
    print("Number of nodes =",count)
    curr = head
    # Move up to the count//2 and return the element.
    for _ in range(count//2):
        curr = curr.next
    return curr.data


```

## Analysis:

`Time Complexity`: `O(2*N)`, because we are traversing the linked list twice. First time to count number of nodes, second time to get the middle data.

`Space Complexity`: `O(1)`, No auxiliary space used.

## Idea-2(Two pointers):

Use two pointers concept.
If you notice, if one pointer's speed is twice as the other pointer.
If fast pointer reaches the end, slower pointer is in the middle, because its speed is half of fast pointer.

## Algorithm:

- Initialize two pointers, fast pointer's speed is twice is slower's pointer speed.
- Terminate the loop once the fast pointers reaches the tail.

```py
def findMid(head):
    if head is None:
        return None
    fast = head
    slow = head
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    return slow.data


```

## Analysis:

`Time Complexity`: `O(N)`, because we are traversing the linked only once.

`Space Complexity`: `O(1)`, No auxiliary space used.

#### Note:

The difference between first approach and this approach is in the first one, two loops are used, but in the 2nd one only one loop is used.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        # Important edge case
        if head is None:
            return None
        while temp!=None:
            n1 = Node(temp.val)
            # Keep temp's next
            nextNode = temp.next
            # Update head's next
            temp.next = n1
            # Update n1's next
            n1.next = nextNode
            # Update temp
            temp = nextNode
        # Keep the random pointers.
        t = head
        # until t is not None
        while t:
            # if it has a random pointer
            if t.random:
                # make next of current node's random to be current's random's random node
                t.next.random = t.random.next
            # Take two step a time
            t = t.next.next
        # Segregate two linked lists from each other.

        head2 = head.next
        t1 = head
        t2 = head.next
        while t1.next.next!=None:
            t1p1 = t1.next.next 
            t2p1 = t2.next.next 
            t1.next = t1p1 
            t2.next = t2p1 
            t1 = t1p1
            t2 = t2p1
        return head2


        
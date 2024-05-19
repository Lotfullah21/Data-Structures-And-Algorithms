class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if head is None:
            return None
        if head.next is None:
            return head
        curr = head
        prev= None
        while curr!=None:
            # At the end of the loop, the last element will be the new head.
            prev = curr
            curr.prev, curr.next = curr.next, curr.prev
            # Still the linked list is traversed forward, but bcz of swapping, we need to change it to prev.
            curr = curr.prev
        return prev

def printList(head):
    # Helper function to print the list
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()


# Example usage:
if __name__ == "__main__":
    # Creating a doubly linked list
    head = Node(3)
    head.next = Node(4)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next

    print("Original List:")
    printList(head)

    # Reversing the list
    sol = Solution()
    head = sol.reverseDLL(head)

    print("Reversed List:")
    printList(head)
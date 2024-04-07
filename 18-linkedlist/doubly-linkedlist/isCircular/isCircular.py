class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def isCircular(head):
    # If the list is empty, it is not circular
    if not head:
        return False

    # Initialize two pointers, slow and fast
    slow = head
    fast = head

    # Traverse the list using two pointers
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast pointers meet, the list is circular
        if slow == fast:
            return True

    # If we reach here, it means list is not circular
    return False


# Example usage:
if __name__ == "__main__":
    # Creating a doubly linked list
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next
    head.next.next.next = Node(5)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(6)
    head.next.next.next.next.prev = head.next.next.next
    # Connecting the last node to the first node to make it circular
    head.next.next.next.next.next = head
    head.prev = head.next.next.next.next

    # Checking if the list is circular
    if isCircular(head):
        print(1)
    else:
        print(0)

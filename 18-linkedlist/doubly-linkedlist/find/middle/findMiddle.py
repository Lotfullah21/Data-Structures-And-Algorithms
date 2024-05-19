class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def findMiddle(head):
    if head is None:
        return None
    # Initialize two pointers, slow and fast
    slow = head
    fast = head
    # Traverse the list using two pointers
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    # If the list size is odd, slow will be at the middle
    # If the list size is even, slow will be at the first middle element
    return slow.data

# Example usage:
if __name__ == "__main__":
    # Creating a circular doubly linked list
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = head
    head.prev = head.next.next

    # Finding the middle element of the list
    middle = findMiddle(head)
    print("Middle element:", middle)

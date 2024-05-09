class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertInTail(self, data):
        """Inserts a new node after the tail of the doubly linked list.

        Args:
            data (int): The value of the new node to be inserted.
        Returns:
            Node: The head reference of the updated list.
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        return self.head

    def displayList(self):
        """Returns a list containing the data field of each node in the linked list."""
        curr = self.head
        result = []
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

# Example usage
linkedList = DoublyLinkedList()
linkedList.insertInTail(0)
linkedList.insertInTail(20)
linkedList.insertInTail(30)
linkedList.insertInTail(40)
print("linked list =", linkedList.displayList())

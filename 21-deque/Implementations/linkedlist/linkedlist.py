class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insertFront(self, data):
        # Inserts an element at the front of the deque
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp

    def insertRear(self, data):
        # Inserts an element at the rear of the deque
        temp = Node(data)
        if self.rear is None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
            self.rear = temp

    def delFront(self):
        # Deletes the element at the front of the deque
        if self.front is None:
            return
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

    def delRear(self):
        # Deletes the element at the rear of the deque
        if self.rear is None:
            return
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

    def getFront(self):
        # Returns the element at the front of the deque
        if self.front is None:
            return None
        return self.front.data

    def getRear(self):
        # Returns the element at the rear of the deque
        if self.rear is None:
            return None
        return self.rear.data


# Creating a deque
deque = Deque()

# Inserting elements
deque.insertFront(10)
deque.insertFront(20)
deque.insertRear(30)

# Printing front and rear elements
print("Front element:", deque.getFront())  # Output: 20
print("Rear element:", deque.getRear())    # Output: 30

# Deleting elements
deque.delFront()
deque.delRear()

# Printing front and rear elements after deletion
print("Front element after deletion:", deque.getFront())  # Output: 10
print("Rear element after deletion:", deque.getRear())    # Output: 10

from collections import deque
q = deque(["ajda","Da"])
print(q)
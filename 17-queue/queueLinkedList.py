class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        
    def getFront(self):
        return self.front.data
    def getRear(self):
        return self.rear.data
    def isEmpty(self):
        return self._size==0
    def size(self):
        return self._size
    def enque(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self._size = self._size + 1
    
    def deque(self):
        if self.front == None:
            return None
        else:
            nodeData= self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self._size = self._size - 1
            return nodeData
            
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        
    def isEmpty(self) -> bool:
        "checks if the linked list is empty."
        return self._size==0
    
    def size(self) -> int:
        "returns the size of the linked list."
        return self._size
    
    def enque(self, x) -> list:
        "add the elements to the end of a linked list."
        temp = Node(x)
        if self.rear == None:
            self.front = temp
            self.rear = temp
            return 
        self.rear.next = temp
        self.rear = temp
        self._size = self._size + 1
    
    def deque(self) -> list:
        "remove the elements from front of a linked list."
        if self.front == None:
            return None
        else:
            nodeData = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self._size = self._size - 1
            return nodeData
        
    def getFront(self) -> int:
        "returns the first element of the linked list."
        if self.isEmpty():
            return "list empty"
        return self.front.data
    
    def getRear(self) -> int:
        "returns the last element of the linked list."
        if self.isEmpty():
            return "list empty"
        return self.rear.data
    
    def displayList(self) -> list:
        "to display the items inside a linked list"
        result = []
        temp = self.front
        while(temp!=None):
            result.append(temp.data)
            temp = temp.next
        print(result)
        return result
               
queue = MyQueue()
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
print("before deque")
queue.displayList()
print("Front",queue.getFront())
print("Rear",queue.getRear())
print("size",queue.size())
queue.deque()
print("after deque")
queue.displayList()

"""Implementation of stack using linked list"""
class StackNode:
    def __init__(self, key):
        self.data = key
        self.next = None
        
class MyStack:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def push(self,val):
        temp = StackNode(val)
        temp.next = self.head
        self._size = self._size + 1
        self.head = temp
    # instance variables like self.data or self.size should not match with instance methods like size(), pop(),....
    def size(self):
        return self._size
    
    def peek(self):
        if self.head==None:
            return None
        return self.head.data
    
    def pop(self):
        if self.head==None:
            return float("-inf")
        removedVal = self.head.data
        nextToHead = self.head.next
        self.head = nextToHead
        self._size = self._size - 1
        return removedVal    
    
    
def displayList(head):
    temp = head
    while(temp!=None):
        print(temp.data,end=" ")
        temp = temp.next    
    print()
            
                
if __name__ == "__main__":      
    stack = MyStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    displayList(stack.head)
    print("pop",stack.pop())
    print("size",stack.size())
    print("peek",stack.peek())


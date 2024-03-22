class MyQueue:
    def __init__(self):
        self.arr = []
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
            
    def isEmpty(self):
        if len(self.arr)==0:
            return True
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.isEmpty():       
            res = self.arr.pop(0)
            return res
        else:
            print("Queue is Empty")
            return None  
    def getFront(self):
        if not self.isEmpty():
            return self.arr[0]
        else:
            print("Queue is Empty")
            return None
    def getRear(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            print("Queue is Empty")
            return self.arr[-1]
    def __str__(self):
        return str(self.arr)
 
queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.pop()
print("front",queue.getFront())
print("end",queue.getRear())
print("queue",queue)
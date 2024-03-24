class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("-inf")
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
            return
        difference = val - self.min 
        self.stack.append(difference)
        if val<self.min:
            self.min = val
        
        

    def pop(self) -> None:
        removedElement = self.stack.pop()
        if removedElement<0:
            self.min = self.min - removedElement
        else:
            value = self.min + removedElement
    
        

    def top(self) -> int:
        removedElement = self.stack.pop()
        if removedElement<0:
            return self.min
        else:
            value = self.min + removedElement
            return value
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.min
minStack= MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
minStack.top();    # return 0
minStack.getMin(); #// return -2

"""

Implement Queue using stack
We will using three steps
1. move all elements from s1 to s2. using pop()
2. remove the top element from s2
3. move the remaining elements from s2 to s1; use  (pop)

"""


class MyQueueStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self,x: int) -> list:
        self.s1.append(x)
        return self.s1
        
    # def pop(self) -> int:   
    #     if self.s1==None:
    #         return "Queue empty!"  
    #     # remove all elements from s1 to s2.
    #     while self.s1:
    #         self.s2.append(self.s1.pop())
    #     # pop the last element from s2 which was the first element of s1.
    #     ans = self.s2.pop()
    #     # move all elements from s2 to s1.
    #     while self.s2:
    #         self.s1.append(self.s2.pop())
    #     print("removed element",ans)
    #     print("s1",self.s1)
    #     return ans
    
    def pop(self) -> int:   
        if not self.s2:
            if not self.s1:
                return "Queue empty!"
            # Transfer elements from s1 to s2 only when s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
        # Pop the top element from s2
        ans = self.s2.pop()
        print("removed element", ans)
        return ans
    
    def display(self) -> None:
        print("s1",self.s1)
        print("s2",self.s2)


if __name__ =="__main__":
    queueStack = MyQueueStack()
    queueStack.push(1)
    queueStack.push(2)
    queueStack.push(3)
    queueStack.push(4)
    queueStack.push(5)
    queueStack.push(6)
    queueStack.pop()
    queueStack.display()
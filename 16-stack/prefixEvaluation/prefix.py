class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1  
        self.top2 = self.size  

    def push1(self, x):
        if self.top1 < self.top2 - 1:  
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")

    def push2(self, x):
        if self.top1 < self.top2 - 1: 
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:  
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1

    def pop2(self):
        if self.top2 < self.size:  
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1

# Example usage:
two_stacks = TwoStacks(5)
two_stacks.push1(2)
two_stacks.push1(3)
two_stacks.push2(4)
print(two_stacks.pop1())  # Output: 3
print(two_stacks.pop2())  # Output: 4
print(two_stacks.pop2())  # Output: -1

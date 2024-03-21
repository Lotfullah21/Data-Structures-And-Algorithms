class MaxFreq:
    def __init__(self):
        self.stackMap = {}
        self.freqMap = {}
        self.maxFrequency = 0
    # Add
    def push(self, val):
        frequency = self.freqMap.get(val, 0) + 1
        self.freqMap[val]=frequency
        # Check if for the given frequency, do we have a stack.
        if frequency not in self.stackMap:
            self.stackMap[frequency] = []
            self.maxFrequency = max(self.maxFrequency, frequency)
            # print(self.freqMap)
        self.stackMap[frequency].append(val)
        
    # Remove from the top 
    def pop(self):
        answer = self.stackMap[self.maxFrequency].pop()
        frequency = self.freqMap[answer]-1
        self.freqMap[answer] = frequency
        # If no elements remained in maxFreq, delete that stack and reduce the max frequency.
        if not self.stackMap[self.maxFrequency]:
            del self.stackMap[self.maxFrequency]
            self.maxFrequency-=1
        return answer
# Example usage
freqStack = MaxFreq()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

print("Pop:", freqStack.pop())
print("Pop:", freqStack.pop())
print("Pop:", freqStack.pop())


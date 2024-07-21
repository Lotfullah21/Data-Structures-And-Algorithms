class MedianFinder:
    def __init__(self):
        self.data = []

    def addNum(self, num):
        self.data.append(num)
        self.data.sort()

    def findMedian(self):
        n = len(self.data)
        if n % 2 == 0:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2
        else:
            return self.data[n // 2]
medianFinder= MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(4)
medianFinder.addNum(5)
medianFinder.addNum(6)
medianFinder.addNum(7)
medianFinder.addNum(8)

median = medianFinder.findMedian()
print(median)
import heapq
class MedianFinder:
    def __init__(self):
        self.small = [] # Max-Priority Queue
        self.large = [] # Min-Priority Queue
    def addNum(self,number):
        #  if sizes are the same, add the new data to the max-pq
        if len(self.small) == len(self.large):
            # first, pass it via min-heap, check if it is the smallest, if not, get the smallest using pop operation(first element or the root)
            heapq.heappush(self.large,number)
            # save the smallest element in smallest_large variable
            smallest_large = heapq.heappop(self.large)
            # add the neg of smallest_large_heap to small heap, neg sign because of max-heap implementation in smaller heap. 
            heapq.heappush(self.small, -smallest_large)
        else: # if sizes are not the same, add the number to right heap or min-heap where we keep the largest elements.
            heapq.heappush(self.small, -number)
            # check if it is the smallest in max-heap, if we remove the sign, the smallest means the largest and that is what we are looking.
            largest_small = heapq.heappop(self.small)
            # push the largest element from max-heap to the min-heap
            heapq.heappush(self.large,-largest_small)
    def findMedian(self):
        # if sizes are the same, take the average.
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0])/2
        else:
            # if sizes are not the same, the first element in max-heap is our median.
            return -self.small[0]
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
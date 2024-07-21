# Find the median in a data stream:

<a href="https://leetcode.com/problems/find-median-from-data-stream/submissions/1167963748/" target="_blank">leetcode</a>

`median:` it is middle of an element if the list is sorted and the number of items are odd, if even, it is the average of two middle number.
For instance:
`list1 = [1,2,3,4,5]` in this list, median is 3.

`list2 = [1,2,3,4,5,6]`, the number of items are even, so median of this is (3+4/2).

For a data stream where data flow is continuous, every time a new data point enters to the stream, the median changes and we need to find that.

Lets discuss two solutions for this problem.

#### Idea-1:

##### Sorting:

sort the list after each entry and find the median using following code.

```py
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
```

#### Time Complexity:

sorting a list takes `NlogN` operations and if we do the sorting `N` times for each entry, then, the total time complexity would be `N*NlogN`.
The above Time complexity is costly, what if we want to do it in `NlogN` operations.

#### Idea-2:

using max-priority queue and min-priority queue.

##### max-priority queue:

the pop operation will remove the smallest element in constant time `O(1)`

```

       1
     /   \
    2     4
   / \   / \
  5   9 8   10

here, the root element is smallest of all and every node value is smaller than its children.
[1,3,4,5,9,10,12] ## list representation of above tree

```

##### max-priority queue:

```
      12
     /  \
    9    6
   / \  / \
  5   3 1   8

[12, 9,6,5,3,1,8]  ## list representation of above tree

```

here, the root element is largest of all and every node value is larger than its children.
when a remove an element from max-priority queue, we remove the largest element in `O(1)` operations.

###### How to solve above problem using queue.

We are using two queues to avoid sorting the data stream every time which result to smaller number of operations.

1. create two heaps, one to keep smallest and the other one to keep the largest element.
2. if both of have the same size, add the new element to the max-priority queue.
3. but to add to max-priority queue, pass it through min-heap
4. check in min heap if the new element is smallest of all, if so add it max-heap, else, from min-heap add the smallest to max-heap
5. if size of both heaps are same, add the new data to the min-heap or to the right side heap.
6. but to add to min-heap, pass it through max-heap, check if the current element is the largest among all the elements to in min-heap; if it is, add that element to min-heap
7. else, take the largest from max-heap and add that element to the min-heap.

#### Find the median

if lists are the same size, keep the average, max from max-heap and min element from min-heap.
if they are not the same size, the first element in max-heap is our median.

## Note:

In python, we don't have max-heap, when we use `heapq` by default that is a min-heap, which means the elements are sorted in increasing order per say.
To implement max-heap, as you can see from the given implementation, we are adding negative of that number so that the largest are treated as smallest.
When we take them out, we change the negative sign to positive sign.

### Time complexity:

Pushing an element to heap takes `logN` operations.
as we can see in the following block of code

```py

  if len(self.small) == len(self.large):
            heapq.heappush(self.large,number)
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)
```

we push,pop,and push, each of them takes `logN` operation which in total adding a new number will take `3*logN` operations.
If we add `N` numbers, than it will take `NlogN` operations.
space complexity would be `O(N)`, because we are adding `N` elements.
gettin

Getting the average will take `O(1)` operations.

```py
    def findMedian(self):
        # if sizes are the same, take the average.
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0])/2
        else:
            # if sizes are not the same, the first element in max-heap is our median.
            return -self.small[0]
```

As we can see, from `N**2logN` operations, we reduced to `NlogN` operations

## Note:

by operations, we mean to computational complexity or run time which takes to complete a program.
`N` is the input.
`O(N)` means that the run time increases linearly as input increases.

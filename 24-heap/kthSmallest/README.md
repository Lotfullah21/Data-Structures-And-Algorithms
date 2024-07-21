# Find Kth smallest number in a given array

#### Idea-1 (Naive)

sort the array and print Kth element from the array

```py
    def kthSmallest(self,arr, k):
        arr.sort()
        return arr[k-1]
```

#### Time Complexity

above method takes O(Nlog(N) + N), because sorting operation takes NlogN and N iteration to get the element from the give array.

#### Idea-2 (Heap)

Now, what if we want to solve this in O(NlogK).
We will be using only K elements and k is the number of elements in our Priority Queue.
when we use heap, removing an element from queue can be done in constant time (O(n)); to remove an element from Queue we use `py heapq.heappop(heapifList)` where it modifies the heapified list and remove the first element unlike the regular list which we remove the last element using pop operation.

#### Steps

1. we add k elements in our Heap.
2. use `heapq.heapify(ourListWithKthElements)` to heapify or convert our regular array to heap data structure.
3. run a loop for n-k times, where is length of the array; if element in the arr is smaller than the first element in heap, replace it, because we want to keep the smallest values in our Heap.
   Keep K smallest number in the Q

```py
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            if arr[i]<heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, arr[i])
```

4. run the loop k-1 times to pop k-1th element and at the end remove the last remained element in our heap as an answer.
   remove the first k-1th elements, because we want only the last element in our heap.

```py
 for i in range(k-1):
    heapq.heappop(heap)
```

`return heapq.heappop(heap)` returns the last element remained element from our heap.

or just we could use `return heap[k-1]` to return last element, we used loop for better illustration.

# Find Kth largest number in a given array

<a href="https://leetcode.com/problems/kth-largest-element-in-an-array/description/" target="_blank">leetcFFode</a>

#### Idea-1(Naive Solution)

sort the given array and print kth largest element using indexing.

#### Time Complexity

above method takes O(Nlog(N) + N), because sorting operation takes NlogN and N iteration to get the element from the give array.

#### Implementation:

```py

    def findKthLargest(self, nums: list, k: int) -> int:
        "return kth largest element in an array"
        nums.sort()
        return nums[len(nums)-k]
```

#### Idea-2(Priority Queue)

1. keep k elements in a queue.
2. compare those k elements with the remaining elements in the array
3. if array's elements are greater than k's elements, remove smaller elements from k and replace it with larger values from the remaining array elements.
4. at the end return the first element, because in a heap data structure it keeps the element in increasing order(bst tree order) and the first element in the heap will be the kth element from reverse order of an array

```py
    def findKthLargest(self, nums: list, k: int) -> int:
        "return kth largest element in an array"
        # in the heap list keep k largest elements
        heap = []
        for i in range(0,k):
            # add k elements to the heap
            heap.append(nums[i])
            print("heap",heap)
        # convert it to a priority queue
        heapq.heapify(heap)
        print("min-heap",heap)
        for i in range(k,len(nums)):
            # check if the first element in the heap is larger than the array's element.
            if heap[0]<nums[i]:
                # if so, remove the first element.
                heapq.heappop(heap)
                # add the larger element to the array
                heapq.heappush(heap, nums[i])
                print(heap)
        return heap[0]

```

```py
heapq.heappop(heap)
```

It removes the first element from a queue.

### Find Kth smallest number in a given array

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

or just we could use `return heap[k-1]` to return last element, we used loop for better illustration

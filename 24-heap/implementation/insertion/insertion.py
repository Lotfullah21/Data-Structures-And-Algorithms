class Heap:
    def insert(self, arr, x):
        arr.append(x)
        i = len(arr)-1
        while i>0:
            parIdx = (i-1)//2
            # If parent element is larger, swap it.
            if arr[parIdx]>arr[i]:
                temp = arr[i]
                arr[i] = arr[parIdx]
                arr[parIdx] = temp
                # The bellow node is problem is fixed, Now we have to move upward to see if there is any problem in above nodes after swapping.
                i = parIdx
            else:
                break
            
            
# Example usage:
heap = Heap()
arr = []
heap.insert(arr, 10)
heap.insert(arr, 5)
heap.insert(arr, 20)
heap.insert(arr, 2)

print(arr)  # Output: [2, 5, 20, 10] for a min-heap
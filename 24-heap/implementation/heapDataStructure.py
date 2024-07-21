class Heap:
    def delete(self, arr):
        i = len(arr)-1
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        del arr[i]
        i = 0
        while i<len(arr):
            minIdx = i
            leftIdx = 2*i+1
            rightIdx = 2*i+2
            # leftIdx<len(arr), checks if the left or right index is in the range.
            if leftIdx<len(arr) and arr[leftIdx]<arr[i]:
                minIdx = leftIdx
            elif rightIdx<len(arr) and arr[rightIdx]<arr[i]:
                minIdx = rightIdx
            # After the above swapping, if still the ith index is smaller than the right and left index, our tree has no problem; break.
            if minIdx==i:
                break
            else:
                # If still tree is not fixed, keep checking and fixing the tree.
                temp = arr[minIdx]
                arr[i] = arr[minIdx]
                arr[minIdx] = temp
                i = minIdx
                
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
            
    def peak(self, arr):
        "Returns the min element"
        return arr[0]
        
            
            
# Example usage:
heap = Heap()
arr = []
heap.insert(arr, 10)
heap.insert(arr, 5)
heap.insert(arr, 20)
heap.insert(arr, 2)

print(arr)  # Output: [2, 5, 20, 10] for a min-heap
heap.delete(arr)
print(arr)
print(heap.peak(arr))
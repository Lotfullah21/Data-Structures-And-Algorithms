### Selection Sort

It works based on the idea of find the min-elements and put in the array in increasing order; first minimum in first place, 2nd minimum in 2nd place and so on.

It also make the foundation for heap sort algorithm; heap sort uses heap data structure to optimize selection sort.
At each outer iteration, find the minimum and swap it with current element.
It is not stable, the order of equal elements may change.

```py

def selectionSort(arr: list) -> list:
    "Returns a sorted array in increasing order"
    n = len(arr)
    for i in range(n-1):
        min_ele = arr[i]
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx]>arr[j]:
                min_idx = j
                min_ele = arr[j]

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr

array = [1, 0, 12, -2, 4, 5, 6, 2, 4, 3]
sorted = selectionSort(array)
print("Sorted Array:", sorted) # Sorted Array: [-2, 0, 1, 2, 3, 4, 4, 5, 6, 12]
```

```py
First-Iteration:
min_ele=1; min_idx=0;
arr[0]>arr[1] -> 1>0; Yes; update the min-idx;
min-idx = 1, arr[min-idx]=0
arr[1]>arr[2];No
arr[1]>arr[3] -> 1>-2; Yes; update the min-idx;
min-idx=3; arr[min-idx] = arr[3]=-2
arr[3]>arr[4];No
arr[3]>arr[5];No
arr[3]>arr[6];No
...
End first iteration in outer loop.
Swap the elements.
temp = arr[0]
arr[0]=arr[3]
arr[3]=arr[0]
[-2, 0, 12, 1, 4, 5, 6, 2, 4, 3]

Second-Iteration:
min-ele=0; min-idx=1
arr[1]>arr[2];NO
arr[1]>arr[3];No
arr[1]>arr[4];No
.....
Nothing to swap

Third-Iteration:
min-ele = arr[i] = arr[2] = 12
arr[2]>arr[3] -> 12>1; Yes; update the min-idx;
min-idx=3;
arr[3]>arr[4];No
arr[3]>arr[5];No
arr[3]>arr[6];No
.....
End of Iteration in outer loop
temp = arr[2]=12
arr[2]=arr[3]
arr[3]=temp=12
[-2, 0, 1, 12, 4, 5, 6, 2, 4, 3]


```

### Analysis

`Time complexity`: `O(N^2)`.
`Space Complexity`: `O(1)`.

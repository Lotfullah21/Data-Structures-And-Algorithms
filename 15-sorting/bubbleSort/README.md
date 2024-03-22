## Bubble Sort:

A simple sorting algorithm that compares the adjacent elements of a list.
if current element is greater than the next element, swap them.

It has multiple passes:

`first pass:` move the largest element to the last index
`2nd pass:` move the 2nd largest element to the 2nd last index
`3rd pass:` move the largest element to the 3rd last index

The idea is simple, compare the adjacent elements.

#### Brute Force

```py

def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr



n = len(arr) = 5
Iteration 0:
Range of j = (n-1) => (5-1) => (0,4) => 0, 1, 2, 3;

arr = [1, 12, -2, 2, 0]

i = 0; j = (0,4);
arr[0]>arr[1] -> No;
arr[1]>arr[2] -> Yes => Swap Them => [1, -2, 12, 2, 0]
arr[2]>arr[3] -> Yes => Swap Them => [1, -2, 2, 12, 0]
arr[3]>arr[4] -> Yes => Swap Them => [1, -2, 2, 0, 12]

arr  =  [1, -2, 2, 0, 12]
i = 1; j =(0,4);
arr[0]>arr[1] -> Yes => Swap Them => [-2, 1, 2, 0, 12];
arr[1]>arr[2] -> No;
arr[2]>arr[3] -> Yes => Swap Them => [-2, 1, 0, 2, 12];
arr[3]>arr[4] -> No;

arr = [-2, 1, 0, 2, 12];
i = 2; j =(0,4);
arr[0]>arr[1] -> No;
arr[1]>arr[2] -> Yes => Swap Them => [-2, 0, 1, 2, 12];
arr[2]>arr[3] -> No;
arr[3]>arr[4] -> No;

arr = [-2, 0, 1, 2, 12]
i = 3; j =(0,4);
arr[0]>arr[1] -> No;
arr[1]>arr[2] -> No;
arr[2]>arr[3] -> No;
arr[3]>arr[4] -> No;

```

#### Optimized

1. In each iteration, one element is sorted and there is no necessity of going through all iterations same as outer loop every time.

After each iteration, reduce the inner loop iterations by 1. Generally by i.

`for j in range(n-1-i)` subtract `i` from inner loop to reduce the range and avoid repetition.

2. If the whole array is already sorted, there is need of going through each iteration again, go once and see if any changes occurs, if not, it means the array is sorted; return from the function.

```py
def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        # Initially swapped is false.
        swapped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                # If current element is larger than the next, swapped happened, make it true.
                swapped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        # If swapped did not change, mean the array is sorted and return from the function.
        if swapped == True:
            return
    return arr

```

```py
n = len(arr) = 5
Iteration 0:
Range of j = (n-1) => (5-1) => (0,4) => 0, 1, 2, 3;

arr = [1, 12, -2, 2, 0]

i = 0; j = (0,4);
arr[0]>arr[1] -> No;
arr[1]>arr[2] -> Yes => Swap Them => [1, -2, 12, 2, 0]
arr[2]>arr[3] -> Yes => Swap Them => [1, -2, 2, 12, 0]
arr[3]>arr[4] -> Yes => Swap Them => [1, -2, 2, 0, 12]

arr  =  [1, -2, 2, 0, 12]
i = 1; j =(0,3);
arr[0]>arr[1] -> Yes => Swap Them => [-2, 1, 2, 0, 12];
arr[1]>arr[2] -> No;
arr[2]>arr[3] -> Yes => Swap Them => [-2, 1, 0, 2, 12];


arr = [-2, 1, 0, 2, 12];
i = 2; j =(0,2);
arr[0]>arr[1] -> No;
arr[1]>arr[2] -> Yes => Swap Them => [-2, 0, 1, 2, 12];


arr = [-2, 0, 1, 2, 12]
i = 3; j =(0,1);
arr[0]>arr[1] -> No;

```

## Insertion Sort:

### Key Features:

- `O(N^2)` in worst case
- Used in practice for small arrays:
  - For instance, python uses timSort which is combination of `merge sort` and `insertion sort`, when the size of the array is small, it uses `insertion sort.`
- `O(n)` in best case when the array is sorted.

## Insertion Sort Algorithm

- Element at 0th index is sorted.
- Start from 1st index.
  - Go inside the loop
  - Start comparing the current jth element to its jth-1 element
  - If jth is greater than jth+1
    - Movement is done from current left and right.
  - Swap jth and jth+1 element.
  - else, break out of the loop.

```py

    #Function to sort the list using insertion sort algorithm.
    def insertionSort(self, array, n):
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                else:
                    break
        return array

```

### Analysis

`Time complexity`: `O(N^2)`, for two nested loops.
`Space Complexity`: `O(1)`, No extra spaces used.

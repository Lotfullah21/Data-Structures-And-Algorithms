## Merge Sort:

It is one other types of sorting algorithms that works based on divide, conquer and merge.

Some key features:

- Stable Algorithm
- `O(NlogN)` time complexity and `O(1)` space complexity.
- Well suited for linked list, works with `O(1)` auxiliary space.
- Used in Java's and Python's sorting algorithms.
- in arrays, Quick sort algorithm is preferable.

<a href="https://www.geeksforgeeks.org/problems/merge-sort/1?utm_source=gfg">GFG</a>

```py
class Solution:
    def merge(self ,arr,start: int, mid: int, end: int) -> list:
        p1 = start
        p2 = mid+1
        p3 = 0
        # Take care of (end-start+1), because start-end+1 is different.
        temp = [[] for _ in range(end-start+1)]

        while(p1<=mid and p2<=end):
            if arr[p1]<arr[p2]:
                temp[p3] = arr[p1]
                p1+=1
                p3+=1
            else:
                temp[p3] = arr[p2]
                p2+=1
                p3+=1
        while (p1<=mid):
            temp[p3]=arr[p1]
            p1+=1
            p3+=1
        while (p2<=end):
            temp[p3] = arr[p2]
            p2+=1
            p3+=1
        # Copy the temp array elements into main array.
        n = end - start + 1
        for i in range(n):
            j = start + i
            arr[j] = temp[i]
    # Using merge function, the merge_sort can be done.
    def mergeSort(self, arr, start, end):
        # base case
        if start==end:
            return
        else:
            mid = (start + end) // 2
            self.mergeSort(arr, start, mid)
            self.mergeSort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)
        return arr


arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
solution = Solution()
new_array = solution.merge_sort(arr, 0, len(arr)-1)
print(new_array)

```

### Analysis

`Time complexity`: `O(NlogN)`, where at each level we are doing `N` sorting for whole array and after each level the tree is divided by two `logN`.
`Space Complexity`: `O(N)` because of the temp array we have created in merge function.

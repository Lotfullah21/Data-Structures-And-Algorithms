## Merge Sort:

It is one other types of algorithms that works based on divide, conquer and merge.

Some key features:

- Stable Algorithm
- `O(NlogN)` time complexity and `O(1)` space complexity.
- Well suited for linked list, works with `O(1)` auxiliary space.
- Used in Java and Python sorting algorithms.
- in arrays, Quick sort algorithm is preferable.

### Idea-1:

Create a new array of size (n+m) where n is the size of first array and m is the size of 2nd array. after creating the new array, add array-1 and array-2 elements into a new array and then sort the newly created array(array-3).

Time complexity will be `O((n+m)*logN)`.

### Idea-2:

Create an empty array of size(n+m).
Compare each element of array-1 and array-2.
Put the smaller one into array-3.
Continue this until all elements from both array are compared and appended into the array-3.

We need three pointers to keep track of indices in each of the array.
p1 for array-1.
p2 for array-2.
p3 for array-3.

```py

def mergeTwoSortedArray(arr1: list, arr2: list) -> list:
    "merge two sorted arrays."
    p1 = 0
    p2 = 0
    p3 = 0
    n = len(arr1)
    m = len(arr2)
    c = [[] for _ in range((n+m))]
    # Check until the elements are present in both fo the lists.
    while (p1<n and p2<m):
        if arr1[p1]<arr2[p2]:
            c[p3] = arr1[p1]
            p1+=1
            p3+=1
        else:
            c[p3] = arr2[p2]
            p2+=1
            p3+=1
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-1, put its elements inside p3.
    while (p1<n):
        c[p3] = arr1[p1]
        p1+=1
        p3+=1
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-2, put its elements inside p3.
    while (p2<m):
        c[p3] = arr2[p2]
        p2+=1
        p3+=1
    return c
array_1 = [1, 2, 3, 4]
array_2 = [5, 6, 7, 8]
new_arr = mergeTwoSortedArray(array_1,array_2)
print(new_arr)

```

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
    def merge_sort(self, arr, start, end):
        # base case
        if start==end:
            return
        else:
            mid = (start + end) // 2
            self.merge_sort(arr, start, mid)
            self.merge_sort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)
        return arr


arr = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
solution = Solution()
new_array = solution.merge_sort(arr, 0, len(arr)-1)
print(new_array)

```

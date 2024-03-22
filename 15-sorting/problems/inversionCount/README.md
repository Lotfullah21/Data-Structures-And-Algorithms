### Idea-1: Brute Force

Time complexity `O(N^2)` ans space complexity `O(1)`

```py
class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    ans +=1
        return ans

```

### Idea-1

To do it in `O(NlogN)`, why not use merge sort.
At every step, sort and count if there is a an inversion, which means arr[p]>arr[p2].
if one element in a sorted array is greater than an element in a second array, then all elements on its right-side is also greater than the element in 2nd array.
For instance,

```py
arr1 = [1, 10, 20, 30, 40]
arr2 = [1, 2, 3, 4,  8]
in arr1 at index 1, 10 is greater than 1 and the array is sorted.
It means that all element after 10 is also greater than 1.
10>1
20>1
30>1
40>1.
so at index 1, we are having 4 inversion counts.

at index 1, for element 2 in array2.
10>2
20>2
30>2
40>2.

So at index 2, we are having 4 inversion counts.

At index 3, for element 3 in array2.
10>3
20>3
30>3
40>3.

So at index 3, we are having 4 inversion counts.

At index 4, for element 4 in array2.
10>4
20>4
30>4
40>4.

So at index 4, we are having 4 inversion counts.



At index 5, for element 8 in array2.
10>8
20>8
30>8
40>8.

So at index 5, we are having 4 inversion counts.

In total there 16 inversion count.
```

The idea is to use merge sort algorithm, but at the same time sorting is done, a comparison across the elements of array also had to be done if the element in array1>array2,
increase the inversion count.

To count number of inversions, first the comparison is done across two elements and in 2nd step across arrays.

```py
class Solution:

    def inversionCount(self, arr,n):
        self.ans = 0
        self.merge_sort(arr, 0, len(arr) - 1)
        return self.ans

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
        # return arr

    def merge(self ,arr,start: int, mid: int, end: int) -> list:
        p1 = start
        p2 = mid+1
        p3 = 0
        ans  = 0
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
                self.ans += (mid - p1 + 1)
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
        return ans

arr = [3, 4, -5, 0, 1, 20, 11, 9, 4, 7, 13, -4,0]
solution = Solution()
new_array = solution.inversionCount(arr,len(arr)-1)
print(new_array)

```

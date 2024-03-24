### Algorithm

The idea is to keep all the elements smaller than the first element at the left hand side and all the elements greater than 0th index to the right hand side.

#### Steps

- keep two pointers.
- p1 for elements smaller than arr[s].
- p2 for elements greater than arr[s].
- check if arr[p1] is smaller than arr[s].
- if true, increment the p1.
- check if the arr[p2] is greater than arr[s].
- if true, decrement the p2.
- if none of the condition is true
  - swap p1 and p2
  - increment and decrement p1 and p2.
- swap the 0th index with p2.

```py
def reArrange(arr: list) -> list:
    n = len(arr)
    s = 0
    p1 = 1
    p2 = n - 1
    while p1<=p2:
        if arr[p1]<=arr[s]:
            p1+=1
        elif arr[p2]>arr[s]:
            p2-=1
        else:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    temp = arr[s]
    arr[s] = arr[p2]
    arr[p2] = temp

arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
reArrange(arr)
print(arr) // [2, 4, 5, -1, 6, 1, 10, 18, 29, 11, 17]; all elements to the left side fo 10 is smaller than 10.


```

### Q2: Sub Array Re-Arrangement

in the given question, all the steps of the first question will be followed.
The only difference there is that the start and end indices are different;Not necessarily 0th and n-1th index.
And also, after re-arrangements the array won't be smaller from the 0th till the start point, because it is a sub-array and the index does not start from 0th index.

```py
def reArrangeSubArray(arr: list, start: int, end: int) -> list:
    p1 = start + 1
    p2 = end
    while p1<=p2:
        if arr[p1]<=arr[start]:
            p1+=1
        elif arr[p2]>arr[start]:
            p2-=1
        else:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    temp = arr[start]
    arr[start] = arr[p2]
    arr[p2] = temp
    return p2



arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
reArrangeSubArray(arr, 1, 6)
print(arr) // [10, 1, 4, 17, 6, 5, 29, 18, 2, 11, -1]; all the elements to the left side of 1st index is not smaller, because the starting index is 1.

```

###### User Based

```py

def main():
    n, start, end = map(int, input().split())
    arr = list(map(int, input().split()))
    reArrangeSubArray(arr, start, end)
    for e in arr:
        print(e, end=" ")

def reArrangeSubArray(arr: list, start: int, end: int) -> list:
    p1 = start + 1
    p2 = end
    while p1<=p2:
        if arr[p1]<=arr[start]:
            p1+=1
        elif arr[p2]>arr[start]:
            p2-=1
        else:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    temp = arr[start]
    arr[start] = arr[p2]
    arr[p2] = temp
if __name__ == "__main__":
    main()
```

## Quick Sort:

Follow the re-arranging procedure but use recursion to arrange the smallest element which is a single element.
each time the `reArrangeArray` function is called, it returns the index which the current element shifted, or the correct position of the left most element.
Now, that index is pivotal in moving to the left and right side of the original array to sort.

```py
    def quickSort(self,arr,low,high):
        if low>=high:
            return
        p = self.reArrangeSubArray(arr, low, high)
        self.quickSort(arr, low, p-1)
        self.quickSort(arr,p+1, high)
```

The base case is when the left and right side cross each other or start index == end index.

#### Analysis

- The nightmare for quick sort happens when the array is sorted and quick sort pointers one point at each call.
  So, the `reArrangeArray` takes `O(N)` operations, and if `quickSort` is also called `N` times, then, the time complexity would be `O(N^2)`.

- Space complexity is the stack space we are using to call the functions repeatedly and that is `O(N)`.

#### Note:

On average, the time complexity is `O(NlogN)` and space complexity is `O(logN)`

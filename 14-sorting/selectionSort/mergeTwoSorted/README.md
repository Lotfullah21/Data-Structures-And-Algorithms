### Question:

Given two different sorted array, merge them into one array and sort them.

A: [1, 2, 3, 4]
B: [0, 5, 6]
Output: [0, 1, 2, 3, 4, 5, 6]
Explanation: The output is combination of array A and B in sorted order after merging.

#### Idea-1:

- Create an array of C with size (A+B)
- Copy all element from array A and B to the new Array.
- Use `C.sort()` to sort them.

```py
def mergeTwoArrays(a: list, b: list) -> list:
    sizeA = len(a)
    sizeB = len(b)
    c = a[:] + b[:]
    c.sort()
    return c
a = [1, 2]
b = [0,-32]
result = mergeTwoArrays(a, b)
print(result)
```

### Analysis

`Time complexity`: `O((n+m)logN)` because of sorting.
`Space Complexity`: `O(a+b)`.

#### Idea-2:

Do not use any sorting algorithm, but selection sort technique can be implemented.

- Create an empty array of size(n+m).
- Compare each element of array-1 and array-2.
- Put the smaller one into array-3.
- Continue this until all elements from both array are compared and appended into the array-3.
  - compare m[a] with n[b], which ever smaller, put it in array c and increment array c and array m's pointers.

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
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-1, put its elements inside temp.
    while (p1<n):
        c[p3] = arr1[p1]
        p1+=1
        p3+=1
    # After the above loop is finished, one of the loops is going to be empty, now if that non-empty one is array-2, put its elements inside temp.
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

### Analysis

`Time complexity`: `O(arrayM + arrayN)` because of comparing and appending elements.
`Space Complexity`: `O(arrayL)`, in this particular case.

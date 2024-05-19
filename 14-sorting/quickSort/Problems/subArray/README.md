### Question:

Given N elements, Rearrange the array so that

a) arr[start] should go to correct sorted position
b) all elements <=arr[start] should go to left side of arr[start]
c) all elements >arr[start] should go to right side of arr[start]

after moving the elements to the left and right side of the target, the elements should be sorted necessarily.

Input: [6, 2, 3, 1, 12,9, 0,11]
start = 2nd index
end = 5th index
Output: [6, 2, 1, 3, 12,9, 0,11]

Explanation: all element smaller than `3` are on the left hand side and larger than `3` are on the right hand side, the range that is calculating smaller and larger elements are from (2-5)index, any element beyond these indices are not considered.

### Idea:

Use two pointers.

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

in the given question, all the steps of the first question will be followed.
The only difference there is that the start and end indices are different;Not necessarily 0th and n-1th index.
And also, after re-arrangements the array won't be smaller from the 0th till the start point, because it is a sub-array and the index does not start from 0th index.

```py

def reArrange(arr: list, start: int, end: int) -> list:
    """Move all elements smaller than starting index element to the left and larger elements to the right

    Args:
        arr (list): list of integers.
        start (int): start of sub array.
        end   (int): end of sub array.

    Returns:
        list: A modified list that all elements smaller than starting index should move to the left and larger elements to the right.
    """
    n = len(arr)
    p1 = start+1
    p2 = n - 1
    # As long as p1 and p2 did not cross each other, continue.
    while p1<=p2:
        # If element of p1 is smaller than start, increment the p1.
        if arr[p1]<=arr[start]:
            p1+=1
        # If element of p2 is larger than start, decrement the p2. p2 starts from last index.
        elif arr[p2]>arr[start]:
            p2-=1
        else:
            # If none of the above conditions meets, p1 and p2 are not in the right place swap them.
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p2-=1
            p1+=1
    # Swap the oth index element with element at pointer p2.
    temp = arr[start]
    arr[start] = arr[p2]
    arr[p2] = temp

arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
start = 4
end = 6
reArrange(arr,start,end)
print(arr)
```

### Analysis:

`Time complexity`: `O(N)`, because of traversing whole array and doing swap operation.
`Space Complexity`: `O(1)`, No extra space used.

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
    main
```

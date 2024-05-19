### Question:

Given an array of 0s, 1s, and 2s. Arrange the array elements such that all 0s come first, followed by all the 1s and then, all the 2s.

Note: Do not use the inbuilt sort function.

### Idea-1:

Use `arr.sort()`

### Idea-2:

Use three loops and append them in order

```py
def sortArr(arr: list) -> list:
    "Sort an array of 0's, 1's and 2's"
    n = len(arr)
    temp = []
    for ele in arr:
        if ele==0:
            temp.append(ele)
    for ele in arr:
        if ele==1:
            temp.append(ele)
    for ele in arr:
        if ele==2:
            temp.append(ele)
    for i in range(n):
        arr[i] = temp[i]
    return arr
```

`Time complexity`: `O(3*N)==O(N)`, three for loops.
`Space Complexity`: `O(n)`, because of temp array.

### Dutch National Flag Algorithm

Create 4 sections, each assigned to a specific number except one section which will be unknown.

### Analysis

`Time complexity`: `O(N)`, just while loop.
`Space Complexity`: `O(1)`, No extra space is used.

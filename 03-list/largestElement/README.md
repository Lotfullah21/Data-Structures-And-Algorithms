#### Question:

Given an array of elements, find the largest element in the list.

#### Idea-1:

Go through a loop and compare each element to all other element in the list

```py
def getMax(list: list) -> int:
    "Returns the largest element from a list."
    for x in list:
        for y in list:
            if y>x:
                break
        else:
            return x


largest = getMax([1, 2, 3, 4, 5, 6])
print("largest element", largest)
```

#### Analysis:

`Time Complexity` is `O(N^2)`, because we are having a nested loop.
`Space Complexity` is `O(1)`, no extra space used.

#### Idea-2:

keep a reference value and compare to all values, if other values are greater update the max to new max and return it.

```py
def getMax(list: list) -> int:
    "Returns the largest element from a list."
    # Check list is empty
    if not list:
        return "LIST EMPTY"

    maximum = float("-inf")
    n = len(list)
    for i in range(n):
        if list[i]>maximum:
            maximum = list[i]
    return maximum


largest = getMax([1, 2, 3, 4, 5, 6])
print("largest element is =", largest)

```

#### Analysis:

`Time Complexity` is `O(N)`, because we are checking for all elements.
`Space Complexity` is `O(1)`, no extra space used.

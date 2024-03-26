#### Question:

Given an array, reverse the array.

Input: [1, 2, 3, 4, 5, 6, 7]
Output: [7, 6, 5, 4, 3, 2, 1]

#### Solution:

Reversing a list is doing multiple swap operation.

#### Algorithm:

- initialize the starting point to the first index.
- initialize the end point to the last index.
- start swapping the elements of starting point with ending point.
- at every swapping, increment starting index by and decrement end point by 1.
- when starting point crosses ending point; stop!

```py
def reverseList(arr: list) -> list:
    "Reverse the given list"
    start = 0
    end = len(arr)-1
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    return arr

```

#### Python built-in methods

```py
arr.reverse() // it mutates the original array
newArray = list(reversed(arr)) // creates a new array and saves the reversed list of original array, we need extra space here.
reversed(arr) an iterator object, we need to convert to a list.
newArray = arr[::-1] // saves a reversed copy of original array.


arr.reverse() methods works only for mutable objects like list, if we try it with strings or integers, it does not work, because those objects are immutable.


```
